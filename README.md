# Railway Track Object Detection Using YOLO

## Project Description

This project provides a web application for detecting objects and features on **railway tracks** using a custom-trained **YOLO** deep learning model. Users can upload railway images, and YOLO will automatically detect and annotate relevant track objects. The app is built with Flask and uses the Ultralytics YOLO API for processing.

---

## Features

- **User-friendly web interface** for image upload and viewing results.
- **Automated railway track object detection** using the latest YOLO model.
- **Real-time display** of annotated results.
- **Organized upload & results history**.

---

## Folder Structure

  project/
├── app.py                  # Flask web server and inference code
├── best.pt                 # Trained YOLO model weights
├── static/
│   ├── uploads/            # Stores uploaded images
│   └── results/            # Stores prediction results
├── templates/
│   ├── home.html
│   ├── prediction_page.html
│   └── prediction_result_page_.html
└── README.md







output:
![image](https://github.com/user-attachments/assets/9a0d000a-01e7-455c-95e3-b64c248458be)
