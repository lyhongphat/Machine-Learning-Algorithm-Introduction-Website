import tensorflow as tf
from tensorflow import keras

mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

RESHAPED = 784
X_train = X_train.reshape(60000, RESHAPED)
Y_test = X_test.reshape(10000, RESHAPED)
pass

