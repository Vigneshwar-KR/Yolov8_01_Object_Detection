from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

results = model.train(data="C:/Vicky/Tu Braunschweig/Computer Vision/Projects/Yolo_01/Dataset/Mechanical Parts/data.yaml", epochs=1)

# we can also use cmd line
# yolo task = detect mode=train model=yolov8n.pt data= C:/Vicky/Tu Braunschweig/Computer Vision/Projects/Yolo_01/Dataset/Mechanical Parts/data.yaml epoch =25 imgsz=640 plots=True