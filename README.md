# SmartBridge_ai_ml
HematoVision: AI-Powered Blood Cell Classification

# HematoVision – Blood Cell Classification using Transfer Learning

HematoVision is an AI-powered diagnostic tool that classifies blood cells using **transfer learning** with pre-trained CNNs like ResNet50. Built with TensorFlow/Keras, the model is trained on a dataset of 12,000+ annotated images, categorized into:

- Eosinophils
- Lymphocytes
- Monocytes
- Neutrophils

The project delivers a scalable, efficient, and accurate solution for healthcare and medical training.

---

## 🔍 Problem Statement

Blood cell analysis is traditionally manual and time-consuming. This project leverages **transfer learning** to automate and accelerate the classification of blood cells, improving efficiency and reducing human error in clinical diagnostics.

---

##  Use Case Scenarios

### Scenario 1: Automated Diagnostic Systems
Integrates with hospital systems to classify cells in real-time, generate diagnostic reports, and assist pathologists.

### Scenario 2: Remote Medical Consultations
Enables accurate remote diagnostics in telemedicine platforms through image upload and real-time AI analysis.

### Scenario 3: Medical Education Tools
Interactive tool for students to learn morphology and classification of cells via image input and feedback.



## Tech Stack

- Python 3
- TensorFlow / Keras
- Flask (for web interface)
- ResNet50 (pre-trained CNN)
- Jupyter Notebook
- HTML/CSS (for frontend)
  
#Project Structure

hematovision-app/
├── app.py # Flask backend
├── predict.py # Prediction logic
├── hematovision_model.h5 # Trained model (use Drive link if large)
├── templates/
│ └── index.html # Upload UI
├── uploads/ # Uploaded images folder
├── requirements.txt # Dependencies
└── README.md # Project documentation


