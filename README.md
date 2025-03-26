# VisDrone Object Detection

This project implements object detection on the VisDrone dataset using YOLOv10n, focusing on detecting people and vehicles in drone imagery.

## 🎯 Project Overview

The project uses the VisDrone dataset, which is a large-scale benchmark for visual object detection in drone imagery. We've implemented a simplified version focusing on two main object categories:
- People (combined from pedestrians and people classes)
- Vehicles (combined from cars, vans, trucks, buses, and motorcycles)

## 📊 Dataset

### Original VisDrone Dataset Size
- Train: 6,471 images
- Validation: 548 images
- Test-dev: 1,610 images
- Test(challenge): 1,580 images

### Reduced Dataset Size (for faster experimentation)
- Train: 500 images
- Validation: 100 images
- Test-dev: 100 images

### Class Mapping
Original classes have been simplified into two main categories:

| New Class | Original Classes |
|-----------|-----------------|
| Person (0) | pedestrian (0), people (1) |
| Vehicle (1) | car (3), van (4), truck (5), bus (8), motor (9) |

*Note: bicycle (2), tricycle (6), and awning-tricycle (7) classes are ignored in this implementation.*

## 🛠️ Tools & Technologies

- **Deep Learning Framework**: YOLOv10n
- **Programming Language**: Python
- **Key Libraries**:
  - PIL (Python Imaging Library)
  - tqdm (Progress bar)
  - os, pathlib (File operations)
  - random, shutil (Dataset reduction)

## 📁 Project Structure

```
visdrone-object-detection/
├── data/
│   └── VisDrone/
│       ├── VisDrone2019-DET-train/
│       ├── VisDrone2019-DET-val/
│       └── VisDrone2019-DET-test-dev/
├── preprocess/
│   ├── annotation_handler.py
│   └── data_reducer.py
└── notebooks/
    └── VisDrone_yolov10n_custom_label_e100_bs32.ipynb
```

## 🔧 Data Preprocessing

### 1. Dataset Reduction
The `data_reducer.py` script randomly samples a smaller subset of the original dataset while maintaining the corresponding annotations.

### 2. Annotation Conversion
The `annotation_handler.py` script converts VisDrone annotations to YOLO format and implements the class merging strategy:
- Converts box coordinates to YOLO format (normalized xywh)
- Merges multiple classes into two main categories
- Filters out ignored regions and unnecessary classes

## 🚀 Model Training

### Training Configuration
```yaml
path: /content/data  # dataset root dir
train: VisDrone2019-DET-train/images
val: VisDrone2019-DET-val/images
test: VisDrone2019-DET-test-dev/images

names:
  0: person
  1: vehicle
```

### Training Experiments
1. Initial Run:
   - Model: YOLOv10n
   - Epochs: 10
   - Batch Size: 16

2. Extended Training:
   - Model: YOLOv10n
   - Epochs: 100
   - Batch Size: 32

## 📚 References

1. VisDrone Dataset: [Vision Meets Drones: A Challenge](https://arxiv.org/abs/1804.07437)
2. PaddleDetection Implementation: [PaddleDetection GitHub](https://github.com/PaddlePaddle/PaddleDetection/tree/release/2.7)

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements.

## 📄 License

[Add your license information here]

@article{zhu2021detection,
  title={Detection and tracking meet drones challenge},
  author={Zhu, Pengfei and Wen, Longyin and Du, Dawei and Bian, Xiao and Fan, Heng and Hu, Qinghua and Ling, Haibin},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume={44},
  number={11},
  pages={7380--7399},
  year={2021},
  publisher={IEEE}
}