# Convolutional Neural Network

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim=128, activation='relu'))
classifier.add(Dense(output_dim=7, activation='softmax'))

# Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,
                                   zoom_range=0.1,
                                   shear_range=0.1,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)


# dataset has 3 classes. it contains hand gestures with its meaning
training_set = train_datagen.flow_from_directory('dataset/train_gest',
                                                 target_size=(64, 64),
                                                 batch_size=10,
                                                 shuffle=True,
                                                 color_mode="rgb",
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory('dataset/test_gest',
                                            target_size=(64, 64),
                                            batch_size=3,
                                            color_mode="rgb",
                                            class_mode='categorical')

classifier.fit_generator(training_set,
                         samples_per_epoch=160,
                         nb_epoch=20,
                         validation_data=test_set,
                         nb_val_samples=21)

classifier.save('my_model.h5')
del classifier

print("Model Trained SUCCESSFULLY...!!!")
