# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './SiteList/SiteListWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(984, 706)
        Form.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(138, 226, 52);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Contact_scroll = QtWidgets.QScrollArea(Form)
        self.Contact_scroll.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Contact_scroll.sizePolicy().hasHeightForWidth())
        self.Contact_scroll.setSizePolicy(sizePolicy)
        self.Contact_scroll.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Contact_scroll.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Contact_scroll.setAutoFillBackground(False)
        self.Contact_scroll.setStyleSheet("color: rgba(191, 64, 64, 0);")
        self.Contact_scroll.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Contact_scroll.setFrameShape(QtWidgets.QFrame.Box)
        self.Contact_scroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Contact_scroll.setLineWidth(1)
        self.Contact_scroll.setMidLineWidth(0)
        self.Contact_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Contact_scroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Contact_scroll.setWidgetResizable(True)
        self.Contact_scroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Contact_scroll.setObjectName("Contact_scroll")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 970, 674))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_4.setStyleSheet("gridline-color: rgba(191, 64, 64, 0);\n"
"border-color: rgba(191, 64, 64, 0);\n"
"color: rgba(191, 64, 64, 0);")
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.OtherContacts_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.OtherContacts_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OtherContacts_3.sizePolicy().hasHeightForWidth())
        self.OtherContacts_3.setSizePolicy(sizePolicy)
        self.OtherContacts_3.setMinimumSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 68, 83, 92))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 230, 64, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.OtherContacts_3.setPalette(palette)
        self.OtherContacts_3.setStyleSheet("background-color: rgba(38, 68, 83, 92);\n"
"color: rgba( 64, 230, 64, 255);")
        self.OtherContacts_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OtherContacts_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OtherContacts_3.setLineWidth(0)
        self.OtherContacts_3.setObjectName("OtherContacts_3")
        self.siteslist_lyt = QtWidgets.QFormLayout(self.OtherContacts_3)
        self.siteslist_lyt.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.siteslist_lyt.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.siteslist_lyt.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.siteslist_lyt.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.siteslist_lyt.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.siteslist_lyt.setContentsMargins(0, 0, 0, 0)
        self.siteslist_lyt.setSpacing(0)
        self.siteslist_lyt.setObjectName("siteslist_lyt")
        self.verticalLayout_5.addWidget(self.OtherContacts_3)
        self.Contact_scroll.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout.addWidget(self.Contact_scroll)
        self.add_site_btn = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_site_btn.sizePolicy().hasHeightForWidth())
        self.add_site_btn.setSizePolicy(sizePolicy)
        self.add_site_btn.setMinimumSize(QtCore.QSize(10, 30))
        self.add_site_btn.setStyleSheet("")
        self.add_site_btn.setObjectName("add_site_btn")
        self.verticalLayout.addWidget(self.add_site_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_site_btn.setToolTip(_translate("Form", "add a new site with a new IPNS name"))
        self.add_site_btn.setText(_translate("Form", "New Site"))
