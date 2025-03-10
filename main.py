# -*- coding: utf-8 -*-
# !/usr/bin/python3
# SQM的数据分析工具。给自己玩切勿商用
# v1.5.1  更新自动识别txt文件编码功能
# 2025-03-09
# 作者：SQM

import os
import sys

from PySide6.QtGui import QDragEnterEvent, QDropEvent, QStandardItemModel
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
)

import db_fun
import file_fun
from main_ui import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.is_running = False  # 用于控制是否停止处理

        # 初始化 TableView
        self.list_echo = self.ui.list_echo  # 获取 TableView
        self.model = QStandardItemModel()  # 创建数据模型
        self.list_echo.setModel(self.model)  # 将模型设置到 TableView
        self.list_echo.resizeColumnsToContents()  # 自动调整列宽

        # 连接信号槽
        self.ui.start_db_but.clicked.connect(lambda: file_fun.start_db(self))
        self.ui.list_clear.clicked.connect(lambda: file_fun.clear_table(self))

        self.ui.db_select_but.clicked.connect(lambda: db_fun.db_select(self))
        self.ui.db_clear.clicked.connect(lambda: db_fun.数据库清理(self))
        self.ui.select_yufa.clicked.connect(lambda: db_fun.select_yufa(self))

        self.ui.select_one.clicked.connect(lambda: db_fun.查询上线(self))
        self.ui.show_guanxi.clicked.connect(lambda: db_fun.生成树状图(self))

        # 没有数据库时默认按键不可用
        self.ui.db_select_but.setEnabled(False)
        self.ui.db_clear.setEnabled(False)
        self.ui.select_one.setEnabled(False)
        self.ui.show_guanxi.setEnabled(False)

    def 初始化(self):
        功能说明 = [
            "1. 拖入文件到窗口，点击开始导入数据,没有数据库时会自动创建",
            "2. 输入txt文件，默认分隔符必须是 ---- ",
            "3. 可以使用sql语句查询内容，不会语句的可以点查询语法按钮查看",
            "4. 单人上线查询功能需要输入id列，姓名列，上线列，上线id列, id列必须是唯一的，可以是电话或者id",
            "5. 列名默认为A-Z"
            "6. 必须先查询过单人，然后才能生成树状图"
            "7. 生成的树状图会在程序文件夹下生成，是html文件，可以用浏览器打开",
        ]
        file_fun.append_to_table(self, 功能说明)
        self.list_echo.resizeColumnsToContents()  # 自动调整列宽

    def dragEnterEvent(self, event: QDragEnterEvent):  # 拖拽文件到窗口
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):  # 处理拖拽到窗口的文件
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            file_fun.file_name.append(file_path)
            file_fun.file_path = os.path.split(file_fun.file_name[0])[0] + "/"
            for filename in file_fun.file_name:
                file_fun.append_to_table(self, [f"输入的文件名为：{filename}"])
            file_fun.append_to_table(self, [f"输出的文件夹为: {file_fun.file_path}"])
            self.list_echo.resizeColumnsToContents()  # 自动调整列宽

    def closeEvent(self, event):  # 关闭后清理数据库
        db_fun.数据库清理(self)
        db_fun.delete_database(self)
        super(MainWindow, self).closeEvent(
            event
        )  # 调用基类的 closeEvent 方法以确保窗口关闭


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec())
