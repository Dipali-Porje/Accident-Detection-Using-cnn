# 🚨 Accident Detection System using CNN with Django Web Interface

A Deep Learning-based web application that detects the type of road accident (if any) using image input. Built using **Django** for the backend and a **trained CNN model** for prediction.

## 🧠 Features

- Detects one of four classes from an uploaded image:
  - 🚌 Bus Accident
  - 🚗 Car Accident
  - 🚲 Bike Accident
  - ✅ No Accident
- CNN-based classifier with high accuracy
- Clean, user-friendly Django web interface
- Highlights result with color:
  - 🟥 **Red**: Accident Detected
  - 🟩 **Green**: No Accident

---

## 🗂️ Project Structure

accident_detection_django/
├── manage.py
├── accident_dashboard/
│ ├── templates/
│ │ └── upload.html # Upload and result UI
│ ├── static/ # CSS/JS/images if any
│ ├── views.py # Prediction and rendering logic
│ ├── urls.py
│ └── models.py # (If extended for DB)
├── cnn_model/
│ └── accident_model.h5 # Trained CNN model
├── media/ # Uploaded images
├── requirements.txt
└── README.md


---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Dipali-Porje/accident-detection-Using-cnn.git
cd accident-detection-Using-cnn

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Run Migrations

python manage.py migrate

### 4️⃣ Start the Django Server

python manage.py runserver

### 🛠 Model Info

Framework: TensorFlow / Keras
Input size: 224x224 grayscale or RGB
Classes:
0: Bike Accident
1: Car Accident
2: Bus Accident
3: No Accident
