# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './SiteList/SiteWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SiteItem(object):
    def setupUi(self, SiteItem):
        SiteItem.setObjectName("SiteItem")
        SiteItem.resize(842, 215)
        SiteItem.setStyleSheet("background-color: rgba(38, 68, 83, 92);\n"
"color: rgba( 64, 230, 64, 255);")
        self.site_item_wdg = QtWidgets.QWidget(SiteItem)
        self.site_item_wdg.setGeometry(QtCore.QRect(10, 0, 831, 205))
        self.site_item_wdg.setStyleSheet("QLineEdit: {\n"
"background-color: rgb(32, 74, 135);\n"
"}")
        self.site_item_wdg.setObjectName("site_item_wdg")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.site_item_wdg)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.site_item_wdg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.name_txbx = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_txbx.sizePolicy().hasHeightForWidth())
        self.name_txbx.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.name_txbx.setFont(font)
        self.name_txbx.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.298969 rgba(0, 0, 0, 40), stop:1 rgba(0, 0, 0, 30));")
        self.name_txbx.setObjectName("name_txbx")
        self.horizontalLayout_6.addWidget(self.name_txbx)
        self.remove_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_btn.sizePolicy().hasHeightForWidth())
        self.remove_btn.setSizePolicy(sizePolicy)
        self.remove_btn.setMinimumSize(QtCore.QSize(5, 0))
        self.remove_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.remove_btn.setFont(font)
        self.remove_btn.setStyleSheet("background-color: rgb(102, 10, 10);\n"
"color: rgb(252, 233, 79);")
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout_6.addWidget(self.remove_btn)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.site_item_wdg)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.src_path_btn = QtWidgets.QPushButton(self.frame_6)
        self.src_path_btn.setObjectName("src_path_btn")
        self.verticalLayout_5.addWidget(self.src_path_btn)
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_3 = QtWidgets.QFrame(self.frame_7)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.path_txbx = QtWidgets.QLineEdit(self.frame_3)
        self.path_txbx.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.path_txbx.setObjectName("path_txbx")
        self.verticalLayout_4.addWidget(self.path_txbx)
        self.ipfs_cid_txbx = QtWidgets.QLineEdit(self.frame_3)
        self.ipfs_cid_txbx.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.ipfs_cid_txbx.setObjectName("ipfs_cid_txbx")
        self.verticalLayout_4.addWidget(self.ipfs_cid_txbx)
        self.ipns_key_id_txbx = QtWidgets.QLineEdit(self.frame_3)
        self.ipns_key_id_txbx.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.ipns_key_id_txbx.setObjectName("ipns_key_id_txbx")
        self.verticalLayout_4.addWidget(self.ipns_key_id_txbx)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.frame_7)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.update_txbx = QtWidgets.QPushButton(self.frame)
        self.update_txbx.setObjectName("update_txbx")
        self.verticalLayout.addWidget(self.update_txbx)
        self.open_cid_txbx = QtWidgets.QPushButton(self.frame)
        self.open_cid_txbx.setObjectName("open_cid_txbx")
        self.verticalLayout.addWidget(self.open_cid_txbx)
        self.open_txbx = QtWidgets.QPushButton(self.frame)
        self.open_txbx.setObjectName("open_txbx")
        self.verticalLayout.addWidget(self.open_txbx)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_7)

        self.retranslateUi(SiteItem)
        QtCore.QMetaObject.connectSlotsByName(SiteItem)

    def retranslateUi(self, SiteItem):
        _translate = QtCore.QCoreApplication.translate
        SiteItem.setWindowTitle(_translate("SiteItem", "Form"))
        self.name_txbx.setToolTip(_translate("SiteItem", "IPNS key local name (only exists in the context of this computer)"))
        self.remove_btn.setToolTip(_translate("SiteItem", "delete this Site and its IPNS key"))
        self.remove_btn.setText(_translate("SiteItem", "–"))
        self.src_path_btn.setText(_translate("SiteItem", "source path"))
        self.label_6.setToolTip(_translate("SiteItem", "the IPFS CID of the currently published version of the Site, changes with every update"))
        self.label_6.setText(_translate("SiteItem", "IPFS CID"))
        self.label_5.setToolTip(_translate("SiteItem", "IPNS key of this site, never changes"))
        self.label_5.setText(_translate("SiteItem", "IPNS"))
        self.path_txbx.setToolTip(_translate("SiteItem", "source file/folder for this Site"))
        self.ipfs_cid_txbx.setToolTip(_translate("SiteItem", "the IPFS CID of the currently published version of the Site, changes with every update"))
        self.ipns_key_id_txbx.setToolTip(_translate("SiteItem", "IPNS key of this site, never changes"))
        self.update_txbx.setToolTip(_translate("SiteItem", "update this Site from the source path, uploading the source to IPFS and assigning it to this IPNS key"))
        self.update_txbx.setText(_translate("SiteItem", "Update from Source"))
        self.open_cid_txbx.setToolTip(_translate("SiteItem", "open this Site in your browser using the IPFS CID"))
        self.open_cid_txbx.setText(_translate("SiteItem", "Open in Browser"))
        self.open_txbx.setToolTip(_translate("SiteItem", "open this Site in your browser using the IPNS key"))
        self.open_txbx.setText(_translate("SiteItem", "Open in Browser"))
