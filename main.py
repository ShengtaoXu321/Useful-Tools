import requests, re, urllib3
# from logging_config import log_setup  # 不优雅的方式
from log_manager import LogManage# 优雅的方式
from moviepy.editor import VideoFileClip


# 关闭ssl告警信息
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

# 配置日志
# -- 不优雅的方式
# logger=log_setup()

# -- 优雅的方式
log_manager = LogManage("log_record")  # 实例化一个对象
logger = log_manager.logger



def get_url(url):
    req=requests.get(url)
    try:
        # 1. 先检查响应码状态，如果状态不如200，则抛出异常
        req.raise_for_status()

        # 2. 获取响应数据
        msg = req.content.decode('utf-8')
        print(msg)

        # 提取视频链接，切片的方式
        # start_index = msg.find(b"视频：") + len(b"视频：")
        # end_index = msg.find(b".mp4", start_index) + len(b".mp4")
        # video_url = msg[start_index:end_index]
        # # print(start_index,end_index,video_url)
        # return video_url

        # 提取视频链接，正则的方式
        pattern = r"视频：(.*?)\.mp4"
        # pattern = rb"\u89c6\u9891\uff1a(.*?)\.mp4"
        match = re.search(pattern, msg)
        # 如果match为真，则代表匹配成功，否则就匹配失败
        if match:
            video_url_raw = match.group(0)  # 全部匹配出来
            video_url = match.group(1) + ".mp4" # 匹配括号里面的内容 (.*?)
            return video_url
        else:
            logger.info("匹配失败了哇！")
    except requests.exceptions.HTTPError as e:
        logger.info("API 请求失败...%s",str(e))
        # logger.error("API 请求失败...%s",str(e))  # 也可以用这个
    except Exception as e:
        logger.info("发生异常...%s",str(e))
        # logger.error("API 请求失败...%s",str(e))  # 也可以用这个



def pot_play(url):
    req = requests.get(url)
    try:
        # 1. 先检查响应码状态，如果状态不如200，则抛出异常
        req.raise_for_status()

        # 2. 获取响应数据
        msg = req.content
        # 使用moviepy打开视频内容
        video_clip=VideoFileClip(msg)
        # 播放视频
        video_clip.ipython_display(width=400)

        video_clip.reader.close()
    except Exception as e:
        logger.info(e)













# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "http://api.xcyun.top/api/jiepai.php"
    f=get_url(url)
    print(f)
    pot_play(f)
    log_manager.log_close()




