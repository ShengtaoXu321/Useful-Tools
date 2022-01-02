'''
前言
这个是参考公众号的一篇文章 "web目录碰撞" 复现的一个工具，主要想法是弄清楚原理，并用Golang实现一遍。

应用场景
1. 根据网上下载的开源的CMS源代码和网站上的目录结构，进行碰撞比对
2. 好处是能够深度挖掘被.htacess文件保护的残留安装文件和目录等其他内容
3. 相较于 通用型的御剑、dirsearch等工具，针对性更强一点

测试模式
1. 本地CMS环境搭建，然后进行扫描
2. 对比其他工具的扫描效果

原理分析
就是对源码文件中的目录和网站的目录进行一个比对碰撞，然后输出结果

'''


# 包
import sys
import os
import queue
import requests
import threading
import urllib3

# 为了解决 关闭InsecureRequestWarining，其原因是python3中的request模块已经不在包含urllib3。
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():

    # 第一部分
    '''
    代码逻辑
    1. 需要输入目标网址以及本地源码的路径（输入目标url和本地的字典）
    2. 使用os.chdir函数将目录切换到该路径下
    3. 使用os.walk函数去遍历该路径下的所有文件，以队列的方式进行存储
    4. 发现不需要的文件时，自动忽略
    '''

    target=sys.argv[1]        # 创建输入的目标url
    directory=sys.argv[2]     # 创建输入的本地字典地址
    filters=[".jpg",".gif",".png",".css"]

    # 记录当前工作的路径
    now_work=os.getcwd()

    # 切换工作路径
    os.chdir(directory)      # 切换到输入的字典地址的那个目录

    # 创建一个队列，进行存储
    web_paths = queue.Queue()

    for r,d,f in os.walk("."):      # os.walk返回的是三元组（root, dirs,files）
        '''
        关于os.walk()方法：该方法用于在目录树中游走输出在目录中的文件名，向上或向下。===> 可以用于生成文件、目录遍历器[在windows/unix中有效]
        语法格式： os.walk(top,topdown=True,onerror=none,followlonks=False)
        * top 是你所要遍历的目录地址
        * topdown 为真，则优先遍历top目录，否则优先遍历top的子目录（默认为开启）
        * onerror 需要一个callable对象，当walk需要异常时，会调用
        * followlinks 如果为真，则会遍历目录下的快捷方式（linux下是symbolic link）实际所指的目录（默认关闭）
        & root所指的是当前正在遍历的这个文件夹的本身的地址
        & dirs是一个list，内容是该文件夹中所有的目录的名字，不包括子目录
        & files是一个list，内容是该文件夹中所有的文件，不包括子目录
        '''
        for files in f:
            remote_path="{}/{}".format(r.files)   # .format函数："{}/{}"不设定指定位置，按默认顺序格式化输出，格式a/b形式
            if remote_path.startswith("."):       # str.startswith()方法用检查字符串是否以指定子字符串开头；str.startswith(str,beg=0,end=len(str))
                remote_path=remote_path[1:]
            if os.path.splitext(files)[1] not in filters:   # os.path.splitext()方法将函数名和扩展名分开，例如'a.py' 会被分为'a'和'.py'
                web_paths.put(remote_path)      # 存放到新创建的队列中





    # 第二部分
    '''
    代码逻辑
    1. 拼接上述得到的cms所有文件的路径
    2. 使用requests模块去访问，通过网页状态码来判断是否可以访问到
    '''
    result = []
    def test_remote():
        while not web_paths.empty():      # 队列不为空，队列存放的是获取到的文件路径
            path = web_paths.get()        # 从队列一个一个取出数据
            url = "{}{}".format(target,path)

            headers = {     # 这个是http请求的时候，携带的浏览器参数
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
            }

            # 跟网页上的目录碰撞
            try:
                response = requests.get(url,headers=headers)
                if response.status_code==200:
                    print("[{}]=>{}".format(response.status_code,url))
                    result.append(url)  # 将有效的结果存放在list中

                else: # 非200的情况
                    print("[-]{}状态码为：{}".format(url,response.status_code))
            except Exception as error:
                print("[-] {} {}".format(url,"连接失败！"))
                pass

    # 第三部分
    '''
    代码逻辑
    1. 多线程扫描
    2. 将扫描结束后，将结果写入到result.txt文件中
    '''
    threads = 10 # 定义线程数
    for i in range(threads):
        t = threading.Thread(target=test_remote())  # 开启线程
        t.start()     # 开始开启线程

    while True:
        if threading.activeCount()==1:
            os.chdir(now_work)
            with open('result.txt','w')as f:
                for i in result:
                    f.write(i+'\n')
            f.close()
            break




if __name__ == '__main__':
    main()

