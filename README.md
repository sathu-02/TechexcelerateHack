# Anomaly Detection using VideoMAE

## 📌 Overview
This project implements an *anomaly detection system for videos* using the *VideoMAE (Masked Autoencoder) Transformer. It classifies video clips into **normal* or *anomalous* behavior by analyzing video frames. The model is fine-tuned on custom datasets and deployed using the Hugging Face Transformers library.

## ⚙ Features
- Uses *VideoMAE Transformer* for video classification
- Supports training on a custom dataset of normal and anomalous videos
- Implements *frame extraction* and *preprocessing* for model compatibility
- Provides a pipeline for *real-time anomaly detection*
- Deploys the fine-tuned model on *Hugging Face Hub*

---

## 🛠 Setup Instructions
### *1️⃣ Install Dependencies*
Ensure you have Python *3.8+* installed. Then, install the required packages:
sh
pip install torch torchvision transformers opencv-python numpy matplotlib scikit-learn huggingface_hub


### *2️⃣ Clone the Repository*
sh
git clone https://github.com/sathu-02/TechexcelerateHack.git
cd your-repo


### *3️⃣ Configure Hugging Face Authentication*
Create a .env file and add your Hugging Face token:
ini
HF_TOKEN=your_huggingface_token

Or set it in your terminal:
sh
export HF_TOKEN="your_huggingface_token"


---

## 📂 Dataset Preparation
1. Place your dataset in the train_70/ directory.
2. Organize video files into *normal* and *anomaly* subfolders:
   
   train_70/
   ├── normal/
   │   ├── normal_video1.mp4
   │   ├── normal_video2.mp4
   ├── anomaly/
   │   ├── anomaly_video1.mp4
   │   ├── anomaly_video2.mp4
   

---

## 🚀 Training the Model
Run the training script:
sh
python train.py

This will:
- Load and preprocess video frames
- Train the VideoMAE model for *10 epochs*
- Save the fine-tuned model to ./fine_tuned_anomaly_detector_10/

---

## 📊 Model Evaluation
To evaluate the model:
sh
python evaluate.py

It will print the *accuracy* and other evaluation metrics.

---

## 🔍 Anomaly Detection on New Videos
Run anomaly detection on a test video:
sh
python detect.py --video test_video.mp4

If an anomaly is detected, the script will display the frame with a bounding box.

---

## 🖥 Deploying the Model to Hugging Face
After training, you can *push the model to Hugging Face*:
sh
python push_to_hub.py

Ensure your Hugging Face token is configured properly.

---

🚀 Happy coding!