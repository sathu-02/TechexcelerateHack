# import os
# import tempfile
# import cv2
# from flask import Flask, request, send_file, jsonify
# from transformers import pipeline
# from io import BytesIO
# from PIL import Image
# import torch
# from flask_cors import CORS

# app = Flask(__name__)  # Fix the name here
# CORS(app)  # Enable CORS for cross-origin requests

# # Check if CUDA (GPU) is available, otherwise use CPU
# device = 0 if torch.cuda.is_available() else -1

# # Initialize the video classification pipeline
# pipe = pipeline("video-classification", model="rish13/videomae_4frames", device=device)

# # Store uploaded videos temporarily
# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.route("/upload", methods=["POST"])
# def upload_video():
#     """Handles video file upload and returns the saved file path."""
#     if "video" not in request.files or request.files["video"].filename == "":
#         return jsonify({"error": "No video file uploaded"}), 400

#     video = request.files["video"]
#     file_path = os.path.join(UPLOAD_FOLDER, video.filename)
#     video.save(file_path)

#     return jsonify({"message": "Video uploaded successfully", "file_path": file_path})


# # @app.route("/process", methods=["POST"])
# # def process_video():
# #     """Receives the video path, processes it, and returns the anomaly frame image."""
# #     data = request.get_json()
# #     video_path = data.get("file_path")

# #     if not video_path or not os.path.exists(video_path):
# #         return jsonify({"error": "Invalid file path"}), 400

# #     anomaly_frame, timestamp, score = detect_anomalies_in_video(video_path)

# #     if anomaly_frame:
# #         image = Image.open(BytesIO(anomaly_frame))
# #         image_io = BytesIO()
# #         image.save(image_io, "PNG")
# #         image_io.seek(0)

# #         return send_file(image_io, mimetype="image/png")
# #     else:
# #         return jsonify({"message": "No anomaly detected in the video."}), 200
# @app.route("/process", methods=["POST"])
# def process_video():
#     """Receives the uploaded video and processes it."""
#     if "video" not in request.files:
#         return jsonify({"error": "No video file uploaded"}), 400

#     video = request.files["video"]
#     temp_path = os.path.join("uploads", video.filename)
#     video.save(temp_path)

#     anomaly_frame, timestamp, score = detect_anomalies_in_video(temp_path)

#     if anomaly_frame:
#         image = Image.open(BytesIO(anomaly_frame))
#         image_io = BytesIO()
#         image.save(image_io, "PNG")
#         image_io.seek(0)

#         return send_file(image_io, mimetype="image/png")
    
#     return jsonify({"message": "No anomaly detected."}), 200



# def detect_anomalies_in_video(video_path):
#     """Processes the video and detects anomalies using the model."""
#     cap = cv2.VideoCapture(video_path)
#     min_frames, num_frames = 4, 16
#     frames, frame_count = [], 0
#     highest_anomaly_score, highlighted_frame, highlighted_timestamp = 0, None, 0
#     fps = cap.get(cv2.CAP_PROP_FPS) or 30
#     frame_skip = max(1, int(fps * 0.2))

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         if frame_count % frame_skip == 0:
#             frame_resized = cv2.resize(frame, (224, 224))
#             frames.append(frame_resized / 255.0)

#             if len(frames) >= min(min_frames, len(frames)):
#                 while len(frames) < num_frames:
#                     frames.append(frames[-1])

#                 temp_video_path = tempfile.mktemp(suffix=".mp4")
#                 try:
#                     fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#                     out = cv2.VideoWriter(temp_video_path, fourcc, fps, (224, 224))
#                     for f in frames[-num_frames:]:
#                         out.write((f * 255).astype("uint8"))
#                     out.release()

#                     result = pipe(temp_video_path)

#                     normal_score = result[0]["score"] if result[0]["label"] == "LABEL_0" else 0
#                     anomalous_score = result[0]["score"] if result[0]["label"] == "LABEL_1" else 0

#                     timestamp = (frame_count - len(frames) + 1) / fps
#                     if anomalous_score > normal_score and anomalous_score > highest_anomaly_score:
#                         highest_anomaly_score = anomalous_score
#                         highlighted_frame = frame.copy()
#                         highlighted_timestamp = timestamp

#                 finally:
#                     try:
#                         os.unlink(temp_video_path)
#                     except PermissionError:
#                         print(f"Warning: Could not delete {temp_video_path}, retrying later.")

#                 frames.pop(0)

#         frame_count += 1

#     cap.release()

#     if highlighted_frame is not None:
#         _, buffer = cv2.imencode(".png", highlighted_frame)
#         return buffer.tobytes(), highlighted_timestamp, highest_anomaly_score
#     else:
#         return None, None, None


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)  # Set Flask to run on port 5000


import os
import tempfile
import cv2
from flask import Flask, request, send_file, jsonify
from transformers import pipeline
from io import BytesIO
from PIL import Image
import torch
from flask_cors import CORS  

app = Flask(__name__)  # Fix the incorrect _name_
CORS(app)  

device = 0 if torch.cuda.is_available() else -1
pipe = pipeline("video-classification", model="rish13/videomae_4frames", device=device)

def detect_anomalies_in_video(video_path):
    cap = cv2.VideoCapture(video_path)
    min_frames, num_frames = 4, 16
    frames, frame_count = [], 0
    highest_anomaly_score, highlighted_frame, highlighted_timestamp = 0, None, 0
    fps = cap.get(cv2.CAP_PROP_FPS) or 30  
    frame_skip = max(1, int(fps * 0.2))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            frame_resized = cv2.resize(frame, (224, 224))
            frames.append(frame_resized / 255.0)

            if len(frames) >= min(min_frames, len(frames)):
                while len(frames) < num_frames:
                    frames.append(frames[-1])

                temp_video_path = tempfile.mktemp(suffix=".mp4")
                try:
                    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                    out = cv2.VideoWriter(temp_video_path, fourcc, fps, (224, 224))

                    for f in frames[-num_frames:]:
                        out.write((f * 255).astype("uint8"))
                    out.release()

                    result = pipe(temp_video_path)

                    normal_score = result[0]["score"] if result[0]["label"] == "LABEL_0" else 0
                    anomalous_score = result[0]["score"] if result[0]["label"] == "LABEL_1" else 0

                    timestamp = (frame_count - len(frames) + 1) / fps
                    if anomalous_score > normal_score and anomalous_score > highest_anomaly_score:
                        highest_anomaly_score = anomalous_score
                        highlighted_frame = frame.copy()
                        highlighted_timestamp = timestamp

                finally:
                    cap.release()  # Ensure video capture is released
                    try:
                        os.unlink(temp_video_path)  
                    except PermissionError:
                        print(f"Warning: Could not delete {temp_video_path}, retrying later.")

                frames.pop(0)

        frame_count += 1

    cap.release()

    if highlighted_frame is not None:
        height, width, _ = highlighted_frame.shape
        cv2.rectangle(highlighted_frame, (0, 0), (width, height), (0, 0, 255), 2)
        text = f"Anomaly Detected at {highlighted_timestamp:.2f}s, Score: {highest_anomaly_score:.4f}"
        cv2.putText(
            highlighted_frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1
        )

        _, buffer = cv2.imencode(".png", highlighted_frame)
        return buffer.tobytes(), highlighted_timestamp, highest_anomaly_score
    else:
        return None, None, None

@app.route("/process", methods=["POST"])  # Fix the endpoint
def process_video():
    if "video" not in request.files or request.files["video"].filename == "":
        return jsonify({"message": "No video file uploaded"}), 400

    video = request.files["video"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        video.save(temp_video.name)
        try:
            anomaly_frame, timestamp, score = detect_anomalies_in_video(temp_video.name)

            if anomaly_frame:
                image = Image.open(BytesIO(anomaly_frame))
                image_io = BytesIO()
                image.save(image_io, "PNG")
                image_io.seek(0)

                return send_file(
                    image_io, mimetype="image/png", as_attachment=False, download_name="anomaly_frame.png"
                )
            else:
                return jsonify({"message": "No anomaly detected in the video."}), 200
        finally:
            try:
                os.unlink(temp_video.name)
            except PermissionError:
                print(f"Warning: Could not delete {temp_video.name}, retrying later.")

if __name__ == "__main__":  # Fix incorrect name
    app.run(debug=True)
