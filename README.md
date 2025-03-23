# Anomaly Detection in Videos

## Overview
This project implements an anomaly detection system for videos. Users can upload videos, and the system analyzes them for anomalies using machine learning techniques. The system includes a frontend for user interaction, a backend for handling requests, and a model for detecting anomalies.

## Features
- User authentication (login/signup)
- Video upload functionality
- Anomaly detection in videos
- Storage of flagged videos for further review
- Web-based interface for user interaction

## Project Structure
```
TechexcelerateHack/
├── backend/
│   ├── db/
│   ├── app.js (Node.js backend)
│   ├── app.py (Flask for anomaly detection)
│
├── frontend/
│   ├── assets/
│   ├── db/
│   ├── node_modules/
│   ├── app.js (Frontend logic)
│   ├── home.html
│   ├── login.html
│   ├── main.html
│   ├── signup.html
│   ├── history.html
│   ├── style.css
│   ├── package.json
│   ├── package-lock.json
│   ├── passwordnotmatch.html
│   ├── usernamecannotfound.html
│
├── model/
│   ├── main (1).ipynb
│   ├── model (2).ipynb
│
└── README.md
```

## Setup Instructions
### 1. Install Dependencies
Ensure you have Node.js and Python installed. Then, install the necessary packages:
```sh
# Backend dependencies
cd backend
npm install
pip install flask flask-cors opencv-python transformers
```

```sh
# Frontend dependencies
cd frontend
npm install
```

### 2. Clone the Repository
```sh
git clone https://github.com/sathu-02/TechexcelerateHack.git
cd TechexcelerateHack
```

### 3. Running the Application
#### Backend
Start the backend server:
```sh
cd backend
node app.js  # Start Node.js server
python app.py  # Start Flask server
```

#### Frontend
Start the frontend:
```sh
cd frontend
npm start
```

### 4. Using the Application
- Open a browser and navigate to `http://localhost:3000`
- Sign up or log in
- Upload a video for anomaly detection
- View results on the web interface

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

