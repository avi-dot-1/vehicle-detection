import cv2
import numpy as np
from polygon_utils import POLYGON, point_in_polygon
from yolo_model import initialize_model
import matplotlib.pyplot as plt

def main():
    # Initializing the YOLO model
    model = initialize_model()

    # Example of detecting whether a point is within the polygon
    point = (1500, 1000)
    if point_in_polygon(point, POLYGON):
        print(f"Point {point} is inside the polygon.")
    else:
        print(f"Point {point} is outside the polygon.")

if __name__ == "__main__":
    main()
