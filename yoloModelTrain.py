from ultralytics import YOLO

model = YOLO('yolov8n.pt')
 
results = model.train(data='/storage/research/data/dgxstu03/Aditya/dgxserver/data.yaml', imgsz=640, epochs=50, batch=32)

path_best_weights="/storage/research/data/dgxstu03/Aditya/dgxserver/runs/detect/train22/weights/best.pt"

model = YOLO(path_best_weights) 

metrics = model.val()

print(f"Mean Average Precision @.5:.95 : {metrics.box.map}")    
print(f"Mean Average Precision @ .50   : {metrics.box.map50}") 
print(f"Mean Average Precision @ .70   : {metrics.box.map75}")
