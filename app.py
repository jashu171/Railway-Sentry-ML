import time
from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO  
from PIL import Image
import os

app = Flask(__name__, static_folder='static')

# Ensure the results folder exists
os.makedirs('static/results', exist_ok=True)

# Load the model
model = YOLO("best.pt")  # Replace with the correct path to your model

# Prediction function
def predict_railway(image_path, img_name):
    # Open the image and resize to the correct input size (640x640 for YOLO)
    with Image.open(image_path) as img:
        img = img.resize((640, 640))  # Resize to YOLO model input size

    # Define the path for saving the processed result
    img_path = os.path.join("static/results", img_name)

    # Perform prediction using the YOLO model
    results = model(image_path)

    # Convert the result to a PIL image and save it
    pil_image = Image.fromarray(results[0].plot())
    pil_image.save(img_path)

    return img_name  # Return the image name for use in the template

@app.route('/')
def HOME():
    return render_template("home.html")

@app.route('/predict_page')
def prediction_page():
    return render_template("prediction_page.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image
    img = request.files['r_image']
    
    # Ensure the uploaded image is saved with a unique filename (using timestamp)
    img_name = f"{int(time.time())}_{img.filename}"  # Add a timestamp to avoid name conflicts
    img_path = os.path.join("static/uploads", img_name)
    
    # Save the uploaded image
    img.save(img_path)

    # Get the result image path after prediction
    prediction = predict_railway(img_path, img_name)

    # Return the result page with the image path for displaying the result
    return render_template('prediction_result_page_.html', image=url_for('static', filename='results/' + prediction))

if __name__ == "__main__":
    app.run(debug=True)

