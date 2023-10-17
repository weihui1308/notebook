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
用Adversarial Patch攻击detector(YOLOv2)，实现physical adversarial attack。
# 4: 20220504
### Title: Fooling thermal infrared pedestrian detectors in real world using small bulbs
### Venue: AAAI 2021
将Adversarial Patch攻击应用在热红外成像下的目标检测任务中，用发光的小灯泡制作patch，实现了physical attack。
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
本文提出FGSM（fast gradient sign method）攻击算法，该算法通过修改输入图像的像素值使得修改后的图像能够扰乱分类网络的得分。具体做法是：一方面是基于输入图像计算梯度，另一方面在更新输入图像时是加上梯度，而不是减去梯度，这和常见的分类模型更新参数正好背道而驰，以此使模型产生错误的预测结果。
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
### Title: Attacking Optical Flow
### Venue: ICCV 2019
本文首次提出攻击Optical Flow Estimation，并且实现了attack in the real world。本文采用的是patch-based attack。通过实验，本文发现基于encoder-decoder networks的model，面对攻击时非常脆弱，然而攻击对spatial pyramid networks的影响很小，对传统的非deep learning方法的影响也很有限。
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
### Title: Harnessing Perceptual Adversarial Patches for Crowd Counting
### Venue: ACM CCS 2022
1. Why? 尚没有人研究Crowd Counting任务的鲁棒性。
2. What? 采用adversarial patch对Crowd Counting Model进行攻击，并且在physical world中有效。
3. How? 传统的patch-based attack，设计了针对该任务的loss。
4. How much? at most +685.7 MAE and +699.5 MSE
5. What then? 无
# 39: 20220723
### Title: Physical Attack on Monocular Depth Estimation with Optimal Adversarial Patches
### Venue: ECCV 2022
本文提出对单目深度估计（Monocular Depth Estimation）任务的攻击，是patch-based方法。可以在physical world实现攻击。首先，为了定位感受野的敏感区域，作者设计了一种优化区域的策略，参数是patch四个顶点的位置。然后，为了使模型估计target的位置更远，作者设计了相应的目标函数。在隐蔽性方面，作者从patch size minimization和natural appearance两方面考虑，采用了风格迁移技术。本文首次在physical world中实现对单目深度估计任务的攻击。
# 40: 20220725
### Title: Threat Model-Agnostic Adversarial Defense using Diffusion Models
### Venue: Arxiv 202207
本文提出了一个adversarial defense方法，该方法属于preprocessing method，即对输入model的example进行预处理。具体做法：作者使用diffusion model对input image进行重建，从而破坏或者去除image上的perturbation，从而达到防御目的。
# 41: 20220728
### Title: Watermark Vaccine: Adversarial Attacks to Prevent Watermark Removal
### Venue: ECCV 2022
本文提出水印疫苗，攻击水印去除网络，是对抗攻击技术一个典型的应用场景。作者提出两种攻击方式，一是Disrupting Watermark Vaccine（DWV，破环性水印疫苗），可以使水印去除网络的输出变为被破坏的图片；二是Inerasable Watermark Vaccine（IWV，才不掉的水印），可以使水印去除网络失效，水印去不掉，而且不影响图像其它区域。这是首次把对抗攻击应用到该应用的工作。
# 42: 20220801
### Title: Adversarial Zoom Lens：A Novel Physical-World Attack to DNNs
### Venue: Arxiv 202206
本文提出了一种新的攻击，AdvZL，这种攻击无需任何perturbation，只通过zoom in和out即可实现对DNN-based classifer的攻击。作者提出了一个基于Imagenet的数据集，Imagenet-ZOOMIN，这个数据集将Imagenet中的图像进行了不同尺度的zoom in。通过在数字和物理空间上的实验，验证了这种攻击方式的有效性。该方法从一定程度上展示出了DNN在面对图像尺度缩放时的局限性。
# 43: 20220923
### Title: GAMA: Generative Adversarial Multi-Object Scene Attacks
### Venue: NeurIPS 2022
本文将vision-language model CLIP引入了attack方法的pipeline中，CLIP作为一个tool，作者利用其语义建模能力，将生成的adversarial example通过一个代理模型，转换为text输入到CLIP的text encoder中，然后将original image输入到image encoder中，通过最小化对比学习中的similarity，达到攻击的目的。本文关注的是Multi-Object Scene，这也是和之前关注single-object scene的方法的区别之一。
# 44: 20220923
### Title: Adversarial Color Projection: A Projector-Based Physical Attack to DNNs
### Venue: Arxiv 202209
由于当前多数的physical attack都是基于sticker的，他们很难做到隐蔽，因此作者提出一种light-based attack，采用projector-based方法，改变victim object表面的light，以此来发动攻击。本文方法命名为AdvCP。
# 45: 20220924
### Title: Moiré Attack (MA): A New Potential Risk of Screen Photos
### Venue: NIPS 2021
本文提出摩尔纹可能会变为一种潜在的风险，并做了实验验证这一想法。作者提出Moire Attack，在digital space中，采用一种可控的摩尔纹生成算法，将其添加到imagenet数据集中的图像上。然后将添加摩尔纹之后的图像输入到Inception-V3网络中，根据输出反传回摩尔纹生成的过程，直到攻击达成。该攻击达到100%和97% ASR的untargeted attack和targeted attack，同时，由于摩尔纹是一种常见现象，因此该攻击不容易被发现。然而，这是一种digital attack，在physical space中添加摩尔纹，是难以实现的。这篇文章的写作非常精简清晰，值得参考。
# 46: 20220927
### Title: Catoptric Light can be Dangerous: Effective Physical-World Attack by Natural Phenomenon
### Venue: Arxiv 202209
本文提出一个light-based physical attack方法在夜间攻击sign classifier: adversarial catoptric light (AdvCL)。AdvCL用反射光，一种自然的现象发动转瞬即逝的攻击，隐蔽性好。它提出一种遗传算法来优化反射光的物理参数：Location, Color, Intensity。
# 47: 20220928
### Title: FG-UAP: Feature-Gathering Universal Adversarial Perturbation
### Venue: Arxiv 202209

# 48: 20220928
### Title: Suppress with a Patch: Revisiting Universal Adversarial Patch Attacks against Object Detection
### Venue: Arxiv 202209
本文用adversarial patch来攻击object detection model。title中suppress一词的含义是镇压detector使其检测不到object。具体地，本文实现了一种位置无关的patch，评估了三种可能的patch粘贴方式：a fixed position, dynamic window approach, and random patch placement。本文工作和现有工作的区别：本文利用一个patch来镇压所有object。
# 49: 20221001
### Title: A Survey on Physical Adversarial Attack in Computer Vision
### Venue: Arxiv 202209
浙江大学Donghua Wang。本文总结了物理对抗攻击在三个任务中的进展：Image recognition task，Object detection task，Semantic segmentation task。罗列了当前研究在提高物理对抗攻击性能方面的一些技术。
# 50. 20221003
### Title: Physical Adversarial Attack meets Computer Vision: A Decade Survey
### Venue: Arxiv 202210
近年来，计算机视觉领域涌现出大量对抗攻击的工作，它们暴露了DNN-based model的脆弱性，并引起学术界和工业界对Trustworthy AI的关注。其中，发生在物理世界中的对抗攻击（physical adversarial attack）由于其在真实世界的可操作性，尤其引起人们担忧。物理对抗攻击方法多样、形式多变，但目前仍没有综述工作系统性地讨论、评估和总结该领域的发展情况和前沿研究。在本文中，我们首次关注物理对抗攻击在计算机视觉领域的进展，通过对150+篇论文的分析，提供了一个系统的综述。我们发现，在所有的物理对抗攻击方法中，携带扰动的介质（如Patch, Eyeglass, Light等）是必不可少的，于是我们提出一个新的概念：对抗介质（Adversarial medium），并围绕它，在图像分类（Classification）、检测（Detection）和重识别（Re-Identification）三大主流任务上，讨论分析了当前攻击方法的Effectiveness、Stealthiness和Robustness。并且，我们以攻击person detector为例，总结了发动物理对抗攻击的关键因素。在此基础上，我们讨论了当前物理对抗攻击领域面对的挑战和一些潜在的机会。
# 51. 20221004
### Title: Untargeted, Targeted and Universal Adversarial Attacks and Defenses on Time Series
### Venue: IJCNN 2020
本文对time series classification models进行targeted, untargeted, and universal adversarial attack。实验结果显示传统的攻击方法如FGSM和BIM可以在该任务上取得很高的攻击成功率。采用的数据集是UCR time series datasets。文中有对adversarial attack如何分类进行了说明。
# 52. 20221004
### Title: GhostImage: Remote Perception Attacks against Camera-based Image Classification Systems
### Venue: USENIX 2020
# 53. 20221004
### Title: Adversarial Objects Against LiDAR-Based Autonomous Driving Systems
### Venue: Arxiv 2019
# 54. 20221007
### Title: Natural Color Fool: Towards Boosting Black-box Unrestricted Attacks
### Venue: NIPS 2022
# 55. 20221007
### Title: Over-the-Air Adversarial Flickering Attacks against Video Recognition Networks
### Venue: CVPR 2021
# 56. 20221007
### Title: Sparse and Imperceptible Adversarial Attack via a Homotopy Algorithm
### Venue: PMLR 2021
# 57. 20221008
### Title: Part-Based Models Improve Adversarial Robustness
### Venue: Arxiv 202210
# 58. 20221008
### Title: Invisible Mask: Practical Attacks on Face Recognition with Infrared
### Venue: Arxiv 2018 
# 59. 20221008
### Title: VISUAL PRIVACY PROTECTION BASED ON TYPE-I ADVERSARIAL ATTACK
### Venue: Arxiv 202209
# 60. 20221009
### Title: Perceptual Attacks of No-Reference Image Quality Models with Human-in-the-Loop
### Venue: NIPS 2022
# 61. 20221009
### Title: On Attacking Out-Domain Uncertainty Estimation in Deep Neural Networks
### Venue: Arxiv 202210
1. Why? 
2. What?
3. How?
4. How much? 
5. What then?
# 62. 20221009
### Title: WaveSpy: Remote and Through-wall Screen Attack via mmWave Sensing
### Venue: 2020 IEEE Symposium on Security and Privacy
本文设计了一种可以远程甚至是隔墙的窥屏技术WaveSpy。该技术利用在远程毫米波传感器下的液晶响应效应，是一种end to end层级系统。作者实验评估了这种屏幕攻击的效果，结果显示在真实世界中，WaveSpy实现了99%的屏幕内容类型识别和87.7%的敏感信息检索。作者把该任务称为Screen Attack。
# 63. 20221011
### Title: Universal Adversarial Perturbations: Efficiency on a small image dataset
### Venue: Arxiv 202210
这篇论文详细记录了复现一篇UAP论文（CVPR 2017）的过程。文章写作非常清晰，描述了很多细节，是一个很好的实验参考和写作参考。在复现的基础上，本文还分析了dominant labels，并和一些方法做了对比，提出了自己的一些思考。
# 64. 20221014
### Title: Interpreting Attributions and Interactions of Adversarial Attacks
### Venue: ICCV 2021
1. Why? 
2. What?
3. How?
4. How much? 
5. What then?
# 65. 20221014
### Title: Evaluating the Robustness of Semantic Segmentation for Autonomous Driving against Real-World Adversarial Patch Attacks
### Venue: WACV 2022
本文首次在physical world中攻击Semantic Segmentation任务。所提方法是一个中规中矩的patch-based attack方法。关注的是real-world driving scenario。通过实验结果，本文得出一个结论：Semantic Segmentation Model在physical world中有较强的robustness，patch-based attack的效果在real world中并不好。
# 66. 20221015
### Title: Too Good to Be Safe: Tricking Lane Detection in Autonomous Driving with Crafted Perturbations
### Venue: USENIX 2021
本文首次攻击Lane Detection任务，并在physical world中实现了。本文首先在数字世界中寻找最好的扰动，具体地，建立了一个基于摄动的可见度和相应检测车道的可见度的优化问题，以找到最优的可导致虚假车道但不被人类感知的摄动。然后，根据数字世界的最佳干扰，在现实世界中部署标记，然后评估对真实车辆的攻击。本文在一辆特斯拉S型汽车上进行了大量的实验，实验结果表明车道检测模块可以被非常不显眼的扰动欺骗，从而创建车道，在自动转向模式下误导车辆。
# 67. 20221015
### TItle: Pre-trained Adversarial Perturbations
### Venue: NIPS 2022
1. Why? 
2. What?
3. How?
4. How much? 
5. What then?
# 68. 20221017
### TItle: Face Pasting Attack
### Venue: Arxiv 202210
本文只有4页，但论文的各个部分都有，主要内容是记录了参加的一个比赛所用的方法，他们在比赛中取得了第三名的成绩。该比赛关注攻击人脸识别模型，提供了API接口。文中有介绍该比赛的部分。作者采用的方法非常直接，代码开源。
# 69. 20221018
### TItle: Learning Coated Adversarial Camouflages for Object Detectors
### Venue: IJCAI 2022
本文分析了利用patch进行攻击的弊端：在3D object上多视角攻击下性能会降低。基于此，提出了Coated Adversarial Camouflages。作者提出dense proposals attack strategy，而且建立了一个Unity simulation scene来评估攻击性。在physical world，作者利用3D打印技术，将生成的camouflage印在3D object上，用以评测physical attack的效果。
# 70. 20221019
### TItle: 360-Attack: Distortion-Aware Perturbations from Perspective-Views
### Venue: CVPR 2022
作者提出在spherical images上添加扰动，生成spherical adversarial example。spherical images是有全景相机采集到的，近年来被广泛应用。在处理spherical images时，有两类方法，一类是先把spherical images投影为2D images，然后再进行后续的处理；另一类是直接在spherical image domain上进行处理。本文采用方法中规中矩，但这个工作是adversarial attack与新领域的结合。实验评估时，作者攻击了3D Object Classification任务。
# 71. 20221020
### Title: Attacking Motion Estimation with Adversarial Snow
### Venue: ECCV Workshop 2022
本文针对motion estimation algorithms，设计了一个differentiable snowflake renderer来生成adversarial example。本文探索optical flow methods在真实世界的鲁棒性，例如在下雪的环境中。不同于以往方法在图像上添加2D per-pixel perturbations，该方法通过优化3D spatial positions of snowflakes in the scene，生成的adversarial example不仅攻击性好，而且视觉上是自然的。
# 72. 20221028
### Title: Isometric 3D Adversarial Examples in the Physical World
### Venue: NIPS 2022
本文探索在物理空间对3D点云识别模型的攻击。为了提高3D adversarial example的naturalness，作者约束其在一个$\epsilon$-isometric内。为了提高robustness under physical world，作者提出maxima over transformation (MaxOT) method来search最harmful的transformations。物理攻击的实验策略如下：在数字空间生成3d adversarial example，然后采用3d打印技术生成这些example，生成之后再对其进行扫描，把扫描的点云数据输入识别模型进行攻击。
# 73. 20221028
### Title: Toward Understanding and Boosting Adversarial Transferability From a Distribution Perspective
### Venue: TIP 2022
1. Why? 现有研究已经提出了很多方法来增强对抗迁移性，但是迁移性的原因依旧是未解之谜。无目标攻击对抗样本的迁移性在源模型和目标模型结构相似时效果尚佳，但是如果模型结构差异较大时效果下降明显，如从 CNN 迁移到 ViT。有目标攻击场景下，使用迭代方法产生的对抗样本的迁移性非常低，目前效果最佳的方法是基于生成模型的方法，需要针对每一个目标类别训练生成模型。
2. What? 考虑到在做图像识别时，模型架构是多种多样的，但是它们都有一个共同的点--训练数据集是服从相同分布的。深度学习中有一个典型的假设“独立同分布”，即验证集的数据与训练集的数据虽然是独立的，但是是服从相同的数据分布的。不同模型都期待能够将属于特定分布的图像分类为特定类别，比如将来自于“猫”类别的图像预测为“猫”。但是如果样本是一个分布外样本(out-of-distribution)，深度模型往往难以给出准确的预测。因此本文提出从data distribution的角度理解adversarial transferability。此外，本文提出一个匹配模型梯度和数据分布梯度的方法。
3. How? 本文提出应该从数据分布的视角来理解迁移性，如果无目标攻击能够使数据成为分布外样本，那么不同的模型都将难以识别该样本，这样的无目标攻击应该具有更强的迁移性；如果有目标攻击能够使数据成为目标分布内的样本，那么不同的模型都倾向于将该样本分类为目标类。
4. How much? 现有最佳基于生成模型的攻击方法TTP成功率是46.47%，而本文方法可以达到75.93%的成功率，超过现有最佳方法 29.46%。目前有目标迁移性攻击效果最佳的方法。
5. What then? 文中没有提到。个人考虑：从数据分布的角度考虑adversarial attack。
# 74. 20221031
### Title: Adversarial Patch Attack on Multi-Scale Object Detection for UAV Remote Sensing Images
### Venue: remote sensing
1. Why? 目前，针对遥感图像的攻击有如下挑战：当前大多数都关注digital attack；遥感图像的number of objects比images captured on the ground要多，因此adversarial effect on all objects更有难度；遥感图像中objects的size有很大不同。
2. What? 本文formulate a joint optimization problem来生成更有攻击力的adversarial patch，并且提出scale factor来rescale对抗补丁。在物理空间做了实验。
3. How? 在物理空间的实验，采集数据设备是一台DJI Mini 2。方法和主流的adversarial patch attack类似。
4. How much? 攻击了YOLO-v3和YOLO-v5。
5. What then? 在physical space中，高度变化会带来攻击性能的下降。
# 75. 20221101
### Title: Benchmarking Adversarial Patch Against Aerial Detection
### Venue: Arxiv 202211
1. Why? 当前的patch攻击方法是time-consuming, high computation costs; 迁移到物理空间性能会降低等。
2. What? 提出了对aerial detection任务的攻击，采用的是patch-based attack。
3. How? 本文在多个detector上做实验。
4. How much? AP下降87.86% and 85.48% in white-box and blackbox settings, respectively。
5. What then? search patch的最优位置和形状。
# 76. 20221108
### Title: Diversified Adversarial Attacks based on Conjugate Gradient Method
### Venue: ICML 2022
该论文中作者借鉴对此类问题有效的共轭梯度方法，并提出了一种基于共轭梯度法方法新的对抗攻击算法。其实在大学的最优化课程里，会涉及学到最速下降法，共轭梯度法 ，以及拟牛顿法。作者很好的将共轭梯度法应用到了对抗攻击中去。
实验结果表明，对于大多数模型，论文提出的方法比现有的SOTA算法能够以更少的迭代次数找到更优的对抗样本，而且论文所提出方法的更多样化的搜索显著提高了对抗攻击的成功率。
共轭梯度法一般用于求解线性问题，之后又被延伸用于求解最小化凸二次型问题和一般的非线性问题。共轭梯度法可以用在无约束和投影有约束问题中。
# 77. 20221110
### Title: Poster: On the System-Level Effectiveness of Physical Object-Hiding Adversarial Attack in Autonomous Driving
### Venue: ACM CCS 2022
1. Why? 当前在自动驾驶任务中的object-hiding adversarial attacks能否真正地完成对real-world自动驾驶系统产生影响尚不明确，原因是这些attacks往往都只关注对AI组件的攻击，而不是整个闭环系统。因此本文对这些attacks在系统层面做了comprehensive measurement study。
2. What? 证明了当前的方法无法攻击自动驾驶系统。
3. How? 本文选择STOP sign-hiding attack作为评估的对象，选择了两种方法，在PASS (Platform for Autonomous driving Safety and Security) platform上进行评估。
4. How much? 结果显示，测试的两种攻击方法都不能带来任何system-level impact in AD system。
5. What then? 对更多的方法进行the measurement study，然后指导设计出better achieve the system-level effects in the AD.
# 78. 20221111
### Title: Assessing the Impact of Transformations on Physical Adversarial Attacks
### Venue: ACM AISec 2022

# 79. 20221112
### Title: TPatch: A Triggered Physical Adversarial Patch
### Venue: USENIX 2023
本文提出一种触发式的物理对抗攻击。由于之前的攻击方法是无差别攻击，对于每一个经过的目标都进行攻击，这种设置会增大暴露攻击的风险，因此作者提出一种可以控制的攻击（当trigger激活时攻击，没有激活时不攻击）。本文最大的挑战是如何设计trigger。作者利用声音信号干扰自动驾驶系统的成像，形成的blur作为trigger。在此基础上进行优化patch。本文提出了三种攻击，有hiding, creating or altering attack。
# 80. 20221112
### Title: Poltergeist: Acoustic Adversarial Machine Learning against Cameras and Computer Vision
### Venue: IEEE Symposium on Security and Privacy (SP) 2021
1. Why? 在自动驾驶场景中，未来提高系统的稳定性，会增加一些除视觉传感器之外的传感器，例如为了deblur的惯性传感器。
2. What? 本文提出一个system-level vulnerability，并针对这一点进行攻击自动驾驶任务中的检测器。
3. How? 作者利用Acoustic Waves干扰惯性传感器，使系统拍出来的照片带有blur，以此达到攻击的效果。
4. How much? 在4个academic object detector: YOLO V3/V4/V5 and Fast R-CNN和一个ommercial detector: Apollo，进行了实验的评估。
5. What then? 本文列举了一系列类似的攻击措施，统称为PG attacks，有一些潜在的机会。
# 81. 20221114
### Title: Fooling the Eyes of Autonomous Vehicles: Robust Physical Adversarial Examples Against Traffic Sign Recognition Systems
### Venue: arXiv 202201
1. Why? 
# 82. 20221115
### Title: Attacking Face Recognition with T-shirts: Database, Vulnerability Assessment and Detection
### Venue: arXiv 202211
文章关注人脸识别算法的安全性。作者提出一种攻击方式被称为presentation attacks，通过在T-shirt上印一张人脸图像，攻击face recognition systems。作者制作了一个database，里面包含1608个T-shirt attacks。评估结果显示一些state-of-theart attack detection mechanisms trained on popular benchmark面对这种攻击时无法保持鲁棒性。此外，作者还提出三种方法来检测这类攻击。
# 83. 20221115
### Title: Butterfly Effect Attack: Tiny and Seemingly Unrelated Perturbations for Object Detection
### Venue: arXiv 202211
本文提出了Butterfly Effect Attack，探索不相干的perturbation对与detector的影响。具体的，作者将perturbation添加到图像的左侧，然而图像右侧的object在detector检测时也会收到干扰。通过在KITTI dataset上评估了yolov5和DETR两种检测器。作者定义了三个目标函数：Small perturbation，Performance degradation和Degree of unrelated perturbation，通过genetic algorithm来优化生产扰动。
# 84: 20221118
### Title: Towards Good Practices in Evaluating Transfer Adversarial Attacks
### Venue: arXiv 202211
本文关注在transfer adversarial attack研究中，不同攻击方法之间的对比非常difficult，并且新的攻击方法提出时，和旧的攻击方法对比的设置常常是unsystematic并且unfair。第二，当前transfer adversarial attack方法在评估时，忽略了stealthiness的对比。因此，本文提出了一个Good Practices来解决这些限制。本文评估了23中transfer attack方法在9种defense方法的表现，基于这些，作者分析了结果，提出了新的findings。
# 85: 20221118
### Title: Meta-Attack: Class-agnostic and Model-agnostic Physical Adversarial Attack
### Venue: ICCV 2021


# 86: 20221119
### Title: Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving
### Venue: ACM CCS 2019
本文首次研究应用的自动驾驶中LiDAR的安全性。具体地，本文的攻击目标是在AV系统的前方添加一个不存在的障碍物，以此改变其行驶决策。该方法通过控制spoofed points来欺骗深度学习模型，将攻击建模为一个优化问题。本文工作量很大，共13页。
# 87: 20221130
### Title: Imperceptible Adversarial Attack via Invertible Neural Networks
### Venue: AAAI 2023
本文利用Invertible Neural Networks（可逆神经网络）生成adversarial example。作者将现有的方法总结为两类：Adding adversarial perturbations和Dropping existing information。而本文提出的方法AdvINN一方面向 benign image 中添加 class-specific 信息，另一方面丢弃original class的discriminant信息，目的是生成imperceptible and robust的对抗样本。
# 88: 20221230
### Title: Simultaneously Optimizing Perturbations and Positions for Black-box Adversarial Patch Attacks
### Venue: TPAMI 2022
本文攻击Face Recognition (FR) task。作者观察到当前的patch-based攻击方法要么是固定位置优化扰动，要么是固定扰动优化位置，由此得出位置和扰动对于攻击都是重要的。所以本文采用强化学习的策略来同时优化位置和扰动。本文考虑了攻击成功率和query的次数两个性能指标。本文验证了所提方法可以在物理空间实现攻击。本文方法不但可以攻击FR task，还可以扩展到traffic sign recognition task。
# 89: 20230103
### Title: Do Adaptive Active Attacks Pose Greater Risk Than Static Attacks?
### Venue: WACV 2023
# 90: 20230103
### Title: Phantom Sponges: Exploiting Non-Maximum Suppression to Attack Deep Object Detectors
### Venue: WACV 2023
# 91: 20230103
### Title: Robustness of Trajectory Prediction Models Under Map-Based Attacks
### Venue: WACV 2023
# 92: 20230104
### Title: Experimental quantum adversarial learning with programmable superconducting qubits
### Venue: Nature Computational Science 202211
# 93: 20230220
### Title: Boosting Transferability of Physical Attack against Detectors by Redistributing Separable Attentions
### Venue: Pattern Recognition 2023
# 94: 20230220
### Title: TransPatch: A Transformer-based Generator for Accelerating Transferable Patch Generation in Adversarial Attacks Against Object Detection Models
### Venue: ECCVW 2022
# 95: 20230227
### Title: X-Adv: Physical Adversarial Object Attacks against X-ray Prohibited Item Detection
### Venue: USENIX Security 2023
# 96: 20230303
### Title: CBA: Contextual Background Attack against Optical Aerial Detection in the Physical World
### Venue: arXiv 202303

# 97: 20230313
### Title: AdvT-SEAersarial attacks and defenses for visual signals
### Venue: Nanyang Technological University
Nanyang Technological University，博士学位论文。地址：https://dr.ntu.edu.sg/handle/10356/164772。 本文关注四个DNN-based tasks：natural image classification task，medical image classification task, SOD, Adversarial defense。
# 98: 20230314
### Title: Patch of Invisibility: Naturalistic Black-Box Adversarial Attacks on Object Detectors
### Venue: arXiv 202303
# 99: 20230314
### Title: Adversarial Attack with Raindrops
### Venue: arXiv 202303
# 100: 20230328
### Title: Anti-DreamBooth: Protecting users from personalized text-to-image synthesis
### Venue: arXiv 202303
文本到图像扩散模型是一场革命，使得任何人，即使没有设计技能，也能从简单的文本输入中创建逼真的图像。通过强大的个性化工具如DreamBooth，它们可以生成特定人物的图像，只需学习他/她的几张参考图像。然而，当滥用时，这样一个强大而便利的工具可以制造虚假新闻或针对任何个人受害者的令人不安的内容，从而造成严重的负面社会影响。在本文中，作者探讨了一种名为Anti-DreamBooth的防御系统，以对抗DreamBooth的恶意使用。该系统旨在在发布每个用户的图像之前对其添加微小的噪声扰动，以破坏对这些扰动图像训练的任何DreamBooth模型的生成质量。本文研究了广泛的扰动优化算法，并在两个面部数据集上对各种文本到图像模型版本进行了广泛的评估。尽管DreamBooth和基于扩散的文本到图像模型的公式化很复杂，该方法有效地保护用户免受这些模型的恶意使用。即使在训练和测试之间存在模型或提示/术语不匹配等不利条件下，它们的有效性也能经受住考验。
# 98: 20230329
### Title: Universal Physical Adversarial Attack via Background Image
### Venue: Applied Cryptography and Network Security Workshops 2022


# 99: 20230329
### Title: Decision-based Black-box Attack Against Vision Transformers via Patch-wise Adversarial Removal
### Venue: NIPS 2022

# 100: 20230329
### Title: Adversarial Attack on Attackers: Post-Process to Mitigate Black-Box Score-Based Query Attacks
### Venue: NIPS 2022

# 101: 20230329
### Title: Practical Adversarial Attacks on Spatiotemporal Traffic Forecasting Models
### Venue: NIPS 2022

# 102: 20230329
### Title: On the Robustness of Deep Clustering Models: Adversarial Attacks and Defenses
### Venue: NIPS 2022

# 103: 20230329
### Title: Indicators of Attack Failure: Debugging and Improving Optimization of Adversarial Examples
### Venue: NIPS 2022

# 104: 20230329
### Title: Boosting the Transferability of Adversarial Attacks with Reverse Adversarial Perturbation
### Venue: NIPS 2022

# 105: 20230329
### Title: VoiceBlock: Privacy through Real-Time Adversarial Attacks with Audio-to-Audio Models
### Venue: NIPS 2022

# 106: 20230329
### Title: Adv-Attribute: Inconspicuous and Transferable Adversarial Attack on Face Recognition
### Venue: NIPS 2022

# 107: 20230329
### Title: ViewFool: Evaluating the Robustness of Visual Recognition to Adversarial Viewpoints 
### Venue: NIPS 2022

# 108: 20230329
### Title: Perceptual Attacks of No-Reference Image Quality Models with Human-in-the-Loop
### Venue: NIPS 2022

# 109: 20230329
### Title: Blackbox Attacks via Surrogate Ensemble Search
### Venue: NIPS 2022

# 110: 20230329
### Title: Natural Color Fool: Towards Boosting Black-box Unrestricted Attacks
### Venue: NIPS 2022

# 111: 20230329
### Title: Towards Lightweight Black-Box Attack Against Deep Neural Networks
### Venue: NIPS 2022

# 112: 20230329
### Title: Learning to Attack Federated Learning: A Model-based Reinforcement Learning Attack Framework
### Venue: NIPS 2022
作者提出一种基于Reinforcement Learning的攻击框架，实现untargeted poisoning attacks。本文工作显示了FL系统开发适应性防御的重要性。写作清晰，相关文献总结的也不错，代码开源。
# 113: 20230404
### Title: Semantic Image Attack for Visual Model Diagnosis
### Venue: arXiv 202303


# 114: 20230404
### Title: CONTROLLABLE INVERSION OF BLACK-BOX FACE-RECOGNITION MODELS VIA DIFFUSION
### Venue: arXiv 202303


# 115: 20230406
### Title: Physically Adversarial Infrared Patches with Learnable Shapes and Locations
### Venue: CVPR 2023
本文提出了一种对Infrared Person Detector进行攻击的方式。该方法采用一种Infrared Patch，制作材料为气凝胶。如title中提到的，本文方法优化的是Infrared Patch的shape和location两个属性。在实验方面，作者不仅在person detector上进行了测试，还在vehicle detection任务上进行了测试，这个实验是为了凸显方法的generalization。

# 116. 20230327
### Title: T-SEA: Transfer-based Self-Ensemble Attack on Object Detection
### Venue: CVPR 2023
基于迁移的黑盒攻击方式由于不需要获取目标模型的任何信息，更有利于真实场景的攻击，但成功率也往往更低。许多基于迁移的黑盒攻击依靠多模型集成方式来提高攻击的迁移性，也即，在训练对抗样本阶段，通过集成多个不同的白盒模型，以期训练好的对抗样本能在新的黑盒模型上表现出更强的攻击能力。但这种方式往往需要消耗大量训练时间和资源，同时，要获取同一任务的多个模型，在现实应用中也可能具有一定的实现难度。作者利用对抗补丁来对目标检测模型进行攻击，将对抗补丁贴到检测目标上，使得检测框消失。为了实现在单个白盒模型上训练的对抗补丁的迁移性，本文工作1.发现改变两个简单的训练设置即可对baseline的性能实现一定的提高；2.提出使用自集成（Self-ensemble）策略来充分提高对抗补丁的迁移性。
# 117. 20230603
### Title: Can You Spot the Chameleon? Adversarially Camouflaging Images from Co-Salient Object Detection
### Venue: CVPR 2022
本片工作首次提出攻击CoSOD模型，这是一个新的任务。作者提出联合对抗性曝光和噪声攻击，根据新设计的高特征级对比度敏感损失函数联合和局部调整图像的曝光和附加扰动。该任务对正确保护目前在互联网上共享的大量个人照片有很大的实际好处。此外，有可能被用作评估CoSOD方法稳健性的指标。
# 118. 20230720
### Title: Shape Matters: Deformable Patch Attack
### Venue: ECCV 2022


# 119. 20230720
### Title: Unified Adversarial Patch for Cross-modal Attacks in the Physical World
### Venue: ICCV 2023

# 120. 20230720
### Title: CAPatch: Physical Adversarial Patch against Image Captioning Systems
### Venue: USENIX Security 2023

# 121. 20230722
### Title: Diffusion to Confusion: Naturalistic Adversarial Patch Generation Based on Diffusion Model for Object Detector
### Venue: arXiv 202307

# 122. 20230803
### Title: RFLA: A Stealthy Reflected Light Adversarial Attack in the Physical World
### Venue: arXiv 202307

# 123. 20230803
### Title: Why Don’t You Clean Your Glasses? Perception Attacks with Dynamic Optical Perturbations
### Venue: arXiv 202307

# 124. 20230811
### Title: A reading survey on adversarial machine learning: Adversarial attacks and their understanding
### Venue: arXiv 202308

# 125. 20230818
### Title: AdvCLIP: Downstream-agnostic Adversarial Examples in Multimodal Contrastive Learning
### Venue: arXiv 202308

# 126. 20230818
### Title: ACTIVE: Towards Highly Transferable 3D Physical Camouflage for Universal and Robust Vehicle Evasion
### Venue: arXiv 202308

# 127. 20230826
### Title: Does Physical Adversarial Example Really Matter to Autonomous Driving? Towards System-Level Effect of Adversarial Object Evasion Attack
### Venue: ICCV 2023

# 128. 20230901
### Title: REAP: A Large-Scale Realistic Adversarial Patch Benchmark
### Venue: ICCV 2023
本文的motivation是：当前的adversarial patch attack的评估太难了，主要原因是如果在real world采集数据集进行评估，太expensive，如果在digital domain做simulation，许多physical world的因素get不到，因此作者提出了一个benchmark dataset来评估patch-based attack方法。本文工作针对的是traffic sign detection任务，提出了一个patch rendering的方法，主要包括Geometric Transformation和Relighting Transformation。通过在benchmark dataset上评估RP2 attack和DPatch attack，作者得出结论：当前的攻击方法有效性是不如预期的；在合成的数据集上作评估不能反映real world的情况；光照和patch的位置对攻击效果影响最大。
# 129. 20230904
### Title: Transferable Black-Box Attack against Face Recognition with Spatial Mutable Adversarial Patch
### Venue: TIFS 2023

# 130. 20230904
### Title: Adversarial Attacks on Foundational Vision Models
### Venue: arXiv 202309

# 131. 20230904
### Title: IMPERCEPTIBLE ADVERSARIAL ATTACK ON DEEP NEURAL NETWORKS FROM IMAGE BOUNDARY
### Venue: arXiv 202309

# 132. 20230911
### Title: Adv3D: Generating 3D Adversarial Examples in Driving Scenarios with NeRF
### Venue: arXiv 202309

# 133. 20230921
### Title: Are Vision Transformers Robust to Patch Perturbations?
### Venue: ECCV 2022

# 134. 20230925
### Title: PRAT: PRofiling Adversarial aTtacks
### Venue: arXiv 202309

# 135. 20231008
### Title: F&F Attack: Adversarial Attack against Multiple Object Trackers by Inducing False Negatives and False Positives
### Venue: ICCV 2023

# 136 20231008
### Title: Adversarial Examples with Specular Highlights
### Venue: ICCV 2023


# 137 20231008
### Title: Targeted Adversarial Attacks on Generalizable Neural Radiance Fields
### Venue: ICCV 2023


# 138 20231008
### Title: Benchmarking Image Classifiers for Physical Out-of-Distribution Examples Detection
### Venue: ICCV 2023 workshops

# 139 20231017
### Title: Transferable Black-Box Attack Against Face Recognition With Spatial Mutable Adversarial Patch
### Venue: TIFS 2023







