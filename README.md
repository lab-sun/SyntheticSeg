# SyntheticSeg
The official implementation of **Improving RGB-Thermal Semantic Scene Understanding with Synthetic Data Augmentation for Autonomous Driving**. ([IEEE RA-L](https://ieeexplore.ieee.org/document/10910182)).

## Introduction
We propose a data-driven method, SyntheticSeg, to enhance RGB-T semantic segmentation by generating a large-scale, high-fidelity synthetic dataset.

## Results
We provide pretrained weights obtained using our method by jointly training synthetic and real images on the MFNet dataset. These weights are applicable to methods utilizing different backbones on RTFNet, CMX, and CRM.

### RTFNet
| Backbone | mIOU | Weight |
|:---:|:---:|:---:|
| ResNet-50 | 56.1% | [RTF-50](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |
| ResNet-152 | 56.9% | [RTF-152](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |

### CMX
| Backbone | mIOU | Weight |
|:---:|:---:|:---:|
| MiT-B2 | 60.4% | [CMX-B2](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |
| MiT-B4 | 60.9% | [CMX-B4](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |

### CRM
| Backbone | mIOU | Weight |
|:---:|:---:|:---:|
| Swin-T | 59.9% | [CRM-T](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |
| Swin-S | 62.0% | [CRM-S](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |
| Swin-B | 62.1% | [CRM-B](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |
