#  Lung and Colon Cancer Classification from Histopathological Image Using Machine Learning 


**Course:** CSE 440 — Artificial Intelligence
**Group:** 10
**Institution:** North South University
**Faculty:** Mohammad Shifat-E-Rabbi
**Semester:** Summer 2026

---

##  Group Members

| Name | Student ID |
|---|---|
| Rezwana Shama | 1410062042 |
| Mehbur Rahman | 2121673042 |
| S.M. Atiqur Islam | 2132173642 |
| Aditi Basu | 2212067042 |

---

##  Project Overview

This project develops an **automated cancer classification system** that identifies lung and colon cancer types from histopathological images using a deep learning model. The system is built on a **VGGNet-inspired Convolutional Neural Network (CNN)** trained on the LC25000 dataset, which contains 25,000 histopathological images across five classes:

-  Colon Adenocarcinoma
-  Colon Benign Tissue
-  Lung Adenocarcinoma
-  Lung Squamous Cell Carcinoma
-  Lung Benign Tissue


---

## Objectives

- Design and train a VGGNet-inspired CNN for multi-class cancer image classification
- Achieve high classification accuracy on the LC25000 histopathological dataset
- Implement data preprocessing techniques, including normalization, augmentation, and stratification
- Evaluate model performance using accuracy, precision, recall, F1-score, and confusion matrix
- Deploy the trained model into a real-time Flask web application for clinical-aid use

---

## Technologies & Tools

| Category | Tool / Library |
|---|---|
| Language | Python 3.11.9 |
| Deep Learning | TensorFlow, Keras |
| Image Processing | OpenCV (cv2), ImageDataGenerator |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Flask, HTML, CSS |
| Development IDE | Visual Studio Code |
| Cloud Training | Google Colab (Tesla T4 GPU, 12GB RAM) |
| Version Control | Git & GitHub |
| Dataset | LC25000 (25,000 images, 1.85 GB) |

---

##  Model Architecture

The CNN model consists of **16 layers** inspired by the VGG architecture:

- **Convolutional Layers** — Feature extraction using 64, 128, and 512 filters with ReLU activation
- **Max-Pooling Layers** — Spatial dimension reduction to control overfitting
- **Dense Layers** — Fully connected layers with 256, 64, and 5 units
- **Output Layer** — SoftMax activation for 5-class classification
- **Optimizer** — Adamax (learning rate: 0.001)
- **Loss Function** — Categorical Cross-Entropy
- **Training** — 20 epochs, batch size of 65, best at epoch 16

---

## 📂 Project Structure Tentative

```
cse299-cancer-classification-group10/
│
├── main.py                    # Main entry point to run the Flask app
├── README.md                  # Project explanation (this file)
├── requirements.txt           # Libraries needed to run the project
│
├── model/
│   └── Model.h5               # Trained CNN model (~242 MB)
│
├── support/
│   ├── model_training.ipynb   # CNN training notebook (Google Colab)
│   ├── preprocessing.py       # Image preprocessing & augmentation
│   ├── evaluate.py            # Model evaluation & mismatch testing
│   └── predict.py             # Single image prediction logic
│
├── templates/
│   └── index.html             # Flask web app frontend
│
├── static/
│   └── style.css              # Web app styling
│
├── data/
│   └── LC25000/               # Dataset folder (not included in repo)
│
└── others/
    ├── update_report.pdf          # Mid-project update report
    ├── update_presentation.pptx   # Mid-project update presentation
    ├── final_report.pdf           # Final project report
    ├── final_presentation.pptx    # Final project presentation
    └── demo_video.mp4             # One-minute project demo video
```

---

##  Dataset

The **LC25000 Dataset** contains 25,000 histopathological images (1.85 GB) split as follows:

| Split | Percentage | Total Images |
|---|---|---|
| Training | 80% | 20,000 |
| Validation | 10% | 2,500 |
| Testing | 10% | 2,500 |

Stratification was applied using `train_test_split` to maintain class balance across all subsets.

---

##  Project Timeline Tentative

| Week | Milestone |
|---|---|
| Week 1 | Repository setup, team formation, README |
| Week 2 | Dataset exploration & preprocessing pipeline |
| Week 3 | CNN model architecture design |
| Week 4 | Model training on Google Colab (20 epochs) |
| Week 5 | Model evaluation — accuracy, precision, recall, F1 |
| Week 6 | Update report & update presentation |
| Week 7 | Flask web app development & integration |
| Week 8 | Final testing, demo video & submission |

---

##  Getting Started

### Prerequisites
```bash
Python 3.11.9
TensorFlow 2.x
Flask

## 📋 requirements.txt

```
tensorflow==2.x
flask
opencv-python
numpy
pandas
matplotlib
seaborn
scikit-learn
```

---


##  License

This project is developed for **academic purposes** under CSE 440 at North South University. All rights reserved by the group members.

---

<p align="center">Made with ❤️ by Group 10 — North South University</p>
