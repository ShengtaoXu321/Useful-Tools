# 参考网上的自动清理的程序
import time
import os

# 定义用户的临时文件目录，获取当前时间，并计算出默认时间对比
path='C:\\Users\\Administrator\\AppData\\Local\\Temp'
# print(f"请输入地址：")
# path=str(input())
timeNow=time.time()
old_threshold=timeNow-30*24*60*60   # 当前时间往前推30天，作为时间对比的默认参数值r

# print(f'时间的默认参数值为：{old_threshold}')

# 获取文件，进行比对
files=os.listdir(path)
# print(files)
for files_name in files:
    files_path_name=os.path.join(path,files_name)     # 字符串拼接，加上path路径
    print(files_path_name)
    if not os.path.isdir(files_path_name):  # 判断不是目录
        # print(files_name)
        access_time=os.stat(files_path_name).st_mtime     # 获取文件的最后一次修改时间
        # print(access_time)
        if access_time < old_threshold:
            os.remove(files_path_name)
            print(f'文件{files_name}已经被删除！')

