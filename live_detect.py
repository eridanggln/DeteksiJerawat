# live_detect.py

import torch
import cv2
import pathlib
pathlib.PosixPath = pathlib.WindowsPath

# Load model hasil training
model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp3/weights/best.pt', source='local')  # Ganti path jika perlu
cap = cv2.VideoCapture(0)  # 0 = default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # 🔄 Hilangkan efek mirror di sini

    results = model(frame)
    results.render()

    cv2.imshow("Live Deteksi Jerawat", results.ims[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
