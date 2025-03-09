# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(975, 505)
        icon = QIcon()
        icon.addFile(u"../SQM\u53d6\u8bc1\u5c0f\u5de5\u5177/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_8 = QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.start_db_but = QPushButton(Form)
        self.start_db_but.setObjectName(u"start_db_but")

        self.verticalLayout.addWidget(self.start_db_but)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.db_clear = QPushButton(Form)
        self.db_clear.setObjectName(u"db_clear")

        self.horizontalLayout_2.addWidget(self.db_clear)

        self.list_clear = QPushButton(Form)
        self.list_clear.setObjectName(u"list_clear")

        self.horizontalLayout_2.addWidget(self.list_clear)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.db_str = QLineEdit(Form)
        self.db_str.setObjectName(u"db_str")

        self.verticalLayout_2.addWidget(self.db_str)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.select_yufa = QPushButton(Form)
        self.select_yufa.setObjectName(u"select_yufa")

        self.horizontalLayout_5.addWidget(self.select_yufa)

        self.db_select_but = QPushButton(Form)
        self.db_select_but.setObjectName(u"db_select_but")

        self.horizontalLayout_5.addWidget(self.db_select_but)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.data_input = QLineEdit(Form)
        self.data_input.setObjectName(u"data_input")

        self.verticalLayout_3.addWidget(self.data_input)

        self.select_one = QPushButton(Form)
        self.select_one.setObjectName(u"select_one")

        self.verticalLayout_3.addWidget(self.select_one)

        self.show_guanxi = QPushButton(Form)
        self.show_guanxi.setObjectName(u"show_guanxi")
        self.show_guanxi.setAutoDefault(False)
        self.show_guanxi.setFlat(False)

        self.verticalLayout_3.addWidget(self.show_guanxi)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.list_echo = QTableView(Form)
        self.list_echo.setObjectName(u"list_echo")

        self.horizontalLayout_7.addWidget(self.list_echo)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 8)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.retranslateUi(Form)

        self.show_guanxi.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SQM\u7684\u6570\u636e\u5206\u6790\u5de5\u5177", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u8f93\u5165\u533a", None))
        self.start_db_but.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5165\u5e93", None))
        self.db_clear.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u6e05\u9664", None))
        self.list_clear.setText(QCoreApplication.translate("Form", u"\u8868\u683c\u6e05\u7406", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"SQL\u6570\u636e\u67e5\u8be2", None))
        self.select_yufa.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u8bed\u6cd5", None))
        self.db_select_but.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5c42\u7ea7\u5173\u7cfb\u5206\u6790\u533a", None))
        self.data_input.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u8981\u67e5\u8be2\u7684\u552f\u4e00ID", None))
        self.select_one.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u4e2a\u4eba\u4e0a\u7ebf", None))
        self.show_guanxi.setText(QCoreApplication.translate("Form", u"\u5c42\u7ea7\u6811\u72b6\u56fe", None))
    # retranslateUi

