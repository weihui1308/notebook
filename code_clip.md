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
# 如果有可用 GPU 则会返回 True
dtype = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
# content_img = image_loader("images/dancing.jpg").type(dtype)
# dtype对应不同数据类型
````
### 3. 