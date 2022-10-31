# 1. 20220528
### Title: Diffusion Models for Adversarial Purification
### Venue: PMLR 2022
本文用diffusion model做对抗防御，效果非常好。训练时方法的输入是Adversarial image，经过diffusion model，输出Purified image，然后将其输入一个classifier中，使其分类正确。这是首次利用diffusion model来做Adversarial Purification。
# 2. 20220725
### Title: Threat Model-Agnostic Adversarial Defense using Diffusion Models
### Venue: Arxiv 202207
本文是adversarial defense和diffusion model的结合，作者利用热门的diffusion model，提出了一种preprocessing defense mechanism来防御攻击。该方法首先用threat model在image上添加扰动，得到adversarial example，然后在其上添加高斯noise，再把它输入到一个diffusion model的reverse diffusion process，由于该步骤本身就是remove noise的过程，因此可以把adversarial perturbation也remove掉。
# 3. 20221012
### Title: Adversarial Attack on Attackers: Post-Process to Mitigate Black-Box Score-Based Query Attacks
### Venue: NeurIPS 2022
上海交通大学自动化系图像处理与模式识别研究所黄晓霖副教授团队。本文关注真实场景的防御，提出主动对攻击者实施攻击，在保证用户正常使用模型（无精度/速度损失）的同时，有效阻止黑盒攻击者通过查询模型输出生成对抗样本。本文考虑通过后处理来防御，其自带以下优点：有效防御基于查询分数的攻击；不影响模型精度，甚至还能使模型的置信度更加准确；是一种轻量化，即插即用的方法。核心思路是，测试阶段主动误导攻击者进入错误的攻击方向，也就是对攻击者发动攻击（adversarial attack on attackers, AAA）
# 4. 20221013
### Title: Symmetry Subgroup Defense Against Adversarial Attacks
### Venue: Arxiv 202210
本文是一篇关于adversarial defense的工作。作者强调当前CNN分类网络缺乏不变性，例如对一张图片进行对称的transformation，分类网络就会把这张图片分类错误。利用CNN的这一内在特性，作者提出Symmetry Subgroup Defense，即将adversarial example进行symmetrically transformation，以使其失去攻击力，使分类器重新将其分类为正确标签。本文写作方式很特别，用了大量的符号定义。
# 5. 20221015
### Title: Defending Against Adversarial Attacks via Neural Dynamic System
### Venue: NIPS 2022
DNN容易被攻击的性质阻碍了其在安全关键领域的应用。为了解决这个问题，最近的一些研究提出从动力系统的角度来增强DNN的鲁棒性。根据这一思路，本文受到非自治动力系统的渐近稳定性的启发，将每个自然样本都变成缓慢时变动力系统的渐近稳定平衡点，以防御对抗攻击。本文根据动力系统平衡点理论提出: 如果一个自然样本是一个渐近稳定的平衡点，而对抗样本在这个平衡点附近，那么渐近稳定性可以降低对抗噪声，使对抗样本接近自然样本。在这个理论结果的基础上，本文发明了一种基于非自治神经常微分方程的算法(ASODE)，并对其相应的线性系统施加约束，使所有自然样本成为动力系统的渐近稳定平衡点。通过分析，这些约束可以通过转换为损失函数中的正则化项来实现。实验结果表明，ASODE提高了DNN的鲁棒性，并且优于现有的方法。
# 6. 20221018
### Title: Segment and Complete: Defending Object Detectors against Adversarial Patch Attacks with Robust Patch Detection
### Venue: CVPR 2022
1. Why? 目标检测器受到adversarial patch的严重威胁。
2. What? 本文提出Segment and Complete （SAC）方法来防御adversarial patch的攻击，经过实验验证了SAC的有效性和鲁棒性，并且提出了一个数据集APRICOT-Mask，该数据集提供了对adversarial patch像素级的标注。
3. How? 首先利用model分割adversarial patch，然后将patch去除，然后进行检测。
4. How much? 攻击成功率从7.97%下降到了2.17%。
5. What then? 把patch去除升级为对相应区域进行inpaint。
# 7. 20221028
### Title: Efficient and Effective Augmentation Strategy for Adversarial Training
### Venue: NIPS 2022
1. Why? Adversarial training是data-hungry的，而且Adversarial training无法像数据增广方法一样为模型（image classifier）提供很大的性能提升。
2. What? 本文首先分析了Adversarial training中strong data augmentations失败的原因，基于此提出了Diverse Augmentation based Joint Adversarial Training来进行更有效的Adversarial training。然后将DAJAT整合进入了两阶段的训练策略中，提出Ascending Constraint Adversarial Training (ACAT) 。通过实验验证了所提方法的性能。
3. How? 作者把训练阶段的数据增广看作一个domain generalization问题，分析了数据增广的影响和扮演的角色。
4. How much? 在ResNet-18 and WideResNet-34-10模型上，本文提出的方法在防御方面取得SOTA。
5. What then? 本文只关注effective，没有关注which augmentations are best suited for the same.



































