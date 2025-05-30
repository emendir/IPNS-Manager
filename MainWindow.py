# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_widget_tlbx = QtWidgets.QToolBox(self.centralwidget)
        self.main_widget_tlbx.setToolTip("")
        self.main_widget_tlbx.setObjectName("main_widget_tlbx")
        self.SitesPage = QtWidgets.QWidget()
        self.SitesPage.setGeometry(QtCore.QRect(0, 0, 787, 442))
        self.SitesPage.setObjectName("SitesPage")
        self.sitespage_lyt = QtWidgets.QVBoxLayout(self.SitesPage)
        self.sitespage_lyt.setObjectName("sitespage_lyt")
        self.main_widget_tlbx.addItem(self.SitesPage, "")
        self.PostPublishCodPage = QtWidgets.QWidget()
        self.PostPublishCodPage.setGeometry(QtCore.QRect(0, 0, 775, 496))
        self.PostPublishCodPage.setObjectName("PostPublishCodPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PostPublishCodPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.PostPublishCodPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.PostPublishCodPage)
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.prepublish_codebox = QtWidgets.QTextEdit(self.PostPublishCodPage)
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        self.prepublish_codebox.setFont(font)
        self.prepublish_codebox.setObjectName("prepublish_codebox")
        self.verticalLayout.addWidget(self.prepublish_codebox)
        self.prepublish_code_save_btn = QtWidgets.QPushButton(self.PostPublishCodPage)
        self.prepublish_code_save_btn.setObjectName("prepublish_code_save_btn")
        self.verticalLayout.addWidget(self.prepublish_code_save_btn)
        self.main_widget_tlbx.addItem(self.PostPublishCodPage, "")
        self.PostPublishCodPage1 = QtWidgets.QWidget()
        self.PostPublishCodPage1.setGeometry(QtCore.QRect(0, 0, 145, 864))
        self.PostPublishCodPage1.setObjectName("PostPublishCodPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PostPublishCodPage1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.PostPublishCodPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.PostPublishCodPage1)
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.postpublish_codebox = QtWidgets.QTextEdit(self.PostPublishCodPage1)
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        self.postpublish_codebox.setFont(font)
        self.postpublish_codebox.setObjectName("postpublish_codebox")
        self.verticalLayout_2.addWidget(self.postpublish_codebox)
        self.postpublish_code_save_btn = QtWidgets.QPushButton(self.PostPublishCodPage1)
        self.postpublish_code_save_btn.setObjectName("postpublish_code_save_btn")
        self.verticalLayout_2.addWidget(self.postpublish_code_save_btn)
        self.main_widget_tlbx.addItem(self.PostPublishCodPage1, "")
        self.horizontalLayout.addWidget(self.main_widget_tlbx)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.main_widget_tlbx.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_widget_tlbx.setItemText(self.main_widget_tlbx.indexOf(self.SitesPage), _translate("MainWindow", "Sites"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Here you can add python code to be run every time you press a Site\'s &quot;Update from path&quot; button. This code gets executed just before the site folder/file is uploaded to IPFS, so it\'s a great way to automate adding some finishing touches to the site before it\'s published.</p><p>You have access to the following variables that belong to that Site, as well as the <a href=\"https://github.com/emendir/IPFS-Toolkit-Python\"><span style=\" text-decoration: underline; color:#2eb8e6;\">IPFS-Toolkit </span></a>module and os, shutil, pathlib, json &amp; sys.</p><p> If you don\'t want IPNS manager to add the source as-is to IPFS, you can publish whatever you want to IPFS and set the variable `new_ipfs_cid` to your own IPFS-content\'s CID.</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "source_path\n"
"old_ipfs_cid\n"
"new_ipfs_cid\n"
"ipns_key_id\n"
"ipns_key_name"))
        self.prepublish_codebox.setToolTip(_translate("MainWindow", "enter your python code here"))
        self.prepublish_code_save_btn.setToolTip(_translate("MainWindow", "save your custom python code"))
        self.prepublish_code_save_btn.setText(_translate("MainWindow", "Save"))
        self.main_widget_tlbx.setItemText(self.main_widget_tlbx.indexOf(self.PostPublishCodPage), _translate("MainWindow", "Pre-Publish Code Execution"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Here you can add python code to be run every time you press a Site\'s &quot;Update from path&quot; button. This code gets executed right after the site folder/file is uploaded to IPFS, so it\'s a great way round off your content delivery system by automating the last finish-up processing steps.</p><p>You have access to the following variables that belong to that Site, as well as the <a href=\"https://github.com/emendir/IPFS-Toolkit-Python\"><span style=\" text-decoration: underline; color:#2eb8e6;\">IPFS-Toolkit </span></a>module and os, shutil, pathlib, json &amp; sys:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "source_path\n"
"old_ipfs_cid\n"
"new_ipfs_cid\n"
"ipns_key_id\n"
"ipns_key_name"))
        self.postpublish_codebox.setToolTip(_translate("MainWindow", "enter your python code here"))
        self.postpublish_code_save_btn.setToolTip(_translate("MainWindow", "save your custom python code"))
        self.postpublish_code_save_btn.setText(_translate("MainWindow", "Save"))
        self.main_widget_tlbx.setItemText(self.main_widget_tlbx.indexOf(self.PostPublishCodPage1), _translate("MainWindow", "Post-Publish Code Execution"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
