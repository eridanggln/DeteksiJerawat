🔍 AcneScan – Intelligent Acne Detection Tool
AcneScan is an intuitive web application developed with Flask (Python) that enables users to either upload an image or take a live photo using their device's camera. The system then identifies various types of acne automatically using a YOLOv5 deep learning detection model.

🗂️ Dataset Source – Roboflow Acne v3
The model was trained using the publicly available Acne v3 dataset from Roboflow:
https://universe.roboflow.com/skin-lj9yp/acne_v3
This dataset contains annotations for multiple acne categories:
- Blackhead
- Whitehead
- Papule
- Pustule
- Nodule

⚙️ Model Architecture – YOLOv5
The detection model leverages the YOLOv5 framework, sourced from Ultralytics’ official GitHub repository. It was trained for 30 epochs, resulting in accurate and efficient identification of acne conditions in facial images.
