import os
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Flatten
from tensorflow.keras.applications.vgg16 import VGG16


conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(150, 150, 3))

conv_base.trainable = False


model = Sequential()
model.add(conv_base)
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.build((None, 150, 150, 3))
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop', metrics=['accuracy'])
print(model.summary())
print(len(model.trainable_weights))


####
base_dir = '/Users/rodrigo/Downloads/cats_and_dogs_small'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
)

test_datagen = ImageDataGenerator(rescale=1. / 255,)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')


####
history = model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=15,
    validation_data=validation_generator,
    validation_steps=50,
)

# model.save('cats_and_dogs_last_.h5')

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, 1 + len(acc))

plt.plot(epochs, acc, 'r', label='Trainning')
plt.plot(epochs, val_acc, 'r--', label='Validation')
plt.title('Accuracy')
plt.legend()
plt.show()

plt.plot(epochs, loss, 'r', label='Trainning')
plt.plot(epochs, val_loss, 'r--', label='Validation')
plt.title('Loss')
plt.legend()
plt.show()
