import os
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.ops.gen_resource_variable_ops import resource_scatter_mul_eager_fallback


conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(150, 150, 3))

print(conv_base.summary())


base_dir = '/Users/rodrigo/Downloads/cats_and_dogs_small'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')


datagen = ImageDataGenerator(rescale=1. / 255)
batch_size = 20


def extract_features(directory, sample_count):
    features = np.zeros(shape=(sample_count, 4, 4, 512))
    labels = np.zeros(shape=(sample_count))
    generator = datagen.flow_from_directory(
        directory,
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='binary')
    i = 0
    for inputs_batch, labels_batch in generator:
        features_batch = conv_base.predict(inputs_batch)
        features[i * batch_size: (i + 1) * batch_size] = features_batch
        labels[i * batch_size: (i + 1) * batch_size] = labels_batch
        i += 1
        if i * batch_size >= sample_count:
            break
    return features, labels


train_features, train_labels = extract_features(train_dir, 2000)
validation_features, validation_labels = extract_features(validation_dir, 1000)
test_features, test_labels = extract_features(test_dir, 1000)

train_features = np.reshape(train_features, (2000, 4 * 4 * 512))
print(train_features.shape, train_labels.shape)
np.save('train_features.npy', train_features)
np.save('train_labels.npy', train_labels)
validation_features = np.reshape(validation_features, (1000, 4 * 4 * 512))
print(validation_features.shape, validation_labels.shape)
np.save('validation_features.npy', validation_features)
np.save('validation_labels.npy', validation_labels)
test_features = np.reshape(test_features, (1000, 4 * 4 * 512))
print(test_features.shape, test_labels.shape)
np.save('test_features.npy', test_features)
np.save('test_labels.npy', test_labels)
