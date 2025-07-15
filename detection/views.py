

import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Load the model once when Django starts
model_path = os.path.join(settings.BASE_DIR, "detection", "models_storage", "accident_detection.h5")
model = load_model(model_path)


def index(request):
    return render(request, "index.html")


# Function to Predict Image
def predict_image(image_path):
    """Loads an image and predicts its class using the trained model."""
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    class_labels = {
        0: "Bike Accident",
        1: "Bus Accident",
        2: "Car Accident",
        3: "Non Accident"
    }
    return class_labels.get(predicted_class, "Unknown")


# Django View for Prediction
def predict(request):
    if request.method == "POST" and request.FILES.get("image"):
        img_file = request.FILES["image"]

        upload_dir = os.path.join(settings.MEDIA_ROOT, "uploads")
        os.makedirs(upload_dir, exist_ok=True)

        fs = FileSystemStorage(location=upload_dir, base_url="/media/uploads/")
        filename = fs.save(img_file.name, img_file)
        img_path = os.path.join(upload_dir, filename)
        img_url = fs.url(filename)

        prediction_label = predict_image(img_path)
        alert_color = "red" if "accident" in prediction_label.lower() else "green"

        return render(request, "result.html", {
            "image": img_url,
            "prediction": prediction_label,
            "alert_color": alert_color
        })

    return render(request, "index.html")
