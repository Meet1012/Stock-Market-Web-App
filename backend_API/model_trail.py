import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from numpy import array

model = load_model("required_model.h5")


def predict_data(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    x_input = data.values[341:]
    x_input = x_input.reshape(1,-1)
    temp_input=list(x_input)
    temp_input=temp_input[0].tolist()
    lst_output = []
    n_steps = 100
    i = 0
    while i < 15:
        if temp_input > 100:
            # print(temp_input)
            x_input = np.array(temp_input[1:])
            print("{} day input {}".format(i, x_input))
            x_input = x_input.reshape(1, -1)
            x_input = x_input.reshape((1, n_steps, 1))
            # print(x_input)
            yhat = model.predict(x_input, verbose=0)
            print("{} day output {}".format(i, yhat))
            temp_input.extend(yhat[0].tolist())
            temp_input = temp_input[1:]
            # print(temp_input)
            lst_output.extend(yhat.tolist())
            i = i + 1
        else:
            x_input = x_input.reshape((1, n_steps, 1))
            yhat = model.predict(x_input, verbose=0)
            print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i = i + 1

    all_predicted = scaler.inverse_transform(lst_output)
    lst = [float(i) for i in all_predicted[:]]
    return lst
