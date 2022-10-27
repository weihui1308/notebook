# 1. 20221027
### Title: Towards A Robust Deepfake Detector: Common Artifact Deepfake Detection Model
### arXiv 202210 (MEGVII Technology)
目前deepfake detection技术可以分为两类：一类是利用binary labels训练一个二分类器，这种方式在cross-dataset时性能会降低；一类是学习一些various manipulated forgeries才存在的hand-crafted artifacts，这种方法存在取得比较好的性能提升，但仍是有限的，因为这种hand-crafted artifacts并不是一直存在。本文重新考虑二分类器，认为其跨数据集泛化能力不强是因为Implicit Identity Leakage，在此基础上提出了Common Artifact Deepfake Detection Model，取得SOTA。