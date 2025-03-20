# SyntheticSeg
The official implementation of **Improving RGB-Thermal Semantic Scene Understanding with Synthetic Data Augmentation for Autonomous Driving**. ([IEEE RA-L](https://ieeexplore.ieee.org/document/10910182)).

## Introduction
We propose a data-driven method, SyntheticSeg, to enhance RGB-T semantic segmentation by generating a large-scale, high-fidelity synthetic dataset.

## Results
We provide pretrained weights obtained using our method by jointly training synthetic and real images on the MFNet dataset. These weights are applicable to methods utilizing different backbones on [RTFNet](https://github.com/yuxiangsun/RTFNet), [CMX](https://github.com/huaaaliu/RGBX_Semantic_Segmentation), and [CRM](https://github.com/UkcheolShin/CRM_RGBTSeg).

### RTFNet
| Backbone | mIOU | Improvement | Weight |
|:---:|:---:|:---:|:---:|
| ResNet-50 | 56.1% | 4.4% | [RTF-50](https://drive.google.com/file/d/1YBqEch0ofjymC_SN7HVIr6zNcfSYugso/view?usp=drive_link) |
| ResNet-152 | 56.9% | 3.7% | [RTF-152](https://drive.google.com/file/d/1sQDAxNSWD9h22xDcxFqh750-xBQjZ4_o/view?usp=drive_link) |

### CMX
| Backbone | mIOU | Improvement | Weight |
|:---:|:---:|:---:|:---:|
| MiT-B2 | 60.4% | 2.2% | [CMX-B2](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) |
| MiT-B4 | 60.9% | 1.2% | [CMX-B4](https://drive.google.com/file/d/1NrvYwmstv_zHOiAx4MQvDUFcm_aS3Gjs/view?usp=drive_link) |

### CRM
| Backbone | mIOU | Improvement | Weight |
|:---:|:---:|:---:|:---:|
| Swin-T | 59.9% | 0.8% | [CRM-T](https://drive.google.com/file/d/1l7AZNK15bVyI0uLqwL41Cv4jBk40iFAp/view?usp=drive_link) |
| Swin-S | 62.0% | 0.8% | [CRM-S](https://drive.google.com/file/d/1JulSZmgM_pHLoLriemx4YagXL2H0jAps/view?usp=drive_link) |
| Swin-B | 62.1% | 0.7% | [CRM-B](https://drive.google.com/file/d/1f1uwYDHAe9EfoWu3DRQ0iIcdDUINorub/view?usp=drive_link) |

## Citation
If you use our work in your research, please cite:

```    
    @article{li2025syntheticseg,
      title={Improving RGB-Thermal Semantic Scene Understanding with Synthetic Data Augmentation for Autonomous Driving},
      author={Li, Haotian and Chu, Henry K and Sun, Yuxiang},
      journal={IEEE Robotics and Automation Letters},
      year={2025},
      publisher={IEEE}
    }
```
