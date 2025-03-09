# SQM 数据分析工具

基于Python + PySide6开发的本地数据分析工具，提供数据库操作、上线关系查询及可视化功能。

## 主要功能

- 📂 拖拽文件导入数据（支持txt格式，默认分隔符`----`）
- 🛠️ 自动创建/清理SQLite数据库
- 🔍 执行自定义SQL查询（内置查询语法帮助）
- 👥 单人上线关系查询（需指定ID、姓名、上线列）
- 🌳 生成HTML格式树状关系图
- 📊 表格数据展示与交互

## 运行环境

- Python 3.11+
- 依赖库：
  ```bash
  pip install PySide6 pandas

## 安装使用

### 克隆仓库：

bash
git clone https://github.com/SQM-fuleiya/SQM-Data-analysis-tools.git

### 安装依赖：

bash
pip install -r requirements.txt

### 运行主程序：

bash
python main.py

## 项目结构

plainText
.
├── main.py              # 主程序入口
├── main_ui.py           # Qt界面定义
├── db_fun.py            # 数据库操作模块
├── file_fun.py          # 文件处理模块
├── build/               # 构建目录
└── dist/main.exe        # 打包生成的可执行文件

## 使用说明

### 文件导入：

直接拖拽txt文件到窗口

### 文件格式要求：

plainText
姓名----id----上线姓名----上线id

xlsx

## 功能按钮：

🏁 开始导入数据：初始化数据库
🧹 清空表格：重置显示区域
📑 查询语法：查看SQL示例
👤 查询上线：单用户关系查询
🌿 生成树状图：生成关系图html文件

## 注意事项：

首次使用会自动创建数据库
关闭程序时会自动清理临时数据库
树状图生成依赖查询结果，需先执行查询操作

## 版本历史
v1.0
初始版本
文件导入功能
数据库操作功能
查询功能

v1.5 (2025-03-09)
新增上线关系查询功能
实现HTML树状图生成
优化数据库自动清理机制

## 许可证

MIT License

Copyright (c) 2025 SQM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
