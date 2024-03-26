## privious works提到过的一些通用方法
1. Robust Physical-World Attacks on Deep Learning Visual Classification(CVPR 2018)  
    这篇文章中提出了一种two-stage的评估方法：  
    + Stationary (Lab) Tests：这种方法评估静止时，相机位置固定时对image的分类；
    + Drive-By (Field) Tests：相机是移动的，模拟自动驾驶的场景，因此相机对同一个物体，会捕获很多张image，这种方式评估动态场景下的分类。
2. Synthesizing Robust Adversarial Examples(ICLR 2018)  
    这篇文章提出EOT方法，用来考虑从digital setting到physical setting转变时的因素，如失真、形变、光照等。被很多文章follow。
