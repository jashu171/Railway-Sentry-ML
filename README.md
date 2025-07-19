# 🚂 Railway Track Object Detection Using YOLOv11

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![YOLO](https://img.shields.io/badge/YOLO-v11-red.svg)](https://ultralytics.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Developed a cutting-edge web application for real-time detection and analysis of objects and personnel on railway tracks, leveraging YOLOv11 deep learning technology. The system significantly enhances railway safety by enabling automated monitoring of infrastructure, worker activity, and safety compliance through advanced object detection and analytics.

![Railway Detection Demo](https://github.com/user-attachments/assets/9a0d000a-01e7-455c-95e3-b64c248458be)

## 🎯 Key Features

- **🖼️ Intuitive Web Interface**: Clean, responsive design with drag-and-drop image upload
- **🎯 Real-Time Detection**: Instant object detection with visual annotations and confidence scores
- **👷 Safety Monitoring**: Specialized detection of railway workers and safety equipment
- **📊 Multi-Class Detection**: Identifies workers, safety vests, helmets, and general personnel
- **📱 Cross-Platform**: Compatible with desktop and mobile browsers
- **🔄 Batch Processing**: Support for multiple image uploads and processing
- **📁 Result Management**: Organized storage and retrieval of detection results

## 🏗️ Architecture

### Technology Stack

- **Deep Learning Framework**: Ultralytics YOLOv11
- **Backend**: Flask (Python 3.11+)
- **Computer Vision**: OpenCV, PIL (Pillow)
- **Frontend**: HTML5, CSS3, JavaScript with Jinja2 templating
- **Model Format**: PyTorch (.pt)

### Detection Capabilities

| Object Class | Description | Typical Confidence |
|--------------|-------------|-------------------|
| **Worker** | Railway maintenance personnel | 0.79 - 0.87 |
| **Person** | General human detection | 0.75 - 0.90 |
| **Vest** | High-visibility safety vests | 0.62 - 0.70 |
| **Helmet** | Safety helmets and headgear | 0.62 - 0.75 |

## 📂 Project Structure

```
railway-track-detection/
├── 📄 app.py                          # Main Flask application
├── 🤖 best.pt                         # Trained YOLOv11 model weights
├── 📋 requirements.txt                 # Python dependencies
├── 📖 README.md                        # Project documentation
│
├── 📁 static/
│   ├── 📁 uploads/                     # User uploaded images
│   ├── 📁 results/                     # Detection results with annotations
│   └── 📁 css/                         # Stylesheets
│
├── 📁 templates/
│   ├── 🏠 home.html                    # Landing page
│   ├── 📤 prediction_page.html         # Image upload interface
│   └── 📊 prediction_result_page.html  # Results display page
│
└── 📁 Output images/                   # Sample results and documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip package manager
- 4GB+ RAM (recommended for optimal performance)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jashu171/railway-track-detection.git
   cd railway-track-detection
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv railway_env
   
   # On Windows
   railway_env\Scripts\activate
   
   # On macOS/Linux
   source railway_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Model Installation**
   ```bash
   # Ensure best.pt is in the project root directory
   ls -la best.pt
   ```

5. **Create Required Directories**
   ```bash
   mkdir -p static/uploads static/results
   ```

6. **Launch the Application**
   ```bash
   python app.py
   ```

7. **Access the Web Interface**
   
   Open your browser and navigate to: `http://127.0.0.1:5000/`

## 📖 Usage Guide

### Basic Workflow

1. **Navigate to Upload Page**: Click on "Start Detection" from the home page
2. **Select Image**: Choose a railway track image (JPEG, PNG, BMP, TIFF supported)
3. **Upload & Process**: Click "Upload and Detect" to run the YOLOv11 model
4. **View Results**: Examine the annotated image with bounding boxes and confidence scores
5. **Access History**: View previously processed images in the results section

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/predict` | GET | Upload interface |
| `/predict` | POST | Process uploaded image |
| `/results/<filename>` | GET | View detection results |

## 🖼️ Demo Results

### Web Application Interface
![](https://github.com/jashu171/Railway-Sentry-ML/blob/main/output%20Images/output%20-1%20.jpeg) 
*User-friendly upload interface with real-time processing*

### Detection Examples

**Multi-Worker Detection**
![Worker Detection](https://github.com/jashu171/Railway-Sentry-ML/blob/main/output%20Images/output-2.jpeg)
*Railway workers detected with 79% and 83% confidence*

**Safety Equipment Recognition**
![Safety Detection](https://github.com/jashu171/Railway-Sentry-ML/blob/main/output%20Images/output-3.jpeg)
*Simultaneous detection of workers (84%, 83%) and safety vests (70%, 62%)*

**Helmet Detection**
![Helmet Detection](https://github.com/jashu171/Railway-Sentry-ML/blob/main/output%20Images/output-4.jpeg)
*Safety equipment including vests (70%) and helmets (62%) identified*

**Surveillance Integration**
![Surveillance](https://github.com/jashu171/Railway-Sentry-ML/blob/main/output%20Images/output-5.jpeg)
*Real-time monitoring with 87% confidence person detection*

## ⚙️ Configuration

### Model Configuration

```python
# In app.py - Customize detection parameters
model = YOLO('best.pt')
model.conf = 0.5    # Confidence threshold (0.0-1.0)
model.iou = 0.45    # IoU threshold for NMS
model.max_det = 300 # Maximum detections per image
```

### Performance Tuning

```python
# Optimize for different use cases
# For high accuracy (slower)
model.conf = 0.7
model.iou = 0.5

# For real-time detection (faster)
model.conf = 0.4
model.iou = 0.4
```

## 🔧 Development

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run in debug mode
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

### Model Training (Advanced)

To train your own model:

1. **Prepare Dataset**: Organize images and annotations in YOLO format
2. **Configure Training**: Create `data.yaml` with class definitions
3. **Train Model**:
   ```python
   from ultralytics import YOLO
   
   model = YOLO('yolo11n.pt')  # Load pretrained model
   results = model.train(
       data='data.yaml',
       epochs=100,
       imgsz=640,
       batch=16
   )
   ```

### Testing

```bash
# Run unit tests
python -m pytest tests/

# Test specific functionality
python -m pytest tests/test_detection.py -v
```

## 📊 Performance Metrics

### Model Performance
- **mAP@0.5**: 0.847
- **mAP@0.5:0.95**: 0.623
- **Inference Time**: ~45ms per image (GPU)
- **Model Size**: 22.4 MB

### System Requirements
- **Minimum RAM**: 2GB
- **Recommended RAM**: 4GB+
- **CPU**: Multi-core recommended
- **GPU**: Optional (CUDA-compatible for faster inference)

## 🔒 Security Considerations

- **File Upload Validation**: Only allows image file types
- **File Size Limits**: Maximum 16MB per upload
- **Path Sanitization**: Prevents directory traversal attacks
- **Input Validation**: Validates all user inputs

## 🚀 Deployment

### Production Deployment

```bash
# Using Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# Using Docker
docker build -t railway-detection .
docker run -p 5000:5000 railway-detection
```

### Environment Variables

```bash
export FLASK_ENV=production
export UPLOAD_FOLDER=static/uploads
export RESULTS_FOLDER=static/results
export MAX_CONTENT_LENGTH=16777216  # 16MB
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Submit a Pull Request

### Code Standards

- Follow PEP 8 for Python code
- Add docstrings for all functions
- Include unit tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Ultralytics](https://ultralytics.com/)** - For the exceptional YOLOv11 implementation
- **[Flask Community](https://flask.palletsprojects.com/)** - For the robust web framework
- **[OpenCV](https://opencv.org/)** - For computer vision utilities
- **Railway Industry Professionals** - For domain expertise and validation
- **Open Source Contributors** - For continuous improvements

## 📞 Contact & Support

**👨‍💻 Developer**: Jashwanth Boddupally

- 📧 **Email**: jashwanthboddupally@gmail.com
- 📱 **Phone**: +91 9010767269
- 🌐 **Portfolio**: [jashu171.github.io/portfolio](https://jashu171.github.io/portfolio/)
- 💼 **LinkedIn**: [Jashwanth Boddupally](https://www.linkedin.com/in/jashwanth-boddupally-64068b289/)
- 🐙 **GitHub**: [@jashu171](https://github.com/jashu171)

### Support Options

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/jashu171/railway-track-detection/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/jashu171/railway-track-detection/discussions)
- 📚 **Documentation**: [Wiki](https://github.com/jashu171/railway-track-detection/wiki)

---

<div align="center">

**🚂 Made with ❤️ for Railway Safety and Automation 🚂**

*Enhancing railway infrastructure monitoring through cutting-edge AI technology*

[⭐ Star this repo](https://github.com/jashu171/railway-track-detection) | [🍴 Fork](https://github.com/jashu171/railway-track-detection/fork) | [📝 Report Bug](https://github.com/jashu171/railway-track-detection/issues)

</div>
