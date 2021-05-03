# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/mapclientplugins/imagesourcestep/widgets/qt/configuredialog.ui',
# licensing of 'src/mapclientplugins/imagesourcestep/widgets/qt/configuredialog.ui' applies.
#
# Created: Wed Jun 26 14:52:32 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(629, 581)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(ConfigureDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.identifierLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.identifierLineEdit.setObjectName("identifierLineEdit")
        self.horizontalLayout.addWidget(self.identifierLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setObjectName("tabWidget")
        self.localTab = QtWidgets.QWidget()
        self.localTab.setObjectName("localTab")
        self.gridLayout = QtWidgets.QGridLayout(self.localTab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.localTab)
        self.label_3.setMinimumSize(QtCore.QSize(71, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.localButton = QtWidgets.QPushButton(self.localTab)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.localButton.setFont(font)
        self.localButton.setObjectName("localButton")
        self.gridLayout.addWidget(self.localButton, 0, 3, 1, 1)
        self.localLineEdit = QtWidgets.QLineEdit(self.localTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localLineEdit.sizePolicy().hasHeightForWidth())
        self.localLineEdit.setSizePolicy(sizePolicy)
        self.localLineEdit.setStyleSheet("selection-color: red;\n"
"color: green")
        self.localLineEdit.setObjectName("localLineEdit")
        self.gridLayout.addWidget(self.localLineEdit, 0, 1, 1, 2)
        self.previousLocationLabel = QtWidgets.QLabel(self.localTab)
        self.previousLocationLabel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.previousLocationLabel.setText("")
        self.previousLocationLabel.setObjectName("previousLocationLabel")
        self.gridLayout.addWidget(self.previousLocationLabel, 1, 2, 1, 1)
        self.tabWidget.addTab(self.localTab, "")
        self.pmrTab = QtWidgets.QWidget()
        self.pmrTab.setObjectName("pmrTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pmrTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget.addTab(self.pmrTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.imageSourceTypeComboBox = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageSourceTypeComboBox.sizePolicy().hasHeightForWidth())
        self.imageSourceTypeComboBox.setSizePolicy(sizePolicy)
        self.imageSourceTypeComboBox.setObjectName("imageSourceTypeComboBox")
        self.imageSourceTypeComboBox.addItem("")
        self.imageSourceTypeComboBox.addItem("")
        self.imageSourceTypeComboBox.addItem("")
        self.imageSourceTypeComboBox.addItem("")
        self.imageSourceTypeComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.imageSourceTypeComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label.setBuddy(self.identifierLineEdit)
        self.label_3.setBuddy(self.localLineEdit)
        self.label_6.setBuddy(self.imageSourceTypeComboBox)

        self.retranslateUi(ConfigureDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtWidgets.QApplication.translate("ConfigureDialog", "Configure - Image Source", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ConfigureDialog", "Identifier:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ConfigureDialog", "Location:", None, -1))
        self.localButton.setText(QtWidgets.QApplication.translate("ConfigureDialog", "...", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.localTab), QtWidgets.QApplication.translate("ConfigureDialog", "Local file system", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pmrTab), QtWidgets.QApplication.translate("ConfigureDialog", "Physiome Model Repository", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ConfigureDialog", "Image Source Type:", None, -1))
        self.imageSourceTypeComboBox.setItemText(0, QtWidgets.QApplication.translate("ConfigureDialog", "from file extension", None, -1))
        self.imageSourceTypeComboBox.setItemText(1, QtWidgets.QApplication.translate("ConfigureDialog", "png (*.png)", None, -1))
        self.imageSourceTypeComboBox.setItemText(2, QtWidgets.QApplication.translate("ConfigureDialog", "jpg (*.jpg, *.jpeg)", None, -1))
        self.imageSourceTypeComboBox.setItemText(3, QtWidgets.QApplication.translate("ConfigureDialog", "TIFF (*.tiff)", None, -1))
        self.imageSourceTypeComboBox.setItemText(4, QtWidgets.QApplication.translate("ConfigureDialog", "DICOM (*.dcm)", None, -1))
