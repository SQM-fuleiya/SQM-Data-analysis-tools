# -*- coding: utf-8 -*-
# !/usr/bin/python3
# SQM的数据分析工具。给自己玩切勿商用
# v1.0
# 2025-03-03

import os
import sys
import sqlite3
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from main_ui import Ui_Form
import pandas as pd


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.file_name = []
        self.file_path = ""
        self.is_running = False  # 用于控制是否停止处理

        # 初始化 TableView
        self.list_echo = (
            self.ui.list_echo
        )  # 假设 UI 中已经有一个 QTableView，命名为 list_echo
        self.model = QStandardItemModel()  # 创建数据模型
        self.list_echo.setModel(self.model)  # 将模型设置到 TableView
        self.list_echo.resizeColumnsToContents()  # 自动调整列宽
        self.list_echo.setWordWrap(True)  # 启用文本换行

        # 连接信号槽
        self.ui.start_db_but.clicked.connect(self.start_db)
        self.ui.db_select_but.clicked.connect(self.db_select)
        self.ui.select_yufa.clicked.connect(self.select_yufa)
        self.ui.list_clear.clicked.connect(self.clear_table)

        # 初始化进度条

    def start_db(self):
        self.clear_table()  # 清空表格
        if not self.file_name:
            QMessageBox.warning(self, "警告", "请先选择文件！")
            return

        self.is_running = True
        self.ui.start_db_but.setEnabled(False)
        self.append_to_table(["开始导入数据..."])
        for file_idx, file_path in enumerate(self.file_name, 1):
            if not self.is_running:
                break
            try:
                if file_path.endswith(".txt"):
                    self.process_txt_file(file_path)
                elif file_path.endswith((".xlsx", ".xls")):
                    self.process_excel_file(file_path)
            except Exception as e:
                self.append_to_table([f"处理文件{file_path}时出错：{str(e)}"])
                continue
        self.append_to_table(["导入完成！" if self.is_running else "导入已取消"])
        self.ui.start_db_but.setEnabled(True)

    def process_txt_file(self, file_path):
        batch_size = 1000
        batch_data = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f, 1):
                if not self.is_running:
                    break
                data = line.strip().split("----")
                batch_data.append(data)

                if len(batch_data) >= batch_size:
                    self.batch_insert(batch_data)
                    batch_data = []

            if batch_data and self.is_running:
                self.batch_insert(batch_data)

    def process_excel_file(self, file_path):
        try:
            df = pd.read_excel(file_path)
            self.batch_insert(df.values.tolist())
        except Exception as e:
            raise Exception(f"读取Excel文件失败：{str(e)}")

    def batch_insert(self, data):
        if not data:
            return

        columns = [chr(65 + i) for i in range(len(data[0]))]
        placeholders = ",".join(["?"] * len(columns))
        sql = f"INSERT INTO fenxi ({','.join(columns)}) VALUES ({placeholders})"

        try:
            with sqlite3.connect(f"{self.file_path}/demo.db") as conn:
                conn.execute("PRAGMA synchronous = OFF")
                conn.execute("PRAGMA journal_mode = WAL")
                cursor = conn.cursor()

                # 检查表是否存在
                cursor.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='fenxi'"
                )
                if not cursor.fetchone():
                    create_sql = f"CREATE TABLE fenxi ({','.join([f'{col} TEXT' for col in columns])})"
                    cursor.execute(create_sql)

                cursor.executemany(sql, data)
                conn.commit()

                # 将数据输出到表格
                self.append_to_table(columns)  # 添加表头
                for row in data:
                    self.append_to_table(row)  # 添加数据
        except Exception as e:
            raise Exception(f"数据库写入失败：{str(e)}")

    def db_select(self):
        self.clear_table()
        query = self.ui.db_str.text().strip()
        if not query:
            QMessageBox.warning(self, "警告", "请输入查询语句！")
            return

        try:
            with sqlite3.connect(f"{self.file_path}/demo.db") as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                results = cursor.fetchall()

                # 清空表格并显示查询结果
                self.model.clear()
                if results:
                    columns = [
                        description[0] for description in cursor.description
                    ]  # 获取列名
                    self.append_to_table(columns)  # 添加表头
                    for row in results:
                        self.append_to_table(row)  # 添加数据
        except Exception as e:
            self.append_to_table([f"查询失败：{str(e)}"])

    def delete_database(self):
        """删除数据库文件"""
        db_path = f"{self.file_path}/demo.db"
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
                self.append_to_table(["数据库已删除"])
            except Exception as e:
                self.append_to_table([f"删除数据库失败：{str(e)}"])
        else:
            self.append_to_table(["数据库文件不存在"])

    def append_to_table(self, row_data):
        """将数据添加到表格中"""
        items = [QStandardItem(str(item)) for item in row_data]
        self.model.appendRow(items)

    def cancel_process(self):
        self.is_running = False
        self.append_to_table(["正在停止处理..."])

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.file_name.append(file_path)
            self.file_path = os.path.split(file_path)[0] + "/"
            self.append_to_table([f"输入的文件名为：{file_path}"])
            self.append_to_table([f"输出的文件夹为: {self.file_path}"])

    def clear_table(self):
        """清除 list_echo 中的所有数据"""
        self.model.clear()  # 清除模型中的数据
        self.model.setHorizontalHeaderLabels([])  # 清空表头（可选）

    def select_yufa(self):
        """将语法说明按行输出到表格中"""
        self.clear_table()  # 清空表格

        # 定义语法说明
        syntax_lines = [
            "基本查询 : select * from fenxi",
            "查询某列 : select column_name from fenxi",
            "条件查询 : select * from fenxi where column_name = value    # where 后面更查询条件",
            "逻辑查询 : select * from fenxi where column_name = value and column_name = value  # and 代表与 or 代表或",
            "排序查询 : select * from fenxi order by column_name desc  # desc 代表降序 asc 代表升序",
            "限制查询 : select * from fenxi limit 10   # 限制查询结果的数量",
            "统计查询 : select count(*) from fenxi     # count(*) 代表统计所有行数",
            "合计查询 : select sum(column_name) from fenxi   # sum(column_name) 代表求和",
            "嵌套查询 : select * from fenxi where column_name in (select column_name from fenxi)",
            "模糊查询 : select * from fenxi where column_name like '%value%'",
            "% 代表任意字符 * 代表任意长度 %value% 代表包含 value 的字符串 %value 代表以 value 结尾的字符串 value% 代表以 value 开头的字符串 like 分大小写 LIKE 不分大小写",
            "聚合查询 : select column_name from fenxi group by column_name   # group by 用于对数据进行分组",
        ]

        # 设置表头
        self.model.setHorizontalHeaderLabels(["SQL 语法说明"])

        # 逐行添加到表格中
        for line in syntax_lines:
            self.append_to_table([line])  # 将每一行作为单独的一行数据添加到表格中


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec())
