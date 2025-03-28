# SyntheticSeg
The official implementation of **Improving RGB-Thermal Semantic Scene Understanding with Synthetic Data Augmentation for Autonomous Driving**. ([IEEE RA-L](https://ieeexplore.ieee.org/document/10910182)).

## Introduction
We propose a data-driven method, SyntheticSeg, to enhance RGB-T semantic segmentation by generating a large-scale, high-fidelity synthetic dataset.

## Synthetic Dataset
You can download our synthetic dataset directly [here](http://labsun.mne.cityu.edu.hk/downloads/2025_ral_syntheticseg/SyntheticSeg_datasets.zip), or you can train and infer your own synthetic dataset through [FreestyleNet](https://github.com/essunny310/FreestyleNet).
Then, place them in 'datasets' folder in the following structure:

```shell
<datasets>
|-- <MFdataset_seed>
    |-- <total_rgb>
    |-- <total_thermal>
    |-- <total_label>
```

## Prepare Sampled Synthetic Dataset
* We utilize the checkpoint of our [Temporal-Consistent-RGBT-Segmentation](https://github.com/lab-sun/Temporal-Consistent-RGBT-Segmentation) repository to compute the mean loss for each class. Please refer to its guidelines to set up the environment and prepare the pretrained backbone. Then, download our checkpoint [here](https://drive.google.com/file/d/1ZxI-aGzot4WXw5TqxAibTEmlgZ7gSCYE/view?usp=sharing) and place it in 'ckpt' folder in the following structure:

```shell
<ckpt>
|-- <ckpt.pth>
```

* Execute [preprocess.py](./preprocess.py) to obtain the pixel ratio and mean loss for each class.

* Execute [resample.py](./resample.py) to create a sampled synthetic dataset by adjusting the maximum sampling number.

## Results
We provide pretrained weights obtained using our method by jointly training synthetic and real images on the MFNet dataset. These weights are applicable to methods utilizing different backbones on [RTFNet](https://github.com/yuxiangsun/RTFNet), [CMX](https://github.com/huaaaliu/RGBX_Semantic_Segmentation), and [CRM](https://github.com/UkcheolShin/CRM_RGBTSeg).

### RTFNet
| Backbone | mIOU | Improvement | Weight |
|:---:|:---:|:---:|:---:|
| ResNet-50 | 56.1% | 4.4% | [Google Drive](https://drive.google.com/file/d/1YBqEch0ofjymC_SN7HVIr6zNcfSYugso/view?usp=drive_link) or [NAS](http://nas.labsun.org/downloads/2025_ral_syntheticseg/checkpoints/) |
| ResNet-152 | 56.9% | 3.7% | [Google Drive](https://drive.google.com/file/d/1sQDAxNSWD9h22xDcxFqh750-xBQjZ4_o/view?usp=drive_link) or [NAS](http://nas.labsun.org/downloads/2025_ral_syntheticseg/checkpoints/) |

### CMX
| Backbone | mIOU | Improvement | Weight |
|:---:|:---:|:---:|:---:|
| MiT-B2 | 60.4% | 2.2% | [Google Drive](https://drive.google.com/file/d/15TBB1EcMxCG5MqmZ8-H9LGmdY0LZdo97/view?usp=drive_link) or [NAS](http://nas.labsun.org/downloads/2025_ral_syntheticseg/checkpoints/) |
| MiT-B4 | 60.9% | 1.2% | [Google Drive](https://drive.google.com/file/d/1NrvYwmstv_zHOiAx4MQvDUFcm_aS3Gjs/view?usp=drive_link) or [NAS](http://nas.labsun.org/downloads/2025_ral_syntheticseg/checkpoints/) |

### CRM
| Backbone | mIOU | Improvement | Weight |
|:---:|:---:|:---:|:---:|
| Swin-T | 59.9% | 0.8% | [Google Drive](https://drive.google.com/file/d/1l7AZNK15bVyI0uLqwL41Cv4jBk40iFAp/view?usp=drive_link) or [NAS](http://nas.labsun.org/downloads/2025_ral_syntheticseg/checkpoints/) |
| Swin-S | 62.0% | 0.8% | [Google Drive](https://drive.google.com/file/d/1JulSZmgM_pHLoLriemx4YagXL2H0jAps/view?usp=drive_link) or [NAS](http://nas.labsun.org/downloads/2025_ral_syntheticseg/checkpoints/) |
| Swin-B | 62.1% | 0.7% | [Google Drive](https://drive.google.com/file/d/1f1uwYDHAe9EfoWu3DRQ0iIcdDUINorub/view?usp=drive_link) or [NAS](http://nas.labsun.org/downloads/2025_ral_syntheticseg/checkpoints/) |

## Citation
If you use our work in your research, please cite:

```    
@ARTICLE{li2025improving,
  author={Haotian Li and Henry K. Chu and Yuxiang Sun},
  journal={IEEE Robotics and Automation Letters}, 
  title={Improving RGB-Thermal Semantic Scene Understanding With Synthetic Data Augmentation for Autonomous Driving}, 
  year={2025},
  volume={10},
  number={5},
  pages={4452-4459},
  doi={10.1109/LRA.2025.3548399}}
```
