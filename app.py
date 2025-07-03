import os, cv2, torch, uuid, pathlib, base64
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Perbaikan path Windows
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/result'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Load YOLOv5 model
model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp4/weights/best.pt', source='local')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    def generate_frames():
        cap = cv2.VideoCapture(0)
        while True:
            success, frame = cap.read()
            if not success:
                break

            # BGR → RGB untuk deteksi
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(rgb_frame)
            results.render()

            # Ambil hasil RGB → kembali ke BGR untuk ditampilkan di OpenCV stream
            rendered = results.ims[0]
            bgr_result = cv2.cvtColor(rendered, cv2.COLOR_RGB2BGR)

            _, buffer = cv2.imencode('.jpg', bgr_result)
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

    return app.response_class(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detect', methods=['POST'])
def detect_upload():
    file = request.files.get('image')
    if file and file.filename:
        filename = f"{uuid.uuid4()}.jpg"
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)

        # BGR → RGB
        img_bgr = cv2.imread(upload_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        results = model(img_rgb)
        results.render()
        result_rgb = results.ims[0]

        # RGB → BGR untuk disimpan oleh OpenCV
        result_bgr = cv2.cvtColor(result_rgb, cv2.COLOR_RGB2BGR)
        result_path = os.path.join(app.config['RESULT_FOLDER'], filename)
        cv2.imwrite(result_path, result_bgr)

        return render_template('index.html', result_img=f'result/{filename}')

    return redirect(url_for('index'))

@app.route('/capture', methods=['POST'])
def capture_from_live():
    data_url = request.json.get('imageData')
    if not data_url:
        return jsonify({'error': 'No image data'}), 400

    # Decode base64 menjadi gambar BGR
    header, encoded = data_url.split(',', 1)
    img_data = base64.b64decode(encoded)
    np_arr = np.frombuffer(img_data, np.uint8)
    img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # BGR → RGB untuk deteksi
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)
    results.render()
    result_rgb = results.ims[0]

    # RGB → BGR untuk simpan ke file
    result_bgr = cv2.cvtColor(result_rgb, cv2.COLOR_RGB2BGR)
    filename = f"{uuid.uuid4()}.jpg"
    result_path = os.path.join(app.config['RESULT_FOLDER'], filename)
    cv2.imwrite(result_path, result_bgr)

    return jsonify({'result_img': f'result/{filename}'})

if __name__ == '__main__':
    app.run(debug=True)
