# encoding:utf-8
# Motto：good good study, day day up. why you so lazy ？？？

import os
from datetime import datetime

# 项目根目录
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# ******************* 一级目录 *******************************

# 结果目录
RESULT_PATH = os.path.join(ROOT_PATH, "Results")

# 工具文件主目录
UTILS_PATH = os.path.join(ROOT_PATH, "utils")

# 测试用例目录
case_dir = os.path.join(ROOT_PATH, "TestCase")

# ******************* 二级目录 *******************************
# 日志目录
LOG_DIR_PATH = os.path.join(RESULT_PATH, "log")

driverDir = os.path.join(UTILS_PATH, "Bsdriver")
Chrome_Win_path = os.path.join(driverDir, 'chromedriver.exe')
Chrome_Mac_path = os.path.join(driverDir, 'chromedriver')

web_driver_path = Chrome_Win_path if os.name == 'nt' else Chrome_Mac_path

# 测试数据所在目录
# 当前时间
currentTime = datetime.now().strftime('%Y%m%d/%H%M%S')
YmdTime = datetime.now().strftime('%Y_%m_%d')

# from utils.handle_config import HandleConfig
#
# private_info_c = HandleConfig(os.path.join(configDir, 'config.conf'))
base_url = "http://www.testclass.net/readers/sign_in"

# private_user_info = private_info_c('admin')

# # 测试数据的常量
Retry_count = 10
#
# # 邮件配置信息
# # 邮件服务器
# smtpServer = 'smtp.qq.com'
# # 发送者
# fromUser = '账号@qq.com'
# # 发送者密码
# fromPassWord = 'mhxvqpewblldbjhf'
# # 接收者
# toUser = ['账号@qq.com']  # 可以同时发送给多人，追加到列表中
# # 邮件标题
# subject = 'xx项目自动化测试报告'
# # 邮件正文
# contents = '测试报告正文'
# # 报告名称
# htmlName = r'{}\testReport{}.html'.format(reportDir, currentTime)
if __name__ == '__main__':
    print(ROOT_PATH.split(r'/')[-1])
