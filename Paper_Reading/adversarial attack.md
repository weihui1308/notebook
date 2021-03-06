# 1: 20220502
### Title: Context-Aware Transfer Attacks for Object Detection
### Venue: AAAI 2022
目标检测模型是context-aware的，受此启发，作者提出context-aware attack，利用的context信息有cooccurrence of objects, relative locations, size。通过添加helper objects，实现了对目标检测模型的可迁移攻击。
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
制作Adversarial T-shirt攻击person detector。针对T-shirt的非刚性变形，文章提出了TPS transformation。
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
# 17: 20220511
### Title: Intriguing properties of neural networks
### Venue: ICLR 2014
该paper主要是发现了以下两个有趣的性质：①神经网络中携带语义信息的不是某单个神经元，而是整个网络（或者说那一层）所表示的空间；②给样本添加一些轻微的扰动，会导致神经网络模型错误分类，这些样本就称为对抗样本（一般认为这篇paper是对抗样本的开山之作）
# 18: 20220512
### Title: Explaining and Harnessing Adversarial Examples
### Venue: ICLR 2015
本文提出FGSM（fast gradient sign method）攻击算法，该算法通过修改输入图像的像素值使得修改后的图像能够扰乱分类网络的分。具体做法是：一方面是基于输入图像计算梯度，另一方面在更新输入图像时是加上梯度，而不是减去梯度，这和常见的分类模型更新参数正好背道而驰，以此使模型产生错误的预测结果。
# 19: 20220512
### Title: Adversarial examples in the physical world
### Venue: ICLR 2017
FGSM算法从梯度的角度做攻击，速度比较快，这是该算法比较创新的地方。但是FGSM算法只涉及单次梯度更新，有时候单次更新并不足以攻击成功，因此，在此基础上推出迭代式的FGSM，这就是I-FGSM（iterative FGSM）。在该篇论文中提出了目标攻击，将输入图像分类成原本最不可能分到的类别。相比FGSM算法，I-FGSM算法的攻击成功率提升得还是非常明显的。
# 20: 20220512
### Title: DeepFool: a simple and accurate method to fool deep neural networks
### Venue: CVPR 2016
本文为Adversary Attack方向的一篇经典论文。算法名为DeepFool，其目标是寻求最小的扰动来达到生成对抗样本的目标。这是一种untargeted attak，该算法是通过寻求当前的点在高维空间中离所有非真实类的决策边界中最近的一个，来作为攻击后的label。
# 21: 20220513
### Title: Towards Evaluating the Robustness of Neural Networks
### Venue: SP 2017
该篇论文证明defensive distillation不能显著地提高模型的鲁棒性，并提出3种新的攻击算法，可以在distilled和undistilled神经网络达到100%的攻击成功率。它把构建对抗样本的过程转化为一个最优化问题。
# 22: 20220513
### Title: Accessorize to a Crime: Real and Stealthy Attacks on State-of-the-Art Face Recognition
### Venue: ACM SIGSAC 2016
本文从物理空间攻击人脸识别系统，攻击的方法使佩戴特殊的、具有攻击性的眼镜。
# 23: 20220513
### Title: Advhat: Real-world adversarial attack on arcface face id system
### Venue: ICPR 2021
本文从物理空间攻击人脸识别系统，攻击的方法使佩戴具有攻击性的帽子。
# 24: 20220513
### Title: Adv-Makeup: A New Imperceptible and Transferable Attack on Face Recognition
### Venue: IJCAI 2021
本文从物理空间攻击人脸识别系统，攻击的方法是采用具有攻击性的妆容。
# 25: 20220513
### Title: Making an Invisibility Cloak: Real World Adversarial Attacks on Object Detectors
### Venue: ECCV 2020
作者关注生成的patch在不同模型之间的迁移性，在不同数据集之间的迁移性，并且做了详尽的实验，实现了physical attach。
# 26: 20220514
### Title: DVS-Attacks: Adversarial Attacks on Dynamic Vision Sensors for Spiking Neural Networks
### Venue: IJCNN 2021
这篇文章攻击的模型是Spiking Neural Networks（脉冲神经网络）。数据来源是DVS（Dynamic Vision Sensors） camera。这种摄像头可以记录时间序列的信息。
# 27: 20220516
### Title: Adversarial Texture for Fooling Person Detectors in the Physical World
### Venue: CVPR 2022
这篇文章提出在利用patch攻击目标检测模型时，会出现部分缺失问题，通俗一点讲就是随着摄像头视角的变化，对抗patch只有一部分或者全部都无法被摄像头捕获到，从而无法完成攻击。即对抗patch无法进行多视角的攻击。为了解决这个问题，本文提出了Adversarial Texture，一种覆盖在衣物表面的纹理，当人们穿上印有Adversarial Texture的衣服时，无论在哪一个角度，检测模型都无法识别到。生成Adversarial Texture是一个two-stage方法，其中stage one负责训练一个可以扩展的生成器，给该生成器输入一个随机变量z，它可以生成任意形状的对抗patch。stage two负责优化变量z以提高对抗patch的攻击性。在数字空间和物理空间的实验结果显示，当一个人穿着本文方法生成的Adversarial Texture所覆盖的衣服时，在监控摄像头视野范围内转圈或者做出不同姿态，都不会被检测到。
# 28: 20220516
### Title: Naturalistic Physical Adversarial Patch for Object Detectors
### Venue: ICCV 2021
为了生成更自然的adversarial patch，作者使用在自然数据集（eg. imagenet）训练好的BigGAN（或StyleGAN）来生成具有攻击性的patch。优化的参数是输入generator的latent space code，而不是GAN网络的参数。整篇文章的思路循规蹈矩，但结果很好，实验做得很充实全面。
# 29: 20220517
### Title: Infrared Invisible Clothing: Hiding from Infrared Detectors at Multiple Angles in Real World
### Venue: CVPR 2022
采用气溶胶做成的衣服攻击热红外行人检测系统，达到多角度攻击的效果。生成攻击texture的方法仍然是生成patch的思路。
# 30: 20220517
### Title: Generating Adversarial yet Inconspicuous Patches with a Single Image
### Venue: AAAI 2021 (student abstract)
这个工作的完成版论文是：Inconspicuous Adversarial Patches for Fooling Image Recognition Systems on Mobile Devices，于2019年发表在IEEE Internet of Things Journal。论文方法生成一个几乎透明的patch，是一个GAN-based方法。论文没有提到physical attack，只在White-box and Black-box Attack上有评估结果。论文提出the contextual consistency。
# 31: 20220523
### Title: Optical Adversarial Attack
### Venue: ICCV 2021
作者提出利用投影仪（projector）将structured illumination投射到物理上，进而达到攻击效果，这个方法是一个projector-camera model。并且好处是不用直接接触物体（例如贴patch），而且得益于光的传播速度非常快，攻击可以在很短时间内完成。
# 32: 20220527
### Title: Semantic Adversarial Examples
### Venue: CVPRW 2018
本文通过将image从RGB空间转移到HSV空间，生成Semantic Adversarial Examples，在搜索时只改变H和S，以保证图像的语义结构。生成的对抗样本，人的视觉仍然可以辨认出图像中的物体，但是分类模型会给出错误的预测。
# 33: 20220528
### Title: Diffusion Models for Adversarial Purification
### Venue: PMLR 2022
本文用diffusion model做对抗防御，效果非常好。训练时方法的输入是Adversarial image，经过diffusion model，输出Purified image，然后将其输入一个classifier中，使其分类正确。这是首次利用diffusion model来做Adversarial Purification。
# 34: 20220530
### Title: A Survey on Universal Adversarial Attack
### Venue: IJCAI 2021
作者对UAP（Universal Adversarial Perturbations）进行综述，UAP指一个perturbation可以在很多image上欺骗target model。文章介绍了什么是UAP，并且对UAP的方法进行罗列、分类、评论和防御。讨论了关于UAP为什么存在的一些研究。讨论了UAP面对的挑战。最后列举了UAP在别的工作上的研究（本文是在image classifier），如semantic segmentation，video recognition，video recognition，Audio Classification。
# 35: 20220531
### Title: NAG: Network for Adversary Generation
### Venue: CVPR 2018
本文提出用GAN的结构生成universal adversarial perturbations，该方法用了两个loss，一个控制攻击，一个控制生成结果的diversity。攻击的分类任务，在digital space。主要贡献1是首次证明可以通过一个生成模型来建模某个classifier的adversarial perturbation的分布，2是经验上地证明生成模型可以capture到perturbation的分布，生成了多样化的perturbation。
# 36: 20220601
### Title: Adversarial Imaging Pipelines
### Venue: CVPR 2021
作者提出了一个新的工作，对相机捕获到的RAW image进行攻击，由于相机会对RAW image进行后续的ISP，所以作者提出的攻击可以不受ISP的影响。作者用U-Net构建了Differentiable Proxy ISPs，用来得到ISP的近似梯度。实验部分搭建了捕获数据的平台，有一个相机拍摄屏幕上的图像，获得RAW image，然后将adversarial perturbations直接添加到RAW image上面。作者攻击的是classification任务。
# 37: 20220616
### Title: Shadows can be Dangerous: Stealthy and Effective Physical-world Adversarial Attack by Natural Phenomenon
### Venue: CVPR 2022
本文提出一种新的对抗攻击方式：用影子进行攻击，这是一种基于光学的方式。之所以用影子，是为了满足攻击的隐蔽性，影子不容易引起人注意。作者在digital domain上建模如何向image上添加影子，影子的shape是多边形，多边形的坐标是在训练过程中优化得到的，影子的value是可以调节的超参数。在训练时，作者发现会出现梯度爆炸或者梯度消失的情况，因此作者采用了粒子群算法来寻找最优解。作者分别在digital domain和physical domain上做了实验，结果显示在untargeted attack上，攻击的成功率非常高。本文代码开源。
# 38: 20220630
### Title: Dual-Key Multimodal Backdoors for Visual Question Answering
### Venue: CVPR 2022
本文首次提出对多模态任务的后门攻击，攻击任务是VQA model。攻击方法用两个trigger，一个是question trigger, 一个是visual trigger。只有当两个trigger都出现时，才会触发攻击，单独出现一个不会触发。本文提出了一个实验证明：越复杂的模型，面对后面攻击越脆弱。
# 39: 20220723
### Title: Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches
### Venue: ECCV 2022


# 40: 20220725
### Title: Threat Model-Agnostic Adversarial Defense using Diffusion Models
### Venue: Arxiv 202207