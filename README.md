# SkinningAI

**SCAN. DETECT. TREAT.**

SkinningAI is a web application that helps users screen common skin conditions from a photo. Upload a picture, and the system classifies the condition using a deep learning model, then shows a short explanation and care suggestions.

> **Disclaimer:** SkinningAI is an early-screening tool for information purposes only. It does **not** replace a diagnosis from a doctor or dermatologist.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [How It Works](#how-it-works)
- [Model & Dataset](#model--dataset)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Limitations & Future Work](#limitations--future-work)
- [Team](#team)

## Background

Access to and the cost of skin consultations remain a barrier for many people. As a result, common conditions such as acne or dry skin are often treated late or self-diagnosed, and mild cases can develop into more serious ones.

SkinningAI aims to provide a **fast, free, and reliable screening tool** that people can use to validate their initial information before deciding on further treatment.

## Features

- Upload a skin photo and get an analysis in seconds
- Classification into **7 skin condition classes**
- Prediction confidence shown as a percentage
- Description of the detected condition and suggested care
- Free to use
- Simple pages: Home, Upload, About Us, Contact Us

### Detected Classes

| # | Class |
| --- | --- |
| 1 | Jerawat (Acne) |
| 2 | Kulit Kering (Dry skin) |
| 3 | Kulit Kusam (Dull skin) |
| 4 | Kulit Sensitif (Sensitive skin) |
| 5 | Pori-Pori Besar (Enlarged pores) |
| 6 | Produksi Minyak (Oily skin) |
| 7 | Tanda Penuaan (Signs of aging) |

## How It Works

1. Open the **Upload** page.
2. Click **Insert photo** and choose the image you want to analyze.
3. Click **Start Analyzing**.
4. The result, confidence score, and suggestions appear in the result box below.

Behind the scenes, the Flask backend resizes the image to **224×224**, applies EfficientNet preprocessing, runs the model, and returns the predicted class along with its description and advice.

## Model & Dataset

**Model:** EfficientNetB0 (a CNN), chosen for its balance between accuracy and computational efficiency.

**Techniques:**

- **CNN** for automatic visual feature extraction
- **Transfer learning** to reduce overfitting on a limited dataset and speed up training
- **Data augmentation** (rotation, zoom, shift) to improve generalization

**Dataset:** [7 Masalah Kulit Indonesia](https://www.kaggle.com/datasets/deayulianisabrina/7-masalah-kulit-indonesia) on Kaggle

| Item | Value |
| --- | --- |
| Classes | 7 |
| Images per class | 350 |
| Total images | 2,450 |
| Split | 70% train / 15% validation / 15% test |

**Result:** Final test accuracy of **77.51%**.

## Tech Stack

- **Backend:** Python, Flask
- **AI / ML:** TensorFlow / Keras (EfficientNetB0), NumPy, Pillow
- **Frontend:** HTML, CSS, JavaScript (Jinja2 templates)

## Project Structure

```
SkinningAI/
├── app.py                 # Flask app (routes + model inference)
├── models/
│   └── skin_disease_efficientnet_final.keras
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── index.html
│   ├── upload.html
│   ├── about.html
│   └── contact.html
├── static/
│   ├── styles.css
│   ├── script.js
│   └── uploads/           # uploaded images (created automatically)
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Edward-NA/SkinningAI.git
cd SkinningAI

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install flask tensorflow pillow numpy
```

### Run the app

Make sure the trained model file is located at `models/skin_disease_efficientnet_final.keras`, then run:

```bash
python app.py
```

Open the local address shown in the terminal (by default `http://127.0.0.1:5000`) in your browser.

## Limitations & Future Work

**Limitations**

- The dataset is limited and image lighting conditions vary
- The model does not replace a doctor's diagnosis
- Accuracy still depends on the quality of the input image

**Future work**

- Expand the dataset
- Add more skin condition classes
- Integrate into a mobile app

## Team

| Name | Role |
| --- | --- |
| Darren Christian Pramana | Proposal, model training and AI model development |
| Edward Nicholas Adidjaja | Proposal, website UI design, frontend & backend source code |
| Nathan Phan | Proposal, website UI design, frontend & backend source code |

Computer Science, Bina Nusantara University

---

> Built as a team project. Dataset credit: Dea Yuliani Sabrina on Kaggle.
