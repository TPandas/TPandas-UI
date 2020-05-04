"""
-*-conding:utf-8
@Time:2019-05-21 7:02
@auther:grassroadsZ
@file:handle_log.py
"""
import logging
import os

from concurrent_log_handler import ConcurrentRotatingFileHandler

from settings import LOG_DIR_PATH, YmdTime


class MyLog(object):
    """
    我的日志类
    """

    def __init__(self):
        # 定义名为case的日志收集器对象
        self.logger = logging.getLogger(self.__class__.__name__)
        # 定义日志收集器等级
        self.logger.setLevel("INFO")
        # 加个判断避免一条用例写两次
        if not self.logger.handlers:
            # 定义输出到终端
            console_handle = logging.StreamHandler()
            file_handle = ConcurrentRotatingFileHandler(
                filename=os.path.join(
                    LOG_DIR_PATH, YmdTime + "_log.txt"), mode="a", maxBytes=102400 * 102400, backupCount=3,
                encoding="utf-8")
            # 定义日志输出出道等级
            console_handle.setLevel("INFO")

            file_handle.setLevel("INFO")

            # 定义日志显示格式
            console_format = logging.Formatter(
                "%(asctime)s - [%(levelname)s] -%(module)s -[line:%(lineno)d] - [日志信息]: %(message)s")
            file_format = logging.Formatter(
                "%(asctime)s - [%(levelname)s] -%(module)s -[line:%(lineno)d] - [日志信息]: %(message)s")

            console_handle.setFormatter(console_format)
            file_handle.setFormatter(file_format)
            self.logger.addHandler(console_handle)
            self.logger.addHandler(file_handle)

    def out(self):
        return self.logger


# do_log = MyLog().out()


if __name__ == '__main__':
    do_log = MyLog().out()
    do_log.info("msg")
    do_log.debug("debug")
    do_log.warning("warn")
    do_log.error("error")
