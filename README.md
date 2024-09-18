# YOLO with Polygon Point Check:

This repository demonstrates the use of the YOLO object detection model, combined with a utility to check if a point lies within a given polygon.

## Files

- `requirements.txt`: Required Python libraries.
- `polygon_utils.py`: Contains the polygon and a function to check if a point lies within the polygon.
- `yolo_model.py`: Contains the YOLO model initialization function.
- `main.py`: The main script that runs the YOLO model and performs a polygon point check.

## Setup

1. Install the required libraries:
    ```
    pip install -r requirements.txt
    ```

2. Run the main script:
    ```
    python main.py
    ```

## Dependencies

- YOLO model from the [Ultralytics](https://github.com/ultralytics/ultralytics) library.
- OpenCV for image handling.
- NumPy for numerical operations.
