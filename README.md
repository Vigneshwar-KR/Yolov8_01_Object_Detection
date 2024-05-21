# Yolov8_01_Object_Detection

#**Object detection model used YOLOv8**

![YOLOv8 Integrations Banner](https://github.com/ultralytics/assets/raw/main/yolov8/banner-integrations.png)

## Ultralytics YOLOv8 provides these following modes:
1.   Train
2.   Val
3.   Predict
4.   Track
5.   Benchmark

## Ultralytics YOLOv8 supports these following computer vision tasks:
1.   Detection
2.   Segmentation
3.   Classification
4.   Oriented object detection
5.   Keypoints detection

# **Problem task**
Build a object detection model to localize joints, nuts, bolts and other system components. End goal is to classify the parts based on the given label and handled in the coordinate system of the given system. In order to do that first we need to detect the parts and classify them.

For now i have selected **4 basic class labels**:

    ['Bearing', 'Bolt', 'Gear', 'Nut']
and it will be increased after improving the dataset and the model.

I tried using custom dataset which i prepared from my part time as Hiwi. But as the number of sample available was very low. Therefore, I used this as my test dataset for inference. In order to train the model, i used another custom dataset with 2250 images.

The split is given 1800-225-225
