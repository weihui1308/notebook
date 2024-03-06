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
````
### 4. pytorch框架做图像识别
````python
import torch
import torchvision.models as models
from PIL import Image
from torchvision import transforms
import torchvision.utils as vutils


def print_prob(output):
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    print("The top5 is following:")
    for i in range(top5_prob.size(0)):
        print("\t", categories[top5_catid[i]], top5_prob[i].item())
    return probabilities


filename = "image/dog.jpg"
input_image = Image.open(filename)
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
preprocess = transforms.Compose([
    transforms.Resize(224),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std),
])

input_tensor = preprocess(input_image)
vutils.save_image(input_tensor.data, "1.png", normalize=True)
input_batch = input_tensor.unsqueeze(0)
classifier = models.vgg19(pretrained=True)
classifier.eval()
with torch.no_grad():
    output = classifier(input_batch)
print_prob(output)
print(output.data.max(1)[1][0])
````
### 5. 反归一化
````python
class UnNormalize(object):
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, tensor):
        """
        Args:
            tensor (Tensor): Tensor image of size (C, H, W) to be normalized.
        Returns:
            Tensor: Normalized image.
        """
        for t, m, s in zip(tensor, self.mean, self.std):
            t.mul_(s).add_(m)
            # The normalize code -> t.sub_(m).div_(s)
        return tensor
````
### 6. 寻找二维tensor中topk个值的位置
````python
import torch

k = 3
a = torch.tensor([[1, 8, 3, 4, 6], [1, 10, 3, 7, 6]])
b = torch.topk(a.view(-1), k)
index_max = b.indices
loc_max = []

for idx in range(2):
    x = (index_max[idx] / 5).int().item()
    y = (index_max[idx] % 5).item()
    loc_max.append([x, y])

print(loc_max)
````

### 7. 查看当前cuda和cudnn版本
````
cuda:
cat  /usr/local/cuda/version.txt
或
nvcc --version

cudnn:
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
````

### 8. 测试配置的环境cuda和cudnn是否可用
````python
import torch
print(2.0)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# Assume that we are on a CUDA machine, then this should print a CUDA device:
print(device)

x = torch.Tensor([2.1])
xx = x.cuda()
print(xx)

# CUDNN TEST
from torch.backends import cudnn

print('cudnn is ' + str(cudnn.is_acceptable(xx)))

````
