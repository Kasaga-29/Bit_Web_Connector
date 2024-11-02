# 北京理工大学校园网断网检测&自动重连工具

## 简介
本工具使用 python 实现，可检测校园网是否断连，断连时使用 selenium 库模拟访问 10.0.0.55 进行登录。  

可选择使用 pyinstaller 库将 py 文件封装为**可执行文件**运行。  

有学长/学姐之前做过功能类似但支持更多平台的脚本：https://github.com/coffeehat/BIT-srun-login-script  

本项目仅为了方便大家在 Windows 系统下可以直接执行 exe 文件  

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
   
   **username**: 用户名
   
   **password**: 密码
   
   **interval**: 检测网络连接状态的间隔时间（单位：秒）
   
   **edge_driver_path**: Edge 浏览器的 WebDriver 路径，已放置在 `edge_driver` 目录下
   
   **log_file_path**: 日志地址路径，若不需要可将其设为 None

   以上两路径请使用**绝对路径**表示，否则在执行 exe 文件时可能出现路径错误
   
   另有其余参数可参考 login.py 文件进行设置
   
4. **运行脚本**：
   
   - 打开命令行工具，导航到代码所在的目录
     
   - 执行以下命令运行脚本：
     
     python run.py
     
5. **打包为 EXE 文件**（可选）：  
   
   - 导航到代码所在的目录后，在命令行中执行以下命令：
      
     pyinstaller --onefile run.py
     
   - 打包完成后，run.exe 文件会生成在 `dist` 目录下
      
   - 双击 run.exe 文件即可运行  

## 注意事项  

- 确保项目路径中不包含任何中文、空格、非法字符……
  
- 确保在运行程序之前，已经正确配置了 run.py 的参数。
  
- 本工具请勿用于非法活动。
