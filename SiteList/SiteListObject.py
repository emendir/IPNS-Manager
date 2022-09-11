from PyQt5.QtGui import QTextFrame, QTextFrameFormat
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTreeView, QApplication, QLineEdit, QWidget, QFileDialog, QInputDialog, QMessageBox
# import PyQt5.QtGui
import webbrowser
import _thread

import sip
from Site import Site
import types
import os
import appdirs
import json

# import the Qt Designer UI files thaat have been converted from *.ui to *.py
from SiteList.SiteListWidget import Ui_Form as SiteListObject
from SiteList.SiteWidget import Ui_SiteItem as SiteWidget

# import Qt Designer *.ui files if they exist/ are accessible to replace the python imports
if os.path.exists("SiteList/SiteListWidget.ui"):
    SiteListObject, QWidget = loadUiType("SiteList/SiteListWidget.ui")
if os.path.exists("SiteList/SiteWidget.ui"):
    SiteWidget, w = loadUiType("SiteList/SiteWidget.ui")


class SiteListObject(QWidget, SiteListObject):
    """
    This is the main area which contains the ScrollArea that
    displays all the IPNS Sites and their attribtes.
    It allows the user to edit the selected Site's properties and configuration.
    """

    def __init__(self, mainwindow):
        super(SiteListObject, self).__init__()
        self.setupUi(self)

        self.mainwindow = mainwindow

        self.add_site_btn.clicked.connect(self.AddSite)
        self.sites = list()

    def AddSiteWidget(self, site):
        """Add a SiteWidget (graphical representation/control-widget for a Site object)
        for the input Site object and add it to the ScrollArea of SiteWidgetss."""
        site_widget = SiteWidget()
        site_widget.setupUi(self)
        site_widget.site = site

        def UpdateRecord(e):
            """Function to be executed when the 'Update from Path' is pressed"""
            nonlocal site_widget
            old_ipfs_cid = site_widget.ipfs_cid_txbx.text()
            site_widget.site.path = site_widget.path_txbx.text()
            site_widget.site.name = site_widget.name_txbx.text()
            plugin_defined_cid = self.mainwindow.RunPrePublishCode(site_widget.site.path, old_ipfs_cid,
                                                                   site_widget.site.ipns_key_id, site_widget.site.ipns_key_name)

            # upload to IPFS, update site.cid, update IPNS record
            site_widget.site.UpdateIPNS_Record(plugin_defined_cid)
            site_widget.ipfs_cid_txbx.setText(site_widget.site.ipfs_cid)
            # execute the user's custom code
            _thread.start_new_thread(self.mainwindow.RunPostPublishCode, (site_widget.site.path, old_ipfs_cid, site_widget.site.ipfs_cid,
                                                                          site_widget.site.ipns_key_id, site_widget.site.ipns_key_name))

        def RemoveSite(e):
            """Function to delete this IPNS Site"""
            conf_mbox = QMessageBox()
            conf_mbox.setWindowTitle("Delete Site?")
            conf_mbox.setText(
                "Are you sure you want to permanently delete this Site and its IPNS record? The site source will not be deleted.")
            conf_mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if conf_mbox.exec_() == QMessageBox.Ok:
                nonlocal site_widget
                site_widget.site.DeleteIPNS_Record()
                self.sites.remove(site_widget)
                self.siteslist_lyt.removeWidget(site_widget.site_item_wdg)
                sip.delete(site_widget.site_item_wdg)
                site_widget = None

        def OpenInBrowser(e):
            nonlocal site_widget
            url = "http://localhost:8080/ipns/" + site_widget.site.ipns_key_id
            webbrowser.open_new_tab(url)

        def OpenCID_InBrowser(e):
            nonlocal site_widget
            url = "http://localhost:8080/ipfs/" + site_widget.site.ipfs_cid
            webbrowser.open_new_tab(url)

        def Path_Edited(syte, e):
            syte.site.path = syte.path_txbx.text()
            self.SaveConfig()

        def IPNS_Name_Edited(syte, e):
            if syte.site.ipns_key_name == "self":
                syte.name_txbx.setText("self")
                return
            syte.site.ChangeIPNS_Name(syte.name_txbx.text())
            self.SaveConfig()

        def ChooseSourcePath():
            def Handler(path):
                site_widget.site.path = path
                site_widget.path_txbx.setText(path)
                self.SaveConfig()

            dialog = FileDialog(self, "Choose Source")

            dialog.Finished = Handler
            result = dialog.show()

        site_widget.remove_btn.clicked.connect(RemoveSite)
        site_widget.update_txbx.clicked.connect(UpdateRecord)
        site_widget.open_txbx.clicked.connect(OpenInBrowser)
        site_widget.open_cid_txbx.clicked.connect(OpenCID_InBrowser)
        site_widget.path_txbx.focusOutEvent = types.MethodType(Path_Edited, site_widget)
        site_widget.name_txbx.focusOutEvent = types.MethodType(IPNS_Name_Edited, site_widget)

        self.siteslist_lyt.addWidget(site_widget.site_item_wdg)
        self.sites.append(site_widget)

        site_widget.ipns_key_id_txbx.setText(site.ipns_key_id)
        site_widget.ipfs_cid_txbx.setText(site.ipfs_cid)
        site_widget.name_txbx.setText(site.ipns_key_name)
        site_widget.path_txbx.setText(site.path)
        site_widget.src_path_btn.clicked.connect(ChooseSourcePath)

        self.mainwindow.resizeEvent(None)

    def AddSite(self, e):
        """Eventhandler for the button for creating a new IPNS key and Site"""
        print(self)
        name, ok = QInputDialog.getText(self, 'IPNS Key', 'Enter the new Site\'s name:')
        if not ok:
            return
        site = Site(name)
        self.AddSiteWidget(site)

    def SaveConfig(self):
        """Save all the IPNS Sites' associated paths to appdata."""
        filewriter = open(os.path.join(self.appdata_dir, "config"), "w+")
        for site_widget in self.sites:
            filewriter.write(json.dumps(
                [site_widget.site.ipns_key_name, site_widget.site.path])+"\n")
        filewriter.close()
        pass


class FileDialog(QFileDialog):
    def __init__(self, *args):
        QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.ExistingFile)
        btns = self.findChildren(QPushButton)
        self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.openClicked)
        self.tree = self.findChild(QTreeView)

    def openClicked(self):
        inds = self.tree.selectionModel().selectedIndexes()
        for i in inds:
            if i.column() == 0:
                self.selectedFile = os.path.join(
                    str(self.directory().absolutePath()), str(i.data()))
                break
        self.hide()
        self.Finished(self.selectedFile)

    def fileSelected(self):
        return self.selectedFile
