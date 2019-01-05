# python 日志的配置，python对日志封装成类，日志的调用

import logging


# 使用logging模块：
class CLog:
    # ----------------------------------------------------------------------------
    def __init__(self):
        # 日志文件的存放路径，根据自己的需要去修改
        LOG_FILE_PATH = 'D:\\临时目录\\cic.log'
        self.logger = logging.getLogger()
        fileHandler = logging.FileHandler(LOG_FILE_PATH)
        # 日志的输出格式
        fmt = '\n' + '%(asctime)s - %(filename)s:%(lineno)s  - %(message)s'
        formatter = logging.Formatter(fmt)  # 实例化formatter
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.NOTSET)

    def DebugMessage(self, msg):
        self.logger.debug(msg)
        pass


# 调用日志模块
oCLog = CLog()

a = "aa"
b = "bb"
c = "cc"
d = "dd"
logging.info("code=%s ,status=%s ,seqNo=%s;dddddddddd,ll=%s" % (a, b, c, d))