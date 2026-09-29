import os
from flask import Flask, render_template, request, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
from PIL import Image
import numpy as np

# -----------------------------------------
# INITIAL SETUP
# -----------------------------------------
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# -----------------------------------------
# LOAD MODEL
# -----------------------------------------
MODEL_PATH = os.path.join(BASE_DIR, "models", "skin_disease_efficientnet_final.keras")
print("Loading model from:", MODEL_PATH)
model = load_model(MODEL_PATH)

CLASS_NAMES = [
    "Jerawat",
    "Kulit_Kering",
    "Kulit_Kusam",
    "Kulit_Sensitif",
    "Pori_Pori_Besar",
    "Produksi_Minyak",
    "Tanda_Penuaan"
]

# -----------------------------------------
# PENJELASAN PENYAKIT + SOLUSI
# -----------------------------------------
DISEASE_INFO = {
    "Jerawat": {
        "description": "Jerawat terjadi karena pori-pori tersumbat oleh minyak dan sel kulit mati.",
        "solution": "Gunakan salicylic acid, benzoyl peroxide, jaga kebersihan wajah, hindari memencet jerawat."
    },
    "Kulit_Kering": {
        "description": "Kulit kering disebabkan kurangnya kelembapan pada lapisan kulit terluar.",
        "solution": "Gunakan moisturizer tebal, hindari sabun keras, mandi air hangat, minum air cukup."
    },
    "Kulit_Kusam": {
        "description": "Kulit kusam muncul akibat penumpukan sel kulit mati dan dehidrasi.",
        "solution": "Eksfoliasi 1–2 kali/minggu, gunakan sunscreen, dan skincare yang mengandung vitamin C."
    },
    "Kulit_Sensitif": {
        "description": "Kulit sensitif mudah iritasi akibat produk atau kondisi eksternal.",
        "solution": "Gunakan produk bebas pewangi, lakukan patch test, hindari exfoliant yang keras."
    },
    "Pori_Pori_Besar": {
        "description": "Pori-pori besar terjadi karena produksi minyak berlebih dan elastisitas kulit menurun.",
        "solution": "Gunakan BHA (salicylic acid), clay mask, dan sunscreen setiap hari."
    },
    "Produksi_Minyak": {
        "description": "Kulit berminyak terjadi akibat kelenjar sebaceous yang terlalu aktif.",
        "solution": "Gunakan niacinamide, BHA, hindari over-washing, gunakan oil-free moisturizer."
    },
    "Tanda_Penuaan": {
        "description": "Tanda penuaan muncul karena kehilangan elastisitas dan kolagen kulit.",
        "solution": "Gunakan retinol, sunscreen SPF 50, moisturizer kaya peptida atau hyaluronic acid."
    }
}

# -----------------------------------------
# PREDIKSI MODEL
# -----------------------------------------
def model_predict(img_path, model):
    img = Image.open(img_path).resize((224, 224))
    img_array = np.array(img)

    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    class_index = np.argmax(preds)
    confidence = float(np.max(preds)) * 100

    return CLASS_NAMES[class_index], confidence

# -----------------------------------------
# ROUTES
# -----------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return render_template("upload.html", error="Please upload an image.")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        result, confidence = model_predict(filepath, model)

        description = DISEASE_INFO[result]["description"]
        solution = DISEASE_INFO[result]["solution"]

        return render_template(
            "upload.html",
            prediction=result,
            confidence=f"{confidence:.2f}",
            description=description,
            solution=solution,
            image_url=url_for("static", filename="uploads/" + file.filename)
        )

    return render_template("upload.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# -----------------------------------------
# RUN SERVER
# -----------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
