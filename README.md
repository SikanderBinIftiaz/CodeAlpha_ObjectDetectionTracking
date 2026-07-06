#  CodeAlpha - AI Object Detection & Tracking

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red.svg)
![Status](https://img.shields.io/badge/Project-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

##  Project Overview

This project was developed as part of the **CodeAlpha Python Programming Internship**.

It is an AI-powered Object Detection and Tracking system capable of detecting multiple objects in real time using the **YOLOv8** deep learning model. Each detected object is highlighted with a bounding box, class name, confidence score, and tracking ID.

The application supports both:

-  Live Webcam Detection
-  Video File Detection

---

#  Features

 Real-Time Object Detection

 Multi-Object Tracking

 Live Webcam Support

 Video File Processing

 Bounding Boxes

 Confidence Scores

 Tracking IDs

 FPS Counter

 YOLOv8 Deep Learning Model

---

#  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Video Processing |
| YOLOv8 | Object Detection |
| Ultralytics | YOLO Framework |
| ByteTrack | Object Tracking |

---

#  Project Structure

```
CodeAlpha_ObjectDetectionTracking/
│
├── app.py
├── camera_test.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── outputs/
│     └── output.mp4
│
├── videos/
│     └── sample.mp4
│
└── screenshots/
      ├── live_detection.png
      ├── video_detection.png
      └── tracking.png
```

---

#  Installation

Clone the repository

```bash
git clone https://github.com/SikanderBinIftiaz/CodeAlpha_ObjectDetectionTracking.git
```

Move into the project directory

```bash
cd CodeAlpha_ObjectDetectionTracking
```

Create a virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Live Camera Detection

```bash
python app.py
```

---

## Video Detection

Place your video inside the **videos** folder.

Example

```
videos/sample.mp4
```

Run

```bash
python app.py
```

---

#  YOLOv8 Model

This project uses the **YOLOv8s** model from Ultralytics for object detection.

The model automatically detects objects such as

- Person
- Car
- Bottle
- Laptop
- Chair
- Cell Phone
- Keyboard
- Mouse
- TV
- Bicycle
- Dog
- Cat

and many more.

---

# 📷 Screenshots

## Live Detection

![Live Detection](screenshots/live_detection.png)

---

## Video Detection

![Video Detection](screenshots/video_detection.png)

---

## Object Tracking

![Tracking](screenshots/tracking.png)

---

#  Project Workflow

```
Camera / Video
       │
       ▼
Read Frame
       │
       ▼
YOLOv8 Detection
       │
       ▼
Object Tracking
       │
       ▼
Draw Bounding Boxes
       │
       ▼
Display Results
```

---

#  Future Improvements

- Face Recognition
- Vehicle Speed Detection
- Crowd Counting
- Fire Detection
- Helmet Detection
- License Plate Recognition
- GUI using PySide6
- Streamlit Web Version

---

#  Author

**Sikander Bin Iftiaz**

Python Developer

GitHub

https://github.com/SikanderBinIftiaz

---

#  Acknowledgements

- CodeAlpha Internship
- Ultralytics YOLOv8
- OpenCV Community

---

#  Support

If you like this project,

 Star this repository

and share it with others!
