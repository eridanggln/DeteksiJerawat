---


# Automatic Acne Detection Application 🔍💻

A web application built using Flask (Python). This app allows users to upload a facial image or capture a photo directly using the camera, then automatically detects various types of acne using the YOLOv5 object detection model.

## Dataset – Acne v3 from Roboflow 🗂️

The model was trained using the public Acne v3 dataset available on Roboflow:
**https://universe.roboflow.com/skin-lj9yp/acne_v3**

## The dataset includes several acne-type labels:
* **Blackhead**
* **Whitehead**
* **Papule**
* **Pustule**
* **Nodule**

## Model – YOLOv5 ⚙️
The acne detection model was developed using the YOLOv5 architecture:
**https://github.com/ultralytics/yolov5**
.

**Training was conducted for 30 epochs, producing a precision of 83.24% and recall of 82.43%, indicating that the model can accurately and consistently identify acne.**

## Screenshots 📸


---
