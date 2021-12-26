# 这是一个获取本地ip信息的一个脚本

import urllib.request
import requests
import json
import time

# 使用urllib库
def getIp_Urllib():
    # 访问api,获取请求，然后解析内容
    response = urllib.request.urlopen("http://ip-api.com/json/?lang=zh-CN")
    resCoder=response.read().decode('utf-8')     # bytes ---> str
    dict1=json.loads(resCoder)
    # print(dict1)
    # 新建一个字典，将数据本地存入
    useDict=dict()
    for v in dict1:
        if v not in useDict:
            useDict.update(dict1)  # 字典的追加方式

    print(useDict)

# 使用request库
def getIp_Request():
    res=requests.request('GET','http://ip-api.com/json/?lang=zh-CN')
    if res.status_code == 200:
        resCode=res.content.decode('utf-8')      # bytes ---> str
        dict2=json.loads(resCode)                 # str ----> json（字典）
        # print(dict2)

        # 解析数据
        ip=dict2['query']
        regionName=dict2['regionName']
        country=dict2['country']
        city=dict2['city']
        isp=dict2['isp']
        asn=dict2['as']
        # jindu=dict2['lat']
        # weidu=dict2['lon']

        location=city + ',' + regionName + ',' + country
        locatime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

        # 将文件本地输出记录
        with open('./out.txt',"a") as f1:
            print(f'当前时间为：{locatime}-----您所查询的ip是：{ip}-----------地点是：{location}-----------该ISP：{isp}--------该ASN：{asn}', file=f1)
    else:
        print("获取本地ip信息失败！")
    f1.close()

if __name__ == '__main__':
    # 异常处理
    try:
        # getIp_Urllib()
        getIp_Request()
    except Exception as error:
        print(error)
