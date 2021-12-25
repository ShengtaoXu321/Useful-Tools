# 查询本机ip信息脚本

## 说明
- Version: 1.0
- Tail:
   1. 完成本地IP相关信息的获取
    2. 完成获取到的信息文件保存
    3. 未完成跨平台使用
    4. 代码可以优化
  
- 有关打包：pyinstall
  1. 安装：```pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip```
  2. 打包：```pyinstaller -F -w -i net.ico main.py```