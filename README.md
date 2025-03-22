# Anomaly Detection using VideoMAE Transformer

## Overview

This project implements an anomaly detection system using the **VideoMAE Transformer**. The system allows users to upload videos, analyze them for anomalies, and receive detailed reports.

## Features

- **User Authentication**: Secure user login and signup.
- **Video Upload**: Users can upload videos for anomaly detection.
- **Anomaly Detection**: VideoMAE Transformer processes the video to detect anomalies.
- **Results Dashboard**: Users can view results in a structured format.
- **API Support**: Endpoints available for external applications.

## Project Workflow

### 1. User Authentication

- Users sign up and log in with credentials.
- Secure authentication mechanisms are used (e.g., JWT or OAuth).

### 2. Video Upload

- Users upload videos via the web interface or API.
- Videos are stored temporarily for processing.

### 3. Anomaly Detection

- The uploaded video is preprocessed (frame extraction, resizing, etc.).
- The **VideoMAE Transformer** is used to analyze video frames.
- The model detects anomalies based on learned patterns.

### 4. Results Generation

- Anomalous frames are highlighted.
- A report is generated with timestamps of detected anomalies.
- Results are displayed on a dashboard.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- PyTorch
- Transformers (Hugging Face)
- OpenCV
- Flask (for API & Web Interface)

### Steps

```sh
git clone https://github.com/yourusername/anomaly-detection-videomae.git
cd anomaly-detection-videomae
pip install -r requirements.txt
```

## Usage

### Running the Application

```sh
python app.py
```

Access the web interface at `http://localhost:5000`

### API Endpoints

#### Upload Video

```sh
POST /upload
```

#### Get Anomaly Results

```sh
GET /results/{video_id}
```

## Model Details

- Uses **VideoMAE Transformer** for self-supervised learning.
- Pretrained on large-scale video datasets.
- Fine-tuned for anomaly detection tasks.

## Contributing

Contributions are welcome! Feel free to open issues and pull requests.

## License

MIT License
