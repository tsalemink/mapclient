# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pluginfinderdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapclient.view.workflow.workflowsteptreeview import WorkflowStepTreeView


class Ui_PluginFinderDialog(object):
    def setupUi(self, PluginFinderDialog):
        if not PluginFinderDialog.objectName():
            PluginFinderDialog.setObjectName(u"PluginFinderDialog")
        PluginFinderDialog.resize(900, 550)
        self.verticalLayout = QVBoxLayout(PluginFinderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(PluginFinderDialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEditFilter = QLineEdit(self.layoutWidget_2)
        self.lineEditFilter.setObjectName(u"lineEditFilter")

        self.verticalLayout_2.addWidget(self.lineEditFilter)

        self.stepTreeView = WorkflowStepTreeView(self.layoutWidget_2)
        self.stepTreeView.setObjectName(u"stepTreeView")
        self.stepTreeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stepTreeView.setDragEnabled(True)
        self.stepTreeView.setSelectionMode(QAbstractItemView.NoSelection)
        self.stepTreeView.setIconSize(QSize(64, 64))
        self.stepTreeView.setIndentation(0)
        self.stepTreeView.setRootIsDecorated(False)
        self.stepTreeView.setSortingEnabled(False)
        self.stepTreeView.setHeaderHidden(True)
        self.stepTreeView.setExpandsOnDoubleClick(False)

        self.verticalLayout_2.addWidget(self.stepTreeView)

        self.splitter.addWidget(self.layoutWidget_2)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(PluginFinderDialog)

        QMetaObject.connectSlotsByName(PluginFinderDialog)
    # setupUi

    def retranslateUi(self, PluginFinderDialog):
        PluginFinderDialog.setWindowTitle(QCoreApplication.translate("PluginFinderDialog", u"Plugin Finder Tool", None))
        self.lineEditFilter.setText("")
        self.lineEditFilter.setPlaceholderText(QCoreApplication.translate("PluginFinderDialog", u"Filter", None))
    # retranslateUi

