import tensorflow as tf
import numpy as np
import pandas as pd
from dailySetup import dailySetup
from trainSNN import make_model


update = input("If you would like to update the model first, please press 1: ")
if int(update) == 1:
    dailySetup()
    model = make_model()
else:
    # Load json and create model
    json_file = open("./model/model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    model = tf.keras.models.model_from_json(loaded_model_json)

    # load the weights into the new model
    model.load_weights("./model/model.h5")
    print("Model successfully loaded")

# TEST
x_test = pd.read_csv("./datalogs/Jan-13-2021/dataFinal.csv")
y_test = x_test.pop("target")

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)