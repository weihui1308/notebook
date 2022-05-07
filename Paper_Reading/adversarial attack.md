# 1: 20220502
### Title: Context-Aware Transfer Attacks for Object Detection
### Venue: AAAI 2022
目标检测模型是context-aware的，首次启发，作者提出context-aware attack，利用的context信息有cooccurrence of objects, relative locations, size。通过添加helper objects，实现了对目标检测模型的可迁移攻击。
# 2: 20220502
### Title: Adversarial Patch
### Venue: NIPS 2017
本文提出了一种方法来创建真实世界中通用的、鲁棒的、目标对抗图像补丁。补丁是通用的原因在于它们可以被用于攻击任何场景；鲁棒是因为它们在各种各样的变换下仍有效果；目标是因为它们可以误导某个分类器输出任意特定目标类别（targeted attach）。这些对抗补丁可打印，并添加到任意场景、拍照并提供给图像分类器；甚至当补丁很小时，他们也能误导分类器忽略场景中的其他项（目标）并输出一个目标类别。
# 3: 20220503
### Title: Fooling automated surveillance cameras: adversarial patches to attack person detection
### Venue: CVPRW 2019
用Adversarial Patch攻击detector(YOLOv2)，实现physical attack。
# 4: 20220504
### Title: Fooling thermal infrared pedestrian detectors in real world using small bulbs
### Venue: AAAI 2021
将Adversarial Patch攻击应用在热红目标检测任务中，用发光的小灯泡制作patch，实现了physical attack。
# 5: 20220504
### Title: Adversarial T-shirt! Evading Person Detectors in A Physical World
### Venue: ECCV 2020
制作Adversarial T-shirt攻击person detector。（todo）
# 6: 20220505
### Title: Legitimate Adversarial Patches: Evading Human Eyes and Detection Models in the Physical World
### Venue: ACM MM 2021
本文采用Adversarial Patch攻击person detector（YOLOv2），同时致力于生成能够躲过人类注意的patch，提出了patch的合理度，并用几个指标约束和衡量。
# 7: 20220506
### Title: DPATCH: An Adversarial Patch Attack on Object Detectors
### Venue: workshop of safeAI@AAAI 2019
本文提出DPATCH，一种被迭代地训练的对抗patch，可以攻击主流的目标检测器。猜测DPATCH中的D代表detection。本文的motivation是发现现有的adversarial patch不能欺骗检测器例如Faster RCNN。提出了对检测框回归和目标分类同时进行攻击的思路。本文攻击了YOLO和Faster RCNN。文章没有考虑patch的视觉可接受度。
# 8: 20220507
### Title: Robust Physical-World Attacks on Deep Learning Visual Classification
### Venue: CVPR 2018
本文认为生成鲁棒的物理攻击扰动，主要的挑战是环境的变化，并提出Robust Physical Perturbations(PR2)，可以生成在相机视角改变距离和角度的扰动。这篇文章中提出了一种two-stage的评估方法：①Stationary(Lab) Tests：这种方法评估静止时，相机位置固定时对image的分类；②Drive-By(Field) Tests：相机是移动的，模拟自动驾驶的场景，因此相机对同一个物体，会捕获很多张image，这种方式评估动态场景下的分类。
# 9: 20220507
### Title: Perceptual-Sensitive GAN for Generating Adversarial Patches
### Venue: AAAI 2019
论文提出了一个叫PS-GAN的网络，输入是原始图像Image和Seed Patch，输出为一个Adversarial Patch。具体地，用GAN的建模能力保证Image+Seed Patch的visual fidelity，而且在模型框架在加入attention 模块，将Patch贴在注意力高的位置，以此来提高模型的攻击性。
# 10: 20220509
### Title: The Translucent Patch: A Physical and Universal Attack on Object Detectors
### Venue: CVPR 2021
文章提出现有的攻击方法有一个主要的限制：需要有接触到object的机会，这样才能把扰动添加上去。而且如果攻击多个object的话，需要把扰动添加的每个object上，这样无疑降低了practicality。因此本文提出一种camera-based物理攻击，将patch添加在相机的镜片上。
# 11: 20220509
### Title: Adversarial Laser Beam: Effective Physical-World Attack to DNN in a Blink
### Venue: CVPR 2021
对抗攻击现有问题：
1.目前大多数研究是针对digital setting，然而在物理世界场景中，通常image被相机捕获然后被提供给model，攻击者无法直接干扰输入的image；
2.在物理世界的对抗样本，通常需要很大的扰动，不然无法被相机捕获到；
3.对抗样本中小扰动的攻击性很容易在物理世界复杂的场景中被减弱；
4.物理世界的对抗样本需要高隐蔽性，避免被防御者发现。
本文提出采用激光束进行攻击，Adversarial Laser Beam(AdvLB)，主要用于光线较暗的环境中。由于是激光束，所以速度非常快，使攻击的可操作性变得非常高。这是对抗攻击的一种新的类型
# 12: 20220510
### Title: Invisible Perturbations: Physical Adversarial Example Exploiting the Rolling Shutter Effect
### Venue: CVPR 2021
当前物理攻击的方法存在问题：都有一个假设——扰动一定时可见的，确保可以被相机感受到。本文提出一种对于人眼是不可见的扰动，利用相机中的辐射测量卷帘效应来创建出现在图像上的精确条纹图案，以此来达到攻击的目的。对于人眼来说，它看起来像是对象被照亮了，但相机创建了一个带有条纹的图像。本文在Related work部分提出一个观点：digital adversarial example，即攻击网络物体系统，是不现实的，因为攻击者如果有能力控制图像的像素，说明他已经有特权，并且可以直接采用更简单有效的攻击方式，而不是修改image的像素。
# 13: 20220510
### Title: Bias-based Universal Adversarial Patch Attack for Automatic Check-out
### Venue: ECCV 2020
本文的提出一种two-stage对抗patch生成算法，目的是生成class-agnostic的universal对抗patch。攻击场景为自动结账平台。在stage one，首先融合许多hard example（指模型识别错误的图片），然后利用attention找到权重较大的区域，得到输出。在stage two，生成类prototype，然后将上一stage的输入贴到prototype上作为adversarial example，用它们攻击目标模型。本文利用model的认知偏置来得到对抗patch的texture，类似于决策边界。然后利用model的语义偏置来缓解训练时对数据量的依赖。
# 14: 20220511
### Title: PhysGAN:Generating Physical-World-Resilient Adversarial Examples for Autonomous Driving
### Venue: CVPR 2020
概述：该篇文章应用场景是自动驾驶，提出了目前物理攻击面临的问题：1.大多数方法生成的是digital对抗样本，无法应用到物理世界中，因为这些方法添加的扰动覆盖整张Image，而真实的物理应用场景中并不能给一些视觉区域添加扰动，比如天空；
2.当前物理攻击算法聚焦于静态的物理世界场景，而真实应用场景是动态的；
3.生成的对抗样本视觉上是不真实的；
4.大多数方法聚焦于分类模型，而自动驾驶是转向模型（steering model），属于回归模型。
针对上述问题，本文才有GAN框架生成对抗样本，输入为3D tensor，第3维是时间，用这种方法考虑场景的动态变化，生成可以持续误导steering model的对抗样本。
# 15: 20220511
### Title: Adversarial Camouflage：Hiding Physical-World Attacks with Natural Styles
### Venue: CVPR 2020
本文提出现有的攻击方法不能既满足攻击扰动的大小，又满足视觉的不可感知行。而且对抗扰动生成的过程是不受控制的，缺乏灵活性。因此本文提出用自然中存在的一些styles去生成对抗样本，同时在算法框架中考虑了从digital setting转化为physical-world setting的一些因素，例如视角变化、相机噪声等。采用了style loss、content loss、smooth loss和adversarial loss。
# 16: 20220511
### Title: Feature Space Targeted Attacks by Statistic Alignment
### Venue: IJCAI 2021
1.Why?在adversarial example领域，目前主流的target attack方法，选择欧氏距离来衡量源特征和target特征之间的差距，这是存在问题的，它引入了不必要的空间匹配限制。就如一张image被识别为cat，和这只cat在image的左边还是右边没关系。2. What？
文章指出了现有方法引入不必要空间约束的问题，提出了两种攻击方法来解决，分别是：PAA和GAA，这两种方法通过对齐source和target的高阶统计，而不是对齐它们的欧式距离。3. How?
引入和MMD，它解决的是two-sample problem。4. How much?
在ImageNet上表现SOTA。5. What then？
文章没有提到。但这篇文章的工作很solid，行文也很清晰，值得follow。