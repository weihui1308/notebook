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