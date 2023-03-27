# 1. 20220630
### Title: Dual-Key Multimodal Backdoors for Visual Question Answering
### Venue: CVPR 2022
本文首次提出对多模态任务的后门攻击，攻击任务是VQA model。攻击方法用两个trigger，一个是question trigger, 一个是visual trigger。只有当两个trigger都出现时，才会触发攻击，单独出现一个不会触发。本文提出了一个实验证明：越复杂的模型，面对后门攻击越脆弱。
# 2. 20221001
### Title: Untargeted Backdoor Watermark: Towards Harmless and Stealthy Dataset Copyright Protection
### Venue: NIPS 2022


# 3. 20221018
### Title: Marksman Backdoor: Backdoor Attacks with Arbitrary Target Class
### Venue: NIPS 2022


# 4. 20230327
### Title: Influencer Backdoor Attack on Semantic Segmentation
### Venue: ArXiv 202303


# 5. 20230327
### Title: T-SEA: Transfer-based Self-Ensemble Attack on Object Detection
### Venue: CVPR 2023
基于迁移的黑盒攻击方式由于不需要获取目标模型的任何信息，更有利于真实场景的攻击，但成功率也往往更低。许多基于迁移的黑盒攻击依靠多模型集成方式来提高攻击的迁移性，也即，在训练对抗样本阶段，通过集成多个不同的白盒模型，以期训练好的对抗样本能在新的黑盒模型上表现出更强的攻击能力。但这种方式往往需要消耗大量训练时间和资源，同时，要获取同一任务的多个模型，在现实应用中也可能具有一定的实现难度。作者利用对抗补丁来对目标检测模型进行攻击，将对抗补丁贴到检测目标上，使得检测框消失。为了实现在单个白盒模型上训练的对抗补丁的迁移性，本文工作1.发现改变两个简单的训练设置即可对baseline的性能实现一定的提高；2.提出使用自集成（Self-ensemble）策略来充分提高对抗补丁的迁移性。

































