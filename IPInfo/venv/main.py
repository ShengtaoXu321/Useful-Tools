'''
Title: 获取IP的一个工具
Auth: Zoomer
Ver: 1.0
Info: 无可视化
'''

import requests
import re
import json
import time

# 全局变量
access_key = "?access_key=630791e8c795fe3d04a8a16e92bfdf36"
url = "http://api.ipapi.com/"
file1 = "./out.log"  # 成功日志
file2 = "./error.log"  # 错误日志
locatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 访问ip api获取数据
def askIpApi():
    realUrl = url + ip + access_key
    # print(realUrl)
    res = requests.request('GET', realUrl)  # python的单引号双引号无区别
    if res.status_code == 200:
        resCont = res.content.decode('utf-8')
        dictRes = json.loads(resCont)
        # print(dictRes)
        # 解析数据
        type = dictRes["type"]
        continent_name = dictRes["continent_name"]
        country_name = dictRes["country_name"]
        region_name = dictRes["region_name"]
        latitude = dictRes["latitude"]
        longitude = dictRes["longitude"]
        # print(longitude)
        flag = dictRes["location"]["country_flag_emoji"]
        info = flag + " " + "ip:" + ip + "; " + "类型:" + type + "; " + "所属大洲：" + continent_name + "; " + "国家：" \
               + country_name + "; " + "地区：" + region_name + "; " +"查询时间为："+locatime

        # print(info)
        return info



# 文件操作封装
def fOutFile(file, data):
    with open(file, "a") as f:
        f.write(data + '\n')


# 验证输入IP的合法性
def checkIp(ip):
    compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.'
                            '(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.'
                            '(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.'
                            '(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')  # 正则匹配
    if compile_ip.match(ip):
        return True
    else:
        return False


# 获取IP信息
def getIpInfo():
    global ip
    ip = (input("请输入需要输入的IP："))
    while True:
        if checkIp(ip):
            try:
                info=askIpApi()
                try:
                    fOutFile(file1, info,1)
                    print("写入文件成功！")
                    getIpInfo()
                except Exception as error1:
                    # print("写入文件失败！", error1)
                    errorInf1="❎ " + "现在的时间是" + locatime + "写入文件失败！" + " "+ str(error1)
                    fOutFile(file2, errorInf1)
                    break
            except Exception as error2:
                print("获取IP信息错误！", error2)
                errorInf2="❎ " + "现在的时间是: "+locatime+" 出现错误是：写入文件失败！"+" "+str(error2)
                fOutFile(file2, errorInf2)
                break
        elif ip == "exit":
            print("感谢使用本工具！")
            break

        else:
            print("请输入正确的IP格式！")
            getIpInfo()


if __name__ == '__main__':
    getIpInfo()
