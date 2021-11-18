import sys
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtGui
import os
import IPFS_API
from SiteList.SiteListObject import SiteListObject
from Site import Site
import appdirs
import json
from MainWindow import Ui_MainWindow
if os.path.exists("MainWindow.ui"):
    Ui_MainWindow, QMainWindow = loadUiType('MainWindow.ui')


appdata_dir = os.path.join(appdirs.user_data_dir(), "IPFS", "IPNS-Manager")

if not os.path.exists(appdata_dir):
    os.makedirs(appdata_dir)


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.close()
        # setting icon and window title
        bundle_dir = getattr(
            sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        self.setWindowIcon(QtGui.QIcon(os.path.join(bundle_dir, 'Icon.svg')))
        self.setWindowTitle("IPFS Name Manager")

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
        self.code_save_btn.clicked.connect(self.SaveCode)

        # adding the main area in which the list of IPFS Sites will be displayed
        self.projectslist = SiteListObject(self)
        self.projectslist.appdata_dir = appdata_dir
        self.sitespage_lyt.addWidget(self.projectslist)

        paths = self.LoadPaths()    # load the paths of the IPNS sites from appdata
        keys = IPFS_API.ipfs.key.list().get("Keys")  # get this IPFS node's list of IPNS keys
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
        self.LoadCode()

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

    def LoadCode(self):
        """Loads the user's custom code for execution on every IPNS publish from appdata."""
        codefile_path = os.path.join(appdata_dir, "CodeFile.py")

        if os.path.exists(codefile_path):
            with open(codefile_path, "r") as codefile:
                self.codebox.setPlainText(codefile.read())

    def SaveCode(self, e):
        """Save the user's custom code for execution on every IPNS publish to appdata."""
        with open(os.path.join(appdata_dir, "CodeFile.py"), "w+") as codefile:
            codefile.write(self.codebox.toPlainText())

    def RunCode(self, source_path, old_ipfs_cid, new_ipfs_cid, ipns_key_id, ipns_key_name):
        """Runs the user's custom code, using the paramaters of this function
        (attributes of the currently updates Site) as variables which they can access.
        Gets called when a SiteWidget's 'Update from Path' button is pressed."""
        exec(self.codebox.toPlainText())


app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
