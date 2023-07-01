import logging


# 创建log类
class LogManage:
    def __init__(self, name):
        """
        初始化程序，构造方法，调用该方法的时候会被执行
        :param name: init
        """
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.log_setup()

    def log_setup(self):
        """
        日志配置和处理程序设置方法
        :return:
        """
        # 创建处理程序和格式化程序
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")

        # 将格式化程序添加到处理程序
        console_handler.setFormatter(formatter)

        # 将处理程序添加到日志记录器中
        self.logger.addHandler(console_handler)

    def log_close(self):
        """
        关闭方法，优雅的关闭每一个处理程序的
        :return:
        """
        # 创建一个handlers列表副本，涵盖每个处理程序
        handlers = self.logger.handlers[:]  # self.logger.handler[:]返回当前日志记录器对象关联的处理程序列表
        for handler in handlers:  # 遍历该列表
            handler.close()  # 关闭该程序
            self.logger.removeHandler(handler)  # 并移除该处理程序,确保日志记录器对象不再向这些处理程序发送日志消息。
        logging.shutdown()  # 关闭日志系统
