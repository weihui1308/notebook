### 1. 新建文件夹
````python
try:
    os.makedirs("/home/wh1")
except OSError:
    pass
try:
    os.makedirs("/home/wh2")
except OSError:
    pass

# 当文件夹存在会报错，所以采用try...except...语句
````
### 2. 确认cuda是否可用
````python
use_cuda = torch.cuda.is_available()
# 如果有可用 GPU 则会返回 True,否则返回False
dtype = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
# content_img = image_loader("images/dancing.jpg").type(dtype)
# dtype对应不同数据类型
````
### 3. 日志输出
````python
import logging
def logger_config(log_path,logging_name):
    FORMAT = '[%(levelname)s: %(filename)s: %(lineno)4d]: %(message)s'
    logger = logging.getLogger(logging_name)
    logger.setLevel(level=logging.DEBUG)
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(console)
    return logger

time_stamp = time.strftime("%Y%m%d_%H:%M:%S", time.localtime()) 
logger = logger_config(log_path=args.outLog + '/log'+ time_stamp +'.txt', logging_name='--->')
logger.info("Train Success: {:.3f}".format(success / total))