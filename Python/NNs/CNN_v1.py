import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshape the images to be compatible with CNNs (28x28 images, 1 color channel)
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

activation_function = 'relu'


my_model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation=activation_function, input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation=activation_function),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation=activation_function),
    layers.Flatten(),
    layers.Dense(64, activation=activation_function),
    layers.Dense(10, activation='softmax')
    ])

my_model.compile(
    optimizer= 'adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

while True:
    my_model.fit(
        train_images, train_labels,
        epochs= 5,
        batch_size= 64)

    test_loss, test_accuracy = my_model.evaluate(test_images, test_labels)
    print(f'Acc: {test_accuracy}')
    inp = input('Quit? (y/n) ')
    if inp == 'y': break