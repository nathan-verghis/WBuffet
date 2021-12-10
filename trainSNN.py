import numpy as numpy
import tensorflow as tf
import pandas as pd
import csv

def make_model():
    x_train = pd.read_csv("./datalogs/training/dataFinal.csv")
    x_test = pd.read_csv("./datalogs/testing/dataFinal.csv")
    y_train = x_train.pop("target")
    y_test = x_test.pop("target")
    print("Data successfully loaded!")

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

    print("Begin training...")

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=30)

    val_loss, val_acc = model.evaluate(x_test, y_test)
    print()
    print()
    print("NN loss : accuracy")
    print(val_loss, val_acc)
    return model


    print("Generating Model...")
    model = make_model()

    print("Saving model")

    # Serialize model to JSON
    model_json = model.to_json()
    with open("./model/model.json", "w") as json_file:
        json_file.write(model_json)

    # Serialize weights to HDF5
    model.save_weights("./model/model.h5")
    print("Model successfully saved!")