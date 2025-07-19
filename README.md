# 🚂 Railway Track Object Detection Using YOLO

A comprehensive web application for automated detection and analysis of objects and features on railway tracks using state-of-the-art YOLO V11 deep learning technology.

## 🔍 Overview

This project leverages the power of YOLO (You Only Look Once) object detection to identify and annotate various objects and features on railway tracks. Built with Flask, it provides an intuitive web interface for uploading railway images and receiving real-time detection results with visual annotations.

### Key Technologies

- **Deep Learning**: Ultralytics YOLO
- **Backend**: Flask (Python)
- **Frontend**: HTML/CSS with Jinja2 templating
- **Computer Vision**: OpenCV, PIL

## ✨ Features

- 🖼️ **User-Friendly Interface**: Clean, responsive web UI for seamless interaction
- 🎯 **Real-Time Detection**: Instant object detection and annotation on uploaded images
- 📊 **Comprehensive Analysis**: Detects multiple railway track objects and features
- 📁 **Organized Storage**: Automatic management of uploads and results
- 🔄 **Batch Processing**: Support for multiple image uploads
- 📱 **Cross-Platform**: Works on desktop and mobile browsers

## 📂 Project Structure

```
railway-track-detection/
│
├── 📄 app.py                     # Main Flask application
├── 🤖 best.pt                    # Trained YOLO model weights
├── 📋 requirements.txt           # Python dependencies
├── 📖 README.md                  # Project documentation
│
├── 📁 static/
│   ├── 📁 uploads/               # User uploaded images
│   └── 📁 results/               # Detection results with annotations
│
├── 📁 templates/
│   ├── 🏠 home.html              # Landing page
│   ├── 📤 prediction_page.html    # Image upload interface
│   └── 📊 prediction_result_page_.html  # Results display
│
└── 📁 Output images/             # Sample detection results and demos
```

## 🚀 Installation

### Prerequisites
- Python 3.11+
- pip package manager

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/railway-track-detection.git
   cd railway-track-detection
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Model File**
   - Ensure `best.pt` (YOLO weights) is in the project root
   - If missing, place your trained model file here

5. **Create Required Directories**
   ```bash
   mkdir -p static/uploads static/results
   ```

6. **Launch Application**
   ```bash
   python app.py
   ```

7. **Access the Application**
   - Open your browser and navigate to `http://127.0.0.1:5000/`

## 🎮 Usage

### Step-by-Step Guide

1. **Home Page**: Visit the landing page for project overview
2. **Upload Image**: Navigate to the prediction page and select a railway track image
3. **Process**: Click submit to run YOLO detection
4. **View Results**: Examine the annotated image with detected objects highlighted
5. **History**: Access previously processed images from the results directory

### Supported Image Formats
- JPEG/JPG
- PNG
- BMP
- TIFF

## 🤖 Model Information

- **Architecture**: YOLOv9/YOLOv11 (Ultralytics)
- **Training Data**: Custom railway track dataset
- **Model File**: `best.pt` (PyTorch format)
- **Input Size**: Automatically resized for optimal performance
- **Output**: Bounding boxes with confidence scores and class labels

### Detectable Objects & Classes

Based on the detection results shown above, the system can identify:

**Primary Detection Classes:**
- 🏷️ **worker** - Railway maintenance personnel and staff members
- 🏷️ **person** - General human detection for safety monitoring  
- 🏷️ **vest** - High-visibility safety vests and protective clothing
- 🏷️ **helmet** - Safety helmets and protective headgear

**Detection Features:**
- **High Accuracy**: Confidence scores typically range from 0.62 to 0.87
- **Multi-object Recognition**: Can detect multiple objects simultaneously
- **Real-time Processing**: Instant detection with bounding box annotations
- **Safety Focus**: Specialized in railway safety equipment and personnel
- **Surveillance Integration**: Compatible with CCTV and monitoring systems

## 🖼️ Gallery

### Detection Results & Application Interface

**Main Application Interface**
The web application provides a clean, user-friendly interface for uploading and processing railway images:

![Application Interface](Output%20images/web_interface_demo.png)
*Upload interface with drag-and-drop functionality*

### Live Detection Examples

**Worker Detection with High Accuracy**
The system accurately identifies railway workers with confidence scores:

![Worker Detection 1](Output%20images/prediction_results_1.png)
*Multiple workers detected with 0.79 and 0.83 confidence scores*

**Multi-object Detection in Station Environment**
Simultaneous detection of workers and safety equipment:

![Station Detection](Output%20images/prediction_results_2.png)
*Workers (0.84, 0.83 confidence) and safety vests (0.70, 0.62 confidence) detected*

**Safety Equipment Recognition**
Detection of safety helmets and protective gear:

![Safety Equipment](Output%20images/prediction_results_3.png)
*Safety vest (0.70 confidence) and helmet (0.62 confidence) identification*

**Track Surveillance Detection**
Real-time monitoring from surveillance cameras:

![Surveillance Detection](Output%20images/surveillance_detection.png)
*Person detection on railway tracks (0.87 confidence) with timestamp*

**Application in Action**
Live demonstration of the web interface showing detection results:

![Live Demo](Output%20images/application_demo.png)
*Real-time processing and result display*

### Detection Capabilities

The YOLO model successfully identifies:
- ✅ **Workers** - Railway maintenance personnel and staff
- ✅ **Safety Equipment** - Helmets, vests, protective gear  
- ✅ **People** - General person detection for safety monitoring
- ✅ **Railway Infrastructure** - Tracks, stations, equipment
- ✅ **Surveillance Integration** - Camera feed processing with timestamps

## ⚙️ Customization

### Using Your Own Model
1. Replace `best.pt` with your trained YOLO weights
2. Ensure the model is compatible with Ultralytics YOLO format
3. Update class names in `app.py` if different from the current model

### UI Customization
- Modify HTML templates in `templates/` directory
- Add custom CSS styles for enhanced appearance
- Update Flask routes in `app.py` for additional functionality

### Advanced Configuration
```python
# Example model configuration in app.py
model = YOLO('best.pt')
model.conf = 0.5  # Confidence threshold
model.iou = 0.45  # IoU threshold
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Ultralytics YOLO](https://ultralytics.com/) - For the excellent YOLO implementation
- [Flask](https://flask.palletsprojects.com/) - For the web framework
- [OpenCV](https://opencv.org/) - For computer vision utilities
- Railway industry professionals who provided domain expertise
- Open source community contributors

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-username/railway-track-detection/issues) page
2. Create a new issue with detailed information
3. Contact the development team

**Made with ❤️ for railway safety and automation**

output:
![image](https://github.com/user-attachments/assets/9a0d000a-01e7-455c-95e3-b64c248458be)


### Sample Detection Results

**Railway Track Analysis**
![Railway Track View](static/uploads/photo-1719153034939-788450b7dc57.jpg)

**Construction Site Monitoring**
![Workers on Track](static/uploads/istockphoto-181858921-1024x1024.jpg)

**Infrastructure Installation**
![Track Construction](static/uploads/istockphoto-1127090826-640x640.jpg)

**Safety Inspection**
![Worker Inspecting](static/uploads/istockphoto-1269800321-612x612.jpg)

<details>
<summary>View More Examples</summary>

**Construction Activity**
![Construction Site](static/uploads/1733388539_download11.jpg)

**Monitoring Operations**
![Activity Monitors](static/uploads/1734885805_download11.jpg)

**Engineering Inspection**
![Engineer Checking Rails](static/uploads/1735209973_1894.jpg)

**Field Operations**
![Engineer on Site](static/uploads/1732155464_photo.jpg)

</details>

## ⚙️ Customization

### Using Your Own Model
1. Replace `best.pt` with your trained YOLO weights
2. Ensure the model is compatible with Ultralytics YOLO format
3. Update class names in `app.py` if different from the current model

### UI Customization
- Modify HTML templates in `templates/` directory
- Add custom CSS styles for enhanced appearance
- Update Flask routes in `app.py` for additional functionality

### Advanced Configuration
```python
# Example model configuration in app.py
model = YOLO_V11('best.pt')
model.conf = 0.5  # Confidence threshold
model.iou = 0.45  # IoU threshold
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Ultralytics YOLO](https://ultralytics.com/) - For the excellent YOLO implementation
- [Flask](https://flask.palletsprojects.com/) - For the web framework
- [OpenCV](https://opencv.org/) - For computer vision utilities
- Railway industry professionals who provided domain expertise
- Open source community contributors

---

## 📞 Contact Details

You can reach me through the following channels:

- **Email:** jashwanthboddupally@gmail.com  
- **Phone:** +91 9010767269  
- **Portfolio:** [https://jashu171.github.io/portfolio/](https://jashu171.github.io/portfolio/)  
- **LinkedIn:** [Jashwanth Boddupally](https://www.linkedin.com/in/jashwanth-boddupally-64068b289/)  
- **GitHub:** [jashu171](https://github.com/jashu171)
  
**Made with ❤️ for railway safety and automation**
