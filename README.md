🔍 Aplikasi Deteksi Jerawat Otomatis

Aplikasi web yang dibangun menggunakan Flask (Python). Aplikasi ini memungkinkan pengguna untuk mengunggah gambar wajah atau mengambil foto langsung melalui kamera, kemudian secara otomatis mendeteksi berbagai jenis jerawat menggunakan model deteksi objek YOLOv5.

🗂️ Dataset – Acne v3 dari Roboflow

Model ini dilatih menggunakan dataset publik Acne v3 yang tersedia di Roboflow:
https://universe.roboflow.com/skin-lj9yp/acne_v3

Dataset ini mencakup berbagai label jenis jerawat berikut:
- Komedo Hitam (Blackhead)
- Komedo Putih (Whitehead)
- Papula (Papule)
- Pustula (Pustule)
- Nodul (Nodule)

⚙️ Model – YOLOv5

Model deteksi jerawat ini dibangun menggunakan arsitektur YOLOv5 https://github.com/ultralytics/yolov5. Proses pelatihan dilakukan selama 30 epoch dengan hasil precision sebesar 83,24% dan recall sebesar 82,43% menandakan bahwa model mampu mengenali objek jerawat secara akurat dan konsisten.  Nilai mAP@0.5 sebesar 86,81% menunjukkan kemampuan deteksi yang tinggi pada ambang batas IoU 0.5, sementara mAP@0.5:0.95 sebesar 44,88% mencerminkan performa model yang cukup baik di berbagai tingkat ketelitian.

