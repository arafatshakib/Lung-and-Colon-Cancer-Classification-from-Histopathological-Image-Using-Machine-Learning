Week 1 Progress Report (Model & Training)


Branch
feature/model-setup

Tasks Completed
1. Research on CNN Architectures

Studied several CNN architectures commonly used for histopathology image classification including:

VGG16
ResNet50
DenseNet121
EfficientNetB0

Compared their:

Accuracy
Number of parameters
Computational complexity
Suitability for medical image datasets

After comparing previous research papers, a VGGNet-inspired custom CNN was selected because:

Simpler implementation
Easier training
Good performance on the LC25000 dataset
Lower computational requirements than deeper networks
2. Google Colab Environment Setup

Configured Google Colab environment.

Installed:

TensorFlow
Keras
NumPy
Matplotlib
Pandas
Scikit-learn

Verified GPU availability.

Example output:

GPU Available: True
GPU: Tesla T4
TensorFlow Version: 2.16.x
3. Designed Initial CNN Architecture

Prepared the initial network design.

Architecture plan:

Input
↓

Conv2D (64)

↓

MaxPooling

↓

Conv2D (128)

↓

MaxPooling

↓

Conv2D (256)

↓

MaxPooling

↓

Conv2D (512)

↓

MaxPooling

↓

Flatten

↓

Dense(256)

↓

Dropout

↓

Dense(5 Softmax)

This architecture was documented for implementation during Week 2.

Challenges
Compared multiple architectures before deciding.
Reviewed several histopathology classification papers.
Balanced model complexity against training time.
Files Committed
docs/
    architecture_notes.md

model/
    model_plan.md

README.md
architecture_notes.md
# CNN Architecture Notes

Candidate models:

- VGG16
- ResNet50
- DenseNet121
- EfficientNet

Chosen Model:

Custom VGG-inspired CNN

Reason:

- Simple
- Lightweight
- Easy to modify
- Performs well on the LC25000 dataset

Input Shape

224 x 224 x 3

Classes

5

Activation

ReLU

Output

Softmax
