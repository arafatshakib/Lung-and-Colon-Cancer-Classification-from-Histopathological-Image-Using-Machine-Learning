import tensorflow as tf

from build_model import build_model


model = build_model()

dummy_images = tf.random.normal((2, 224, 224, 3))

dummy_labels = tf.one_hot([0, 1], depth=5)

model.train_on_batch(dummy_images, dummy_labels)

print("Dry run completed successfully.")
