# 🛡️ Anti-Spoofing System (Liveness Detection)

> A robust, real-time face anti-spoofing detection system using **YOLOv8** and **OpenCV**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)

## 📖 Overview

This project implements a computer vision pipeline to distinguish between **"Real"** faces (live people) and **"Fake"** faces (photos, screens, or masks). It eliminates the vulnerability of standard face recognition systems to spoofing attacks.

The system is built on **Ultralytics YOLOv8**, a state-of-the-art object detection model, ensuring high speed and accuracy for real-time applications.

## ✨ Features

- **Real-time Detection**: Operates seamlessly on live webcam feeds.
- **High Accuracy**: Custom-trained YOLO model for binary classification (Real vs. Fake).
- **Smart Data Collection**:
    - **Blur Detection**: Automatically discards blurry images during data collection using Laplacian variance.
    - **Auto-Balancing**: Helps organize data into training, validation, and testing sets.
- **Visual Feedback**: Color-coded bounding boxes (Green for Real, Red for Fake) with confidence scores.

## 🛠️ Tech Stack

- **Core**: Python 3
- **Computer Vision**: OpenCV, cvzone
- **AI/ML Engine**: Ultralytics YOLOv8
- **Data Handling**: NumPy, Math

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed. It is recommended to use a virtual environment.

```bash
# Clone the repository
git clone https://github.com/yourusername/Anti-Spoofing-Project.git
cd Anti-Spoofing-Project

# Install dependencies (create a requirements.txt first if you haven't!)
pip install ultralytics cvzone opencv-python numpy
```

### 1. Data Collection
To train your own model, first collect dataset samples:

```bash
python dataCollection.py
```
*   **Controls**: The script automatically captures faces. It filters out blurry frames.
*   **Config**: Adjust `classID` (0 for Fake, 1 for Real) in the script before running.

### 2. Data Preparation
Organize your raw data into a YOLO-compatible structure:

```bash
python splitData.py
```
This splits your data into `train`, `val`, and `test` directories and generates the `dataset` folder.

### 3. Training
Train the model on your custom dataset:

```bash
python train.py
```
*   **Note**: Ensure the dataset configuration file (`data.yaml`) path is correct in `train.py`.

### 4. Inference (Run the App)
Run the real-time detection system:

```bash
python main.py
```

## 📂 Project Structure

```
├── Dataset/             # Raw and processed datasets
├── models/              # Trained weights (manas.pt, yolov8n.pt)
├── runs/                # Training logs and graphs
├── dataCollection.py    # Script for collecting face data
├── splitData.py         # Script to split data (Train/Val/Test)
├── train.py             # YOLOv8 training script
└── main.py              # Main real-time application
```

## ✔️ Demo Outcomes 

```
<img width="1470" height="956" alt="Screenshot 2024-12-27 at 19 11 26" src="https://github.com/user-attachments/assets/ec95b211-3843-4116-92de-32d963ac7e45" />
<img width="1470" height="956" alt="Screenshot 2024-12-26 at 11 16 12" src="https://github.com/user-attachments/assets/5b465662-fe67-45e4-a704-ca2570f6769e" />
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
