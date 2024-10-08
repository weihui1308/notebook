# 2024(两篇)
### Generative Image Dynamics

### Rich Human Feedback for Text-to-Image Generation

# 2023(两篇)
### Visual Programming: Compositional visual reasoning without training

### Planning-oriented Autonomous Driving


# 2022(一篇)
### Learning to Solve Hard Minimal Problems
该研究提出了一种在 RANSAC 框架中解决困难的几何优化问题的方法。最小化问题源于将原始几何优化问题松弛化（relax）为具有许多虚假解决方案的最小问题。该研究提出的方法避免了计算大量虚假解决方案。研究者设计了一种学习策略，用于选择初始问题 - 解决方案对以用数值方法继续解决原问题。该研究通过创建一个 RANSAC 求解器来演示所提方法，该求解器通过使用每个视图中的 4 个点进行最小松弛化来计算 3 个校准相机的相对位姿。平均而言，该方法可以在 70 μs 内解决一个原始问题。此外，该研究还针对校准相机的相对位姿这一问题进行了基准测试和研究。
# 2021(一篇)
### GIRAFFE: Representing Scenes as Compositional Generative Neural Feature Fields
深度生成模型可以在高分辨率下进行逼真的图像合成。但对于许多应用来说，这还不够：内容创作还需要可控。虽然最近有几项工作研究了如何分解数据中的潜在变化因素，但它们大多在二维中操作，忽略了我们的世界是三维的。此外，只有少数作品考虑到了场景的组成性质。我们的关键假设是，将组合式三维场景表示纳入生成模型，可以使图像合成更加可控。将场景表示为生成性神经特征场，使我们能够从背景中分离出一个或多个物体，以及单个物体的形状和外观，同时无需任何额外的监督就能从非结构化和unposed的图像集中学习。将这种场景表示与神经渲染管道结合起来，可以产生一个快速而真实的图像合成模型。正如我们的实验所证明的那样，我们的模型能够分解单个物体，并允许在场景中平移和旋转它们，还可以改变摄像机的姿势。
# 2020(一篇)
### Unsupervised Learning of Probably Symmetric Deformable 3D Objects from Images in the Wild
本文提出了一种无需外部监督即可从原始单视图图像中学习3D变形对象的方法。该方法基于自动编码器，该自动编码器将每个输入图像分解为深度，反射率，视角和照明。为了在无监督的情况下解构这些组件，作者使用了以下事实：许多对象类别至少在原则上具有对称结构。

作者通过光照的推理来利用底层对象的对称性，即使外观由于阴影而不对称。接着通过预测对称概率图来建模可能（但不一定）对称的对象，并与模型的其他组件联合起来进行端到端的学习。实验表明该方法可以从单视图图像中非常准确地恢复人脸，猫脸和汽车的3D形状，而无需任何监督或预先设定的形状模型。
# 2019(一篇)
### A Theory of Fermat Paths for Non-Line-of-Sight Shape Reconstruction
核心内容：我们提出了一个新的理论，即在一个已知的可见场景和一个不在瞬态相机视线范围内的未知物体之间的费马路径（fermat path）。这些光路或者遵守镜面反射，或者被物体的边界反射，从而编码隐藏物体的形状。 我们证明费马路径对应于瞬态测量中的不连续性。基于此，我们推导出一种新的约束，它将这些不连续处的路径长度的空间导数与表面法线相关联。 基于这一理论，我们提出了一种名为Fermat Flow的算法来估计非视距物体的形状。我们的方法第一次实现复杂对象的精确形状恢复，范围从隐藏在拐角处以及隐藏在漫射器后面的漫反射到镜面反射。 最后，我们的方法与用于瞬态成像的特定技术无关。因此，我们展示了使用SPAD和超快激光从皮秒级瞬态恢复的毫米级形状，以及使用干涉测量法从飞秒级瞬态微米级重建。我们相信，这项工作是非视距成像技术的重大进步。

获奖理由：这篇论文作出重大进步的问题是非视线内的物体形状重建，换句话说就是能看到墙角后面的东西。这篇论文的理论部分非常优美，而且同样非常给人带来激励。它把计算机视觉所能解决的问题的边界继续向前推进了一步。
# 2018(一篇)
### Taskonomy: Disentangling Task Transfer Learning
论文研究了一个非常新颖的课题，那就是研究视觉任务之间的关系，根据得出的关系可以帮助在不同任务之间做迁移学习。该论文提出了「Taskonomy」——一种完全计算化的方法，可以量化计算大量任务之间的关系，从它们之间提出统一的结构，并把它作为迁移学习的模型。实验设置上，作者首先找来一组一共 26 个任务，当中包括了语义、 2D、2.5D、3D 任务，接着为任务列表里的这 26 个任务分别训练了 26 个任务专用神经网络。结果显示，这些迁移后的模型的表现已经和作为黄金标准的任务专用网络的表现差不多好。论文提供了一套计算和探测相关分类结构的工具，其中包括一个求解器，用户可以用它来为其用例设计有效的监督策略。
# 2017(两篇)
### Densely Connected Convolutional Networks
近期的研究已经展现这样一种趋势，如果卷积网络中离输入更近或者离输出更近的层之间的连接更短，网络就基本上可以更深、更准确，训练时也更高效。这篇论文就对这种趋势进行了深入的研究，并提出了密集卷积网络（DenseNet），其中的每一层都和它之后的每一层做前馈连接。对于以往的卷积神经网络，网络中的每一层都和其后的层连接，L 层的网络中就具有 L 个连接；而在 DenseNet 中，直接连接的总数则是 L(L+1)/2 个。对每一层来说，它之前的所有的层的 feature-map 都作为了它的输入，然后它自己的 feature-map 则会作为所有它之后的层的输入。
### Learning from Simulated and Unsupervised Images through Adversarial Training
随着图像领域的进步，用生成的图像训练机器学习模型的可行性越来越高，大有避免人工标注真实图像的潜力。但是，由于生成的图像和真实图像的分布有所区别，用生成的图像训练的模型可能没有用真实图像训练的表现那么好。为了缩小这种差距，论文中提出了一种模拟+无监督的学习方式，其中的任务就是学习到一个模型，它能够用无标注的真实数据提高模拟器生成的图片的真实性，同时还能够保留模拟器生成的图片的标注信息。论文中构建了一个类似于 GANs 的对抗性网络来进行这种模拟+无监督学习，只不过论文中网络的输入是图像而不是随机向量。为了保留标注信息、避免图像瑕疵、稳定训练过程，论文中对标准 GAN 算法进行了几个关键的修改，分别对应「自我正则化」项、局部对抗性失真损失、用过往的美化后图像更新鉴别器。

这是奉行保密文化的苹果公司所发布的第一篇 AI 论文，标志着苹果公开 AI 学术研究成果、对外敞开大门的第一步。该论文发表于去年 12 月，提出了由三部分（模拟器 Simulator，精制器 Refiner，再加上一个判别器 Discriminator）组成的 SimGAN 训练方法。 有意思的是，当初就有学者对这篇论文的含金量提出质疑，认为苹果这份论文“试水”的意义远大于研究本身的意义。
# 2016(一篇)
### Deep Residual Learning for Image Recognition 
在现有基础下，想要进一步训练更深层次的神经网络是非常困难的。我们提出了一种减轻网络训练负担的残差学习框架，这种网络比以前使用过的网络本质上层次更深。我们明确地将这层作为输入层相关的学习残差函数，而不是学习未知的函数。同时，我们提供了全面实验数据，这些数据证明残差网络更容易优化，并且可以从深度增加中大大提高精度。我们在 ImageNet 数据集用 152 层--比 VGG 网络深 8 倍的深度来评估残差网络，但它仍具有较低的复杂度。在 ImageNet 测试集中，这些残差网络整体达到了 3.57% 的误差。该结果在 2015 年大规模视觉识别挑战赛分类任务中赢得了第一。此外，我们还用了 100 到 1000 层深度分析了的 CIFAR-10。 对于大部分视觉识别任务，深度表示是非常重要的。仅由于极深的表示，在 COCO 对象检查数据时，我们就得到了近 28% 相关的改进。深度剩余网络是我们提交给 ILSVRC 和 COCO2015 竞赛的基础，而且在 ImageNet 检测任务，ImageNet 定位，COCO 检测和 COCO 分割等领域赢我们获得了第一。
# 2015(一篇)
### DynamicFusion: Reconstruction and Tracking of Non-rigid Scenes in Real-Time
作者提出第一个结合商用传感器对 RGBD 扫描结果进行捕获，该结果可实时重建非刚性变形场景的密集 SLAM 系统。被称作 DynamicFusion 的这种方法在重建场景几何的当儿，还能同时估算一个密集体积的 6D 运动场景，并将估算结果变成实时框架。与 KinectFusion 一样，该系统可以生成越来越多去噪、保留细节、结合多种测量的完整重建结果，并实时显示最新的模型。由于该方法无需基于任何模板或过往的场景模型，因此适用于大部分的移动物体和场景。
# 2014(一篇)
### What Camera Motion Reveals About Shape with Unknown BRDF 
作者提出了一种理论，用于解决在未知远距离照明以及未知各向同性反射率下，运动物体的形状识别问题，无论是正交投影还是穿透投影。该理论对表面重建硬度增加了基本限制，与涉及的方法无关。在正交投影场景下，三个微分运动在不计 BRDF 和光照的情况下，可以产生一个将形状与图像导数联系起来的不变量。而在透视投影场景下，四个微分运动在面对未知的 BRDF 与光照情况，可以产生基于表面梯度的线性约束。此外，论文也介绍了通过不变量实现重建的拓扑类。 最后，论文推导出一种可以将形状恢复硬度与场景复杂性联系起来的通用分层。从定性角度来说，该不变量分别是用于简单照明的均匀偏微分方程，以及用于复杂照明的非均匀方程。从数量角度来说，该框架表明需要更多的最小运动次数来处理更复杂场景的形状识别问题。关于先前假设亮度恒定的工作，无论是 Lambertian BRDF 还是已知定向光源，一律被被当作是分层的特殊情况。作者利用合成与真实数据进一步说明了重建方法可以如何更好地利用这些框架。
# 2013(一篇)
### Fast, Accurate Detection of 100,000 Object Classes on a Single Machine
许多物体检测系统受到将目标图像与过滤器结合进行卷积所需时间的约束，这些过滤器从不同的角度对物件的外表（例如物体组件）进行编码。作者利用局部敏感散列这点，将卷积中的点积内核运算符替换为固定数量的散列探测器，这些探测器可以在无视滤波器组大小情况下，及时、有效地对所有滤波器响应进行采样。 为了向大家展示技术的有效性，作者将其用于评估 100,000 组可变形零件模型，模型将根据目标图像的多个维度需要运用超过一百万个滤波器，作者需在 20 秒内通过 20GB RAM 的单个多核处理器来达成评估目标。实验结果显示，与其他同样硬件配置下执行卷积的系统相比，该模型获得了大约 20,000 倍的提速 - 相等于四个量级。模型在针对 100,000 个物体类别的平均精确度达到了 0.16，主要因为在训练数据与基本实施的收集上面临挑战，最终模型在三分之一类别上实现至少 0.20 的 mAP，另外在大约 20％的类别上实现 0.30 或更高的 mAP。
# 2012(一篇)
### A Simple Prior-free Method for Non-Rigid Structure-from-Motion Factorization
作者提出一种简单的「无先验」方法来解决非刚性结构的运动因子分解问题。除了基本的低秩条之外，该方法无需任何关于非刚性场景或相机运动的先验知识。即便如此，它依然得以稳定运行，并产生最佳结果，且不受许多传统非刚性分解技术的基础 - 模糊性问题（basis-ambiguity issue）困扰。 该方法易于实现，可以解决包括小型与固定大小的 SDP（半定规划）、线性最小二乘或范数最小化追踪等问题。大量实验结果表明，该方法优于现有的多数非刚性因子分解线性方法。本论文不仅提供全新的理论见解，同时提供了一种适用于非刚性结构运动分解的实用日常解决方案。
# 2011(一篇)
### Real-time Human Pose Recognition in Parts from Single Depth Images
作者提出一种可以基于无时间信息从单个深度图像中快速、准确预测身体关节 3D 位置的方法。通过采用物体识别方法设计出身体部位的间接表示，进而将有难度的姿势估计问题映射为简单的每像素分类问题。作者同通过庞大、多样化的训练数据集，让分类器可以针对身体部位的姿势、身体形状、衣服等不变量进行预估，进而通过重新投影分类结果找到局部模式，最终生成具有置信度的身体关节 3D 建模。 该系统能在消费类硬件上以每秒 200 帧的速度运行。评估系统在合成与实际测试集的处理结果中显示了高精度，并分析了几个训练参数对此的影响。与相关工作相比，该模型实现了目前最先进的精度，并在全骨架最近邻匹配上有了很大进步。
# 2010(一篇)
### Efficient computation of robust low-rank matrix approximations in the presence of missing data using the L1 norm
低秩近似矩阵计算是许多计算机视觉应用中的基础操作。这类问题的主力解决方案一直是奇异值分解（Singular Value Decomposition）。一旦存在数据缺失和异常值，该方法将不再适用，遗憾的是，我们经常在实践中遇到这种情况。 论文提出了一种计算矩阵的低秩分解法，一旦丢失数据时会主动最小化 L1 范数。该方法是 Wiberg 算法的代表——在 L2 规范下更具说服力的分解方法之一。通过利用线性程序的可区分性，可以对这种方法的基本思想进行扩展，进而包含 L1 问题。结果表明，现有的优化软件可以有效实现论文提出的算法。论文提供了令人信服、基于合成与现实数据的初步实验结果。
# 2009(一篇)
### Single Image Haze Removal Using Dark Channel Prior
本文中提出了一个简单却有效、针对单个输入图像的暗通道去雾法。暗通道先验去雾法是一种户外去雾图像的统计方法，它主要基于一个关键的观察——室外无雾图像中的大多数局部斑块包含一些像素，这些像素的强度起码有一个颜色通道处于低状态。使用这种基于雾度成像模型的先验方法，我们可以直接估计图像的雾霾厚度，借此将图像恢复至高质量的无雾状态。各种模糊图像的去雾结果证明了论文所提出先验方法的成效。此外，我们可以通过该方法获得高质量的深度图。
# 2008(两篇)
### Global Stereo Reconstruction under Second Order Smoothness Priors
3D 曲面平滑度中的二阶先验是比一阶先验更好的典型场景模型。然而，基于全局推理算法（如图形切割）的二阶平滑先验法未能与二阶先验很好地进行结合，因为表达所需的三重集会产生难以处理的（非子模块）优化问题。 本文表明三重集的推理可以获得有效的优化。作者提出的优化策略是基于 α 扩展的最新研究结果，源自「QPBO」算法。该策略通过 QPBO 算法的最新扩展对提议深度图进行重复合并。对于提案深度图的来源并不受局限，比如可以是α扩展的前平行平面，亦或者带有任意参数设置的实际立体算法。最终实验结果证明了二阶先验法以及框架优化策略的有效性。
### Beyond Sliding Windows: Object Localization by Efficient Subwindow Search
大部分有效的物体识别系统都依赖于二进制分类，不过这种方法只能确认物体是否存在，而无法提供物体的实际位置。为了实现物体定位功能，我们可以考虑采用滑动窗口法，然而这将大大增加计算成本，因为必须在大量的候选子窗口上进行分类器函数评估。 为此，论文提出了一种简单而强大的分支界定方案，可以在所有可能子图像上有效最大化大类分类器函数。它在次线性时间内提供基于全局最优解的收敛方案。论文展示了该方法如何适用于不同的检测对象与场景。该方案实现的加速效果允许使用类似具有空间金字塔内核的 SVMs 或者基于χ2-距离的最近邻分类器来进行物体定位，而在过去，这些分类器被认为在处理相关任务时的速度太慢了。该方案在 UIUC 车辆数据集、PASCAL VOC 2006 数据集以及 PASCAL VOC 2007 竞赛中均取得了最先进的结果。
