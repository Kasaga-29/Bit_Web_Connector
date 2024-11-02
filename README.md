# 北京理工大学校园网断网检测&自动重连工具

## 简介
本工具使用python实现，可检测校园网是否断连，断连时使用selenium库模拟访问10.0.0.55进行登录。
可选择使用pyinstaller库将py文件封装为可执行文件运行。

## 支持系统
- Windows

## 环境配置
1. **安装 Python**：
   确保你的系统中已安装 Python。
2. **安装 Selenium 库**：
   pip install selenium
3. **安装 PyInstaller 库**：
   pip install pyinstaller

## 使用方法
1. **下载代码**：
   将本项目的代码下载到本地。
2. **配置登录参数**：
   username: 用户名
   password: 密码
   interval: 检测网络连接状态的间隔时间
   edge_driver_path: Edge浏览器的WebDriver路径，已放置在 `edge_driver` 目录下
   log_file_path: 日志地址路径，若不需要可将其设为 None
   另有其余参数可参考login.py文件进行设置
3. **运行脚本**：
   - 打开命令行工具，导航到代码所在的目录
   - 执行以下命令运行脚本：
     python run.py
4. **打包为 EXE 文件**（可选）：
   - 导航到代码所在的目录后，在命令行中执行以下命令：
     pyinstaller --onefile run.py
   - 打包完成后，run.exe 文件会生成在 `dist` 目录下
   - 双击 run.exe 文件即可运行

## 注意事项
- 确保在运行程序之前，已经正确配置了 run.py 的参数。
- 本工具请勿用于非法活动。
