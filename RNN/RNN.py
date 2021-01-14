import matplotlib as plt
import numpy as numpy
import tensorflow as tf
import pandas as pd

def make_model():
    x_train = pd.read_csv("./datalogs/training/dataFinal.csv")
    x_test = pd.read_csv("./datalogs/testing/dataFinal.csv")
    y_train = x_train.pop("target")
    y_test = x_test.pop("target")

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=30)

    val_loss, val_acc = model.evaluate(x_test, y_test)
    print(val_loss, val_acc)

make_model()