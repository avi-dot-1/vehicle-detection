from ultralytics import YOLO

def initialize_model():
    # Initializing YOLO model:
    model = YOLO('yolov8n.pt')
    return model
