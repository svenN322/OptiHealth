from tensorflow import keras
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from PIL import Image

# Importar funciones y bibliotecas del modelo
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
from tensorflow.keras.models import load_model # type: ignore
import numpy as np

# Nombres de las clases
class_labels = ['BLEFARITIS','CATARATAS','CHALAZIÓN','CONJUTIVITIS','MELANOMA_OCULAR','NORMALES','PTERIGIÓN','RETINOBLASTOMA']
# Carga el modelo pre-entrenado
model_path = 'models/ojitoschiquititos.h5'

def get_classes(file_path):
    # Carga el modelo pre-entrenado
    model = load_model(model_path)

    # Preparar imagen para predicción
    img = image.load_img(file_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # Realizar predicción
    prediction = model.predict(x)
    predicted_class_index = np.argmax(prediction[0])
    predicted_class = class_labels[predicted_class_index]
    #probability = np.max(predictions[0])

    return predicted_class