from kornia.losses.ssim import SSIMLoss
import torchvision.transforms as T
from PIL import Image
import kornia.metrics as metrics
import numpy as np
import math


def calculate_psnr(img1, img2, border=0):
    # img1 and img2 have range [0, 255]
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    h, w = img1.shape[:2]
    img1 = img1[border:h-border, border:w-border]
    img2 = img2[border:h-border, border:w-border]

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')
    return 20 * math.log10(255.0 / math.sqrt(mse))


def image_loader(image_name, size):
    loader = T.Compose([
        T.Resize(size),  # scale imported image
        T.CenterCrop(size),
        T.ToTensor(),
        # T.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
        #T.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])  # transform it into a torch tensor

    image = Image.open(image_name).convert('RGB')
    # fake batch dimension required to fit network's input dimensions
    image = loader(image).unsqueeze(0)
    return image

criterion = SSIMLoss(5)

img_path1 = 'img_ori/1.jpg'
img_path2 = 'img_tar/weight=20.jpg'

img1 = image_loader(img_path1, 256)
img2 = image_loader(img_path2, 256)
ssim = 1 - criterion(img1, img2)
#psnr = calculate_psnr((img1*255).numpy(), (img2*255).numpy())
psnr = metrics.psnr(img1, img2, 1.)
print(ssim)
print(psnr)