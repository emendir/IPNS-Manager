from inspect import signature
import IPFS_API
import json
import os
import shutil
import pathlib
import sys
import traceback

from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, pyqtProperty, QPropertyAnimation
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

import appdirs
from MainWindow import Ui_MainWindow
from Site import Site
from SiteList.SiteListObject import SiteListObject

# move existing appdata from /IPFS/IPNS-Manager to /IPNFS-Manager
if os.path.exists(os.path.join(appdirs.user_data_dir(), "IPFS", "IPNS-Manager")) and not os.path.exists(os.path.join(appdirs.user_data_dir(), "IPNS-Manager")):
    shutil.move(os.path.join(appdirs.user_data_dir(), "IPFS", "IPNS-Manager"),
                os.path.join(appdirs.user_data_dir(), "IPNS-Manager"))

appdata_dir = os.path.join(appdirs.user_data_dir(), "IPNS-Manager")
if not os.path.exists(appdata_dir):
    os.makedirs(appdata_dir)

if os.path.exists("MainWindow.ui"):
    Ui_MainWindow, QMainWindow = loadUiType('MainWindow.ui')


class Main(QMainWindow, Ui_MainWindow):
    plugins = []

    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.close()
        # setting icon and window title
        bundle_dir = getattr(
            sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        self.setWindowIcon(QtGui.QIcon(os.path.join(bundle_dir, 'Icon.svg')))
        self.setWindowTitle("IPFS Name Manager")
        IPFS_API.Start()
        # waiting till IPFS-API is opened
        while not IPFS_API.started:
            conf_mbox = QMessageBox()
            conf_mbox.setWindowTitle("Is IPFS running?")
            conf_mbox.setText(
                "I can't connect to the IPFS node on this computer. Is IPFS running here?")
            conf_mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if conf_mbox.exec_() == QMessageBox.Ok:
                IPFS_API.Start()
            else:
                self.close()
                QTimer.singleShot(0, self.close)
                return
        self.prepublish_code_save_btn.clicked.connect(self.SavePrePublishCode)
        self.postpublish_code_save_btn.clicked.connect(self.SavePostPublishCode)

        # adding the main area in which the list of IPFS Sites will be displayed
        self.projectslist = SiteListObject(self)
        self.projectslist.appdata_dir = appdata_dir
        self.sitespage_lyt.addWidget(self.projectslist)

        paths = self.LoadPaths()    # load the paths of the IPNS sites from appdata
        keys = IPFS_API.http_client.key.list().get("Keys")  # get this IPFS node's list of IPNS keys
        # adding SiteWidget for each IPNS key
        for key in keys:
            path = ""
            name = key.get("Name")
            id = key.get('Id')
            print(name)
            for entry in paths:
                if entry[0] == name:
                    path = entry[1]
                    break
            self.projectslist.AddSiteWidget(
                Site(name, id, path))

        # loading the user's custom code for execution on IPNS publishes
        self.LoadPrePublishCode()
        self.LoadPostPublishCode()
        self.LoadPlugins()

    def LoadPaths(self):
        """Loads the paths (files or folders) associated with IPNS keys from appdata."""
        try:
            filereader = open(os.path.join(appdata_dir, "config"), "r")
            lines = filereader.readlines()
            filereader.close()
            paths = list()
            for line in lines:
                paths.append(json.loads(line))
            return paths
        except:
            return list()

    def LoadPrePublishCode(self):
        """Loads the user's custom code for execution on every IPNS publish from appdata."""
        prepublish_codefile_path = os.path.join(appdata_dir, "prepublish_codefile.py")

        if os.path.exists(prepublish_codefile_path):
            with open(prepublish_codefile_path, "r") as prepublish_codefile:
                self.prepublish_codebox.setPlainText(prepublish_codefile.read())

    def LoadPostPublishCode(self):
        """Loads the user's custom code for execution on every IPNS publish from appdata."""
        postpublish_codefile_path = os.path.join(appdata_dir, "postpublish_codefile.py")

        if os.path.exists(postpublish_codefile_path):
            with open(postpublish_codefile_path, "r") as postpublish_codefile:
                self.postpublish_codebox.setPlainText(postpublish_codefile.read())

    def SavePrePublishCode(self, e):
        """Save the user's custom code for execution on every IPNS publish to appdata."""
        with open(os.path.join(appdata_dir, "prepublish_codefile.py"), "w+") as prepublish_codefile:
            prepublish_codefile.write(self.prepublish_codebox.toPlainText())

    def SavePostPublishCode(self, e):
        """Save the user's custom code for execution on every IPNS publish to appdata."""
        with open(os.path.join(appdata_dir, "postpublish_codefile.py"), "w+") as postpublish_codefile:
            postpublish_codefile.write(self.postpublish_codebox.toPlainText())

    def RunPrePublishCode(self, source_path, old_ipfs_cid, ipns_key_id, ipns_key_name):
        """Runs the user's custom code, using the paramaters of this function
        (attributes of the currently updates Site) as variables which they can access.
        Gets called when a SiteWidget's 'Update from Path' button is pressed."""
        Spinner(self)
        try:
            exec(self.prepublish_codebox.toPlainText())
        except:
            print(traceback.format_exc())
        for plugin in self.plugins:
            try:
                plugin.PrePublish(source_path, old_ipfs_cid, ipns_key_id, ipns_key_name)
            except:
                print(traceback.format_exc())

    def RunPostPublishCode(self, source_path, old_ipfs_cid, new_ipfs_cid, ipns_key_id, ipns_key_name):
        """Runs the user's custom code, using the paramaters of this function
        (attributes of the currently updates Site) as variables which they can access.
        Gets called when a SiteWidget's 'Update from Path' button is pressed."""
        try:
            exec(self.postpublish_codebox.toPlainText())
        except:
            print(traceback.format_exc())
        for plugin in self.plugins:
            try:
                plugin.PostPublish(source_path, old_ipfs_cid, new_ipfs_cid,
                                   ipns_key_id, ipns_key_name)
            except:
                print(traceback.format_exc())

    def LoadPlugins(self):
        files = []
        path_1 = "Plugins"
        path_2 = os.path.join(appdata_dir, "Plugins")
        if os.path.exists(path_1):
            files += [os.path.join(path_1, file) for file in os.listdir(path_1)]
        if os.path.exists(path_2):
            files += [os.path.join(path_2, file) for file in os.listdir(path_2)]
        for plugin_path in files:
            file_name = os.path.basename(plugin_path)
            if os.path.isfile(plugin_path) and file_name[-3:] == ".py" and file_name != "__main__.py":
                try:
                    plugin_name = file_name[:-3]
                    print(f"Loading plugin {plugin_name}")
                    import importlib.util
                    import sys
                    spec = importlib.util.spec_from_file_location(
                        plugin_name, plugin_path)
                    plugin = importlib.util.module_from_spec(spec)
                    sys.modules[plugin_name] = plugin
                    spec.loader.exec_module(plugin)
                    if len(signature(plugin.Plugin).parameters) == 1:
                        plugin_obj = plugin.Plugin(self)
                        if issubclass(plugin.Plugin, QWidget):
                            self.toolBox.addItem(plugin_obj, plugin_obj.plugin_friendly_name)
                    else:
                        plugin_obj = plugin.Plugin()
                    self.plugins.append(plugin_obj)
                except:
                    print("Failed to load plugin", plugin_name)
                    print(traceback.format_exc())


class Spinner(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = QPixmap("Icon.svg")

        self.setFixedSize(30, 30)
        self._angle = 0

        self.animation = QPropertyAnimation(self, b"angle", self)
        self.animation.setStartValue(0)
        self.animation.setEndValue(360)
        self.animation.setLoopCount(-1)
        self.animation.setDuration(2000)
        self.animation.start()

    @pyqtProperty(int)
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
        self.update()

    def paintEvent(self, ev=None):
        painter = QPainter(self)
        painter.translate(15, 15)
        painter.rotate(self._angle)
        painter.translate(-15, -15)
        painter.drawPixmap(5, 5, self.pixmap)


app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
