# Object Detection in Low-Light Environments  

This repository presents a comprehensive approach to tackling the challenge of detecting objects in low-light conditions. The project integrates advanced image enhancement using MIRNet with state-of-the-art object detection via YOLO v8n, achieving significant improvements in detection accuracy and reliability.  

## Abstract  

Object detection in low-light images is hindered by reduced visibility and increased noise levels. By leveraging MIRNet for image enhancement and YOLO v8n for object detection, this project achieves a **mean average precision (mAP50) of 0.702** on the ExDark Image Dataset, the largest publicly available dataset of low-light images.  

## Dataset  

The ExDark Image Dataset contains 7363 low-light images across 12 object classes, annotated for object detection tasks. You can download the dataset from the official repository:  
[ExDark Dataset GitHub](https://github.com/cs-chan/Exclusively-Dark-Image-Dataset).  

![image](https://github.com/user-attachments/assets/b6287541-b420-4b6b-b83c-c2db6d464237)


## Features  
- **MIRNet (Image Enhancement)**: Enhances visibility and reduces noise by leveraging multi-scale residual blocks for spatial and contextual accuracy.  
- **YOLO v8n (Object Detection)**: Efficiently detects objects with multi-scale recognition, CSPDarknet-AA architecture, and advanced loss functions.  
- **ExDark Image Dataset**: Comprising 7363 images across 12 object classes, it provides diverse low-light conditions for robust training and testing.  
- **GPU Optimization**: Utilizes NVIDIA GPUs for smooth and efficient model training.  

## Workflow  

1. **Data Preprocessing**  
   - Adjusted ExDark dataset annotations for YOLO compatibility (e.g., class label conversion, bounding box normalization).  
   - Prepared images for MIRNet with resizing, RGB conversion, and normalization.  

2. **Image Enhancement with MIRNet**  
   - Enhanced low-light images using MIRNet, improving clarity and visibility.  

3. **Object Detection with YOLO v8n**  
   - Preprocessed enhanced images for YOLO v8n.  
   - Trained the model with a batch size of 32 for 50 epochs on NVIDIA GPUs.  

4. **Evaluation**  
   - Achieved mAP50 of 0.702 across all classes.  
   - Detailed performance analysis with precision-recall curves, confusion matrices, and mAP metrics.  

## Results  

The methodology yielded excellent detection performance across diverse object classes. Notably:  
- **mAP50**: 0.702  
- **Best-performing Class**: "Bus" with mAP50 of 0.904.

![image](https://github.com/user-attachments/assets/773d1d4a-b051-4863-90fb-c43399de97f6)

![image](https://github.com/user-attachments/assets/6b214c34-d019-4c38-a411-eda5e547f830)

## Key Metrics  

- **Precision-Recall Curve**: Highlights model efficiency in detecting objects across varying confidence thresholds.  
- **Confusion Matrix**: Demonstrates class-wise detection accuracy.  
- **F1 Score**: Provides a balanced assessment of precision and recall.  

## Requirements  

- Python 3.8+  
- PyTorch  
- NVIDIA GPU with CUDA support  
