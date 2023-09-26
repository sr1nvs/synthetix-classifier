import h5py
import numpy as np
from PIL import Image
from keras.models import load_model

model = load_model('models\cockandballtorture.h5')

image = Image.open('image.jpg') # Load the image
image = image.resize((256,256))
image = np.array(image) / 255.0  # Normalize pixel values to [0, 1]
image = np.expand_dims(image, axis=0)
predictions = model.predict(image)

if predictions[0] > 0.5:
    classification = 'harmless'
else:
    classification = 'harmful'

print(f"The image is classified as {classification}")