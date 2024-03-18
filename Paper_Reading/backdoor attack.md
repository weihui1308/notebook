# 1. 20220630
### Title: Dual-Key Multimodal Backdoors for Visual Question Answering
### Venue: CVPR 2022
本文首次提出对多模态任务的后门攻击，攻击任务是VQA model。攻击方法用两个trigger，一个是question trigger, 一个是visual trigger。只有当两个trigger都出现时，才会触发攻击，单独出现一个不会触发。本文提出了一个实验证明：越复杂的模型，面对后门攻击越脆弱。
# 2. 20221001
### Title: Untargeted Backdoor Watermark: Towards Harmless and Stealthy Dataset Copyright Protection
### Venue: NIPS 2022
本文探索了如何保护（开源）数据集的版权。作者发现，现有的数据集所有权验证可能会带来新的严重风险，这是由于现有数据集水印所用的后门攻击。基于这一观察，作者探索了有毒标签和干净标签设置下的非目标后门水印（UBW）范例，其异常模型行为并非确定性的。作者还研究了如何利用UBW进行无害和隐蔽的数据集所有权验证。在基准数据集上的实验验证了有效性及其对后门防御的抵御能力。
# 3. 20221018
### Title: Marksman Backdoor: Backdoor Attacks with Arbitrary Target Class
### Venue: NIPS 2022


# 4. 20230327
### Title: Influencer Backdoor Attack on Semantic Segmentation
### Venue: ArXiv 202303
本文研究了语义分割任务上的后门攻击，是首次这样做的工作。作者展示了，当图像中加入trigger后，语义分割模型就无法正确识别到车辆，而其它类别的分割结果还在正常的。
# 6. 20230329
### Title: Blind Backdoors in Deep Learning Models
### Venue: USENIX Security 2021
本文提出一种blind backdoor，不修改input，也不需要对model进行query。这种backdoor attacks通过code poisoning来实现。该方法通过向code注入攻击的代码，在不影响model性能的同时，可以操控model进行特殊的预测，例如使model从计算照片中的人脸数量变为隐蔽地识别特定的个人。代码开源。
# 7. 20230329
### Title: Randomized Channel Shuffling: Minimal-Overhead Backdoor Attack Detection without Clean Datasets
### Venue: NIPS 2022

# 8. 20230329
### Title: BadPrompt: Backdoor Attacks on Continuous Prompts 
### Venue: NIPS 2022

# 9. 20230329
### Title: Finding Naturally Occurring Physical Backdoors in Image Datasets
### Venue: NIPS 2022


# 10. 20231023
### Title: MM-BD: Post-Training Detection of Backdoor Attacks with Arbitrary Backdoor Pattern Types Using a Maximum Margin Statistic
### Venue: 2024 IEEE SP

# 11. 20231207
### Title: Synthesizing Physical Backdoor Datasets: An Automated Framework Leveraging Deep Generative Models
### Venue: ArXiv 202312


# 12. 20240318
### Title: Towards Practical Deployment-Stage Backdoor Attack on Deep Neural Networks
### Venue: CVPR 2022
























