from torchvision import transforms
from PIL import Image, ImageDraw
import os


base = 'C:\\Users\\wh\\Desktop\\tmp\\9styles'
num = 0

tf1 = transforms.Resize(300)
tf2 = transforms.CenterCrop(300)
for root, ds, fs in os.walk(base):
    for name in fs:
        img_path = root + '/' + name
        #img = Image.open(img_path).convert('RGB')
        img = Image.open(img_path).convert('L')

        img_resize = tf1(img)
        img_crop = tf2(img_resize)
        s = '%04d' % num
        num += 1
        img_crop.save('style_gray/'+s+'.png')