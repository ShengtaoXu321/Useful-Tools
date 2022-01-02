# 这是参考"霜刃安全"公众号复制的代码
# 目的是学习原理，使用golang进行重构

# Name: fake-netcat
# Author: 昊辰
# Address：https://github.com/haochen1204/python_hacktool_study

# 原理解释
'''
netcat作用是通过tcp或者udp进行连接去读取数据，===> 后门工具、网络调试、探测工具
netcat功能很强大，一般来说，最常用的就是nc的shell功能，这里将python写一个简单的netcat的shell功能

原理：
1. 就是在服务端开启了一个tcp服务器，在攻击机上开启一个tcp客户端
2. 攻击机进行正向连接/反向连接，发送数据，进行对应操作
3. 正向连接：客户端去连服务端（攻击机作为客户端主动去连接受害机）
4. 反向连接：服务器请求客户端的端口（受害机被动连向攻击机）
'''

# 导包
import sys
import getopt


# 帮助函数
def help():
    print(f'''
    使用模板如下：
    python3 main.py -t target_host -p port
    -l --listen   开启监听
    eg:
    python3 main.py -t 192.168.1.1 -p 4444 -l
    python3 main.py -t 192.168.1.1 -p 
    other:
    开启shell后可通过该
    upload_file=abc.txt 来上传文件
    ''')
    sys.exit(0)


def main():
    # 定义全局变量
    global listen
    global port
    global target


    # 获取用户输入的参数
    # 1. 判断输入是否为空
    if not len(sys.argv[1:]):
        help()     # 跳转到帮助界面

    # 2. 获取用户输入的参数
    try:
        opts,args=getopt.getopt(sys.argv[1:], "hlt:p", ["help", "listen", "target", ])       # getopt.opt(args, shortopts, longopts=[]) args：用户输入的参数列表，shortopts：短操作参数
