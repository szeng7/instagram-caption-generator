from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import img_to_array
import argparse as ap
import pickle
import urllib
import cv2
import numpy as np

def train(train_data, dev_data, test_data):

    x_train, y_train = train_data[0], train_data[1]
    x_dev, y_dev = dev_data[0], dev_data[1]
    x_test, y_test = test_data[0], test_data[1]

    model = Sequential()
    model.add(Conv2D(64, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Flatten())
    model.add(Dense(units = 128, activation = 'relu'))
    model.add(Dense(units = 100, activation = 'sigmoid'))
    model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

    model.fit(x_train, y_train, batch_size=4, epochs=20, verbose=1, validation_data=(x_dev, y_dev))
    score = model.evaluate(x_test, y_test, verbose=1)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

def main():
    p = ap.ArgumentParser()

    p.add_argument('--train-pickle', required=False, \
        help='pickle file of training set data')
    p.add_argument('--dev-pickle', required=False, \
        help='pickle file of dev set data')
    p.add_argument('--test-pickle', required=False, \
        help='pickle file of test set data')
    ARGS = p.parse_args()

    with open(ARGS.train_pickle, "rb") as f:
        train_data = pickle.load(f)

    with open(ARGS.dev_pickle, "rb") as f:
        dev_data = pickle.load(f)

    with open(ARGS.test_pickle, "rb") as f:
        test_data = pickle.load(f)

    train(train_data, dev_data, test_data)


if __name__ == "__main__":
    main()