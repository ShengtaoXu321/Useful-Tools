import logging

"""
其实这种函数调用的方式也蛮好的，
logger=logsetup()，能给满足需求了
但是你发现了没有，我想优雅的关闭的时候，我还要创建一个
logger_close=logclose(),
我想要优雅的，结果你丫的给我越整越复杂了，
这时候，我们就需要引入类的概念
class logMan:
使用类的好处就多啦，封装、继承、多态，好多好多
让我们开始吧...

"""


# 配置logging
def log_setup():
    # 创建logger对象
    logger=logging.getLogger("log_info")
    logger.setLevel(level=logging.INFO)  # 设定INFO模式

    # 创建控制台处理程序  （可不做要求）
    console_handler=logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 创建日志消息格式化程序
    formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")

    # 设置处理程序的格式化程序
    console_handler.setFormatter(formatter) # 控制台输出的样式

    # 将处理程序添加到logger对象
    logger.addHandler(console_handler)

    return logger

def log_close():
    logging.shutdown()
