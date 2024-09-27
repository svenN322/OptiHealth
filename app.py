# importing required libraries
from tensorflow import keras
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from app_helper import *


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def inicio():
    return render_template("home.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route('/results', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

        # save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static', 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # get the prediction
        predicted_class_label = get_classes(file_path)
        # predicted_class_label = 'Enfermedad detectada: ' + predicted_class_label

    return render_template("results.html", predictions=predicted_class_label,display_image=secure_filename(f.filename))


if __name__ == "__main__":
    app.run()