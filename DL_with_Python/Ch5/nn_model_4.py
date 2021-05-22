import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

train_features = np.load('train_features.npy')
train_labels = np.load('train_labels.npy')
validation_features = np.load('validation_features.npy')
validation_labels = np.load('validation_labels.npy')
test_features = np.load('test_features.npy')
test_labels = np.load('test_labels.npy')


model = Sequential()
model.add(Dense(256, activation='relu', input_dim=4 * 4 * 512))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer=RMSprop(learning_rate=0.00002),
              loss='binary_crossentropy',
              metrics=['accuracy'],
              )

print(model.summary())
history = model.fit(train_features, train_labels,
                    epochs=30,
                    batch_size=20,
                    validation_data=(validation_features, validation_labels),
                    )


acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, 1 + len(acc))

plt.plot(epochs, acc, 'r', label='Trainning')
plt.plot(epochs, val_acc, 'r--', label='Validation')
plt.legend()
plt.title('Accuracy')
plt.show()

plt.plot(epochs, loss, 'r', label='Trainning')
plt.plot(epochs, val_loss, 'r--', label='Validation')
plt.legend()
plt.title('Loss')
plt.show()
