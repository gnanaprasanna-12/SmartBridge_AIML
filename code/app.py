from flask import Flask, render_template, request
from predict import predict_image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            label, confidence = predict_image(filepath)
            return render_template('index.html', label=label, confidence=confidence, image=file.filename)
    return render_template('index.html', label=None)

if __name__ == '__main__':
    app.run(debug=True)