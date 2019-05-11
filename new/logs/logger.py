
import logging

def get_log(name):
    print(name)
    print(__name__)
    print(type(name))

    logger=logging.getLogger(name)              #收集器
    logger.setLevel("DEBUG")


    # console_handler=logging.StreamHandler() #输出器
    # console_handler.setLevel("DEBUG")
    # console_handler

    #把日志级别 放入配置文件里面变成可配置的
    file_handler=logging.FileHandler("case.log",encoding="utf-8")  # 将收集到的信息放到文件里面
    file_handler.setLevel("DEBUG")                 #INFO级别以上的会输入到文件里面去


    fmt="%(asctime)s-%(name)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d"
    formatter=logging.Formatter(fmt=fmt)        #确定使用格式
    file_handler.setFormatter(formatter)        #拼接

    logger.addHandler(file_handler)       #输出输入拼接

    return logger
