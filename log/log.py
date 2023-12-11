import logging

#创建日志器
logger = logging.getLogger()
#设置日志器的级别
logger.setLevel(logging.INFO)
#设置处理器的格式
format = logging.Formatter("%(asctime)s  %(filename)s[line:%(lineno)d]%(levelname)s %(message)s")

#创建处理器
f = logging.FileHandler(r'D:/Study/pycharm_code/selenuim/day03/log/log.txt', mode='a',encoding='utf-8')
#设置处理器的级别
f.setLevel(logging.INFO)
#设置处理器的格式
f.setFormatter(format)
#将处理器添加至日志器
logger.addHandler(f)