import pandas as pd
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QMessageBox

import db_fun

file_name = []
file_path = ""
单人层级 = []
列数据 = []


def append_to_table(self, row_data):  # 将数据添加到表格中
    items = [QStandardItem(str(item)) for item in row_data]
    self.model.appendRow(items)
    # self.list_echo.resizeColumnsToContents()  # 自动调整列宽
    self.list_echo.setWordWrap(True)  # 启用文本换行


def clear_table(self):  # 清空表格
    self.model.clear()
    self.model.setHorizontalHeaderLabels([])


def start_db(self):  # 文件数据入库
    clear_table(self)  # 清空表格
    # 启用按键
    self.ui.db_select_but.setEnabled(True)
    self.ui.db_clear.setEnabled(True)
    self.ui.select_one.setEnabled(True)
    self.ui.show_guanxi.setEnabled(True)

    if not file_name:  # 检查文件是否存在
        QMessageBox.warning(self, "警告", "请先选择文件！")
        return
    self.is_running = True  # 初始化标志位
    append_to_table(self, ["开始导入数据..."])

    for file_idx, file_path in enumerate(file_name, 1):  # 确认存在文件
        if not self.is_running:
            break

        try:  # 判断文件类型
            if file_path.endswith(".txt"):
                处理txt文件(self, file_path)
            elif file_path.endswith((".xlsx", ".xls")):
                处理表格文件(self, file_path)
        except Exception as e:  # 处理异常
            append_to_table(self, [f"处理文件{file_path}时出错：{str(e)}"])
            continue

    append_to_table(self, ["导入完成！" if self.is_running else "导入已取消"])


def 处理txt文件(self, file_path):  # 处理txt文件
    batch_size = 1000  # 建立缓存池
    batch_data = []

    with open(file_path, "r", encoding="utf-8") as f:
        f.seek(0)

        for line_idx, line in enumerate(f, 1):
            if not self.is_running:
                break

            data = line.strip().split("----")  # 分割数据，分隔符为 ----
            batch_data.append(data)

            if len(batch_data) >= batch_size:
                db_fun.批量入库(self, batch_data)
                batch_data = []

        if batch_data and self.is_running:
            db_fun.批量入库(self, batch_data)


def 处理表格文件(self, file_path):
    try:
        df = pd.read_excel(file_path)
        db_fun.批量入库(self, df.values.tolist())
    except Exception as e:
        raise Exception(f"读取Excel文件失败：{str(e)}")


def cancel_process(self):
    self.is_running = False
    append_to_table(self, ["正在停止处理..."])
