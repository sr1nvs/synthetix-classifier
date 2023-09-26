import numpy as np
from PIL import Image
from keras.models import load_model
from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS



app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app)

model = load_model('models/cockandballtorture.h5')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    
    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'})
    
    image = Image.open(image)
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    
    predictions = model.predict(image)
    
    if predictions[0][0] > 0.5:
        classification = 'Harmless'
    else:
        classification = 'Harmful'
    
    return jsonify({'result': classification})

if __name__ == '__main__':
    app.run(debug=True)
