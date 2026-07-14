Week 2 Progress Report (Model & Training)
Branch
feature/model-training

Tasks Completed

1. Implemented CNN Model

Implemented the complete CNN architecture using TensorFlow/Keras Sequential API.

Included:

Conv2D
MaxPooling
Flatten
Dense
Dropout

2. Model Compilation

Compiled the model using:

Optimizer:
Adamax

Learning Rate:
0.001

Loss:
categorical_crossentropy

Metric:
accuracy

3. Dry Run Testing

Performed a dry run using a very small sample dataset.

Verified:

Model builds successfully
No tensor shape mismatch
Forward propagation works
Training starts normally
4. Model Summary Verification

Generated model summary.

Verified:

Number of parameters
Output shapes
Layer ordering
Challenges
Checked input dimensions.
Verified output layer size equals 5 classes.
Ensured compatibility with ImageDataGenerator.
Files Committed
model/
    build_model.py

model/
    test_model.py

requirements.txt

build_model.py:

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.optimizers import Adamax


def build_model():

    model = Sequential()

    model.add(
        Conv2D(
            64,
            (3, 3),
            activation='relu',
            padding='same',
            input_shape=(224, 224, 3)
        )
    )

    model.add(MaxPooling2D((2, 2)))

    model.add(
        Conv2D(
            128,
            (3, 3),
            activation='relu',
            padding='same'
        )
    )

    model.add(MaxPooling2D((2, 2)))

    model.add(
        Conv2D(
            256,
            (3, 3),
            activation='relu',
            padding='same'
        )
    )

    model.add(MaxPooling2D((2, 2)))

    model.add(
        Conv2D(
            512,
            (3, 3),
            activation='relu',
            padding='same'
        )
    )

    model.add(MaxPooling2D((2, 2)))

    model.add(Flatten())

    model.add(Dense(256, activation='relu'))

    model.add(Dropout(0.5))

    model.add(Dense(5, activation='softmax'))

    optimizer = Adamax(learning_rate=0.001)

    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


if __name__ == "__main__":

    model = build_model()

    model.summary()
