# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableView,
    QVBoxLayout,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(908, 505)
        icon = QIcon()
        icon.addFile(
            "../SQM\u53d6\u8bc1\u5c0f\u5de5\u5177/favicon.ico",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        Form.setWindowIcon(icon)
        self.horizontalLayout_8 = QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_db_but = QPushButton(Form)
        self.start_db_but.setObjectName("start_db_but")

        self.horizontalLayout_2.addWidget(self.start_db_but)

        self.list_clear = QPushButton(Form)
        self.list_clear.setObjectName("list_clear")

        self.horizontalLayout_2.addWidget(self.list_clear)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.db_str = QLineEdit(Form)
        self.db_str.setObjectName("db_str")

        self.verticalLayout_2.addWidget(self.db_str)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.select_yufa = QPushButton(Form)
        self.select_yufa.setObjectName("select_yufa")

        self.horizontalLayout_4.addWidget(self.select_yufa)

        self.db_select_but = QPushButton(Form)
        self.db_select_but.setObjectName("db_select_but")

        self.horizontalLayout_4.addWidget(self.db_select_but)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.list_echo = QTableView(Form)
        self.list_echo.setObjectName("list_echo")

        self.horizontalLayout_7.addWidget(self.list_echo)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 8)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form", "SQM\u7684\u6570\u636e\u5206\u6790\u5de5\u5177", None
            )
        )
        self.label.setText(
            QCoreApplication.translate("Form", "\u6570\u636e\u8f93\u5165\u533a", None)
        )
        self.start_db_but.setText(
            QCoreApplication.translate("Form", "\u6570\u636e\u5165\u5e93", None)
        )
        self.list_clear.setText(
            QCoreApplication.translate("Form", "\u8868\u683c\u6e05\u7406", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Form", "SQL\u6570\u636e\u67e5\u8be2", None)
        )
        self.select_yufa.setText(
            QCoreApplication.translate("Form", "\u67e5\u8be2\u8bed\u6cd5", None)
        )
        self.db_select_but.setText(
            QCoreApplication.translate("Form", "\u67e5\u8be2", None)
        )

    # retranslateUi
