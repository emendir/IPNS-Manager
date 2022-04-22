import IPFS_API
import json
import os
import shutil
import pathlib
import sys

from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtGui

import appdirs
from MainWindow import Ui_MainWindow
from Site import Site
from SiteList.SiteListObject import SiteListObject

# move existing appdata from /IPFS/IPNS-Manager to /IPNFS-Manager
if os.path.exists(os.path.join(appdirs.user_data_dir(), "IPFS", "IPNS-Manager")) and not os.path.exists(os.path.join(appdirs.user_data_dir(), "IPNS-Manager")):
    shutil.move(os.path.join(appdirs.user_data_dir(), "IPFS", "IPNS-Manager"),
                os.path.join(appdirs.user_data_dir(), "IPNS-Manager"))

appdata_dir = os.path.join(appdirs.user_data_dir(), "IPNS-Manager")

if os.path.exists("MainWindow.ui"):
    Ui_MainWindow, QMainWindow = loadUiType('MainWindow.ui')


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
        exec(self.prepublish_codebox.toPlainText())

    def RunPostPublishCode(self, source_path, old_ipfs_cid, new_ipfs_cid, ipns_key_id, ipns_key_name):
        """Runs the user's custom code, using the paramaters of this function
        (attributes of the currently updates Site) as variables which they can access.
        Gets called when a SiteWidget's 'Update from Path' button is pressed."""
        exec(self.postpublish_codebox.toPlainText())


app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
