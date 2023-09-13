import tensorflow
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from pandas_datareader import data as pdr
from datetime import datetime

model = load_model("C:/Users/meet2/OneDrive/Desktop/Projects/React_Projects/stock_market/backend_API/stock_pred.h5")

def rough():
    p = np.random.random((250,1))
    p.shape
    np.expand_dims(p[-60:],axis=0).shape

def predict_data(data):
    # end_date = datetime.now().date()
    # start_date = datetime(end_date.year - 2, end_date.month, end_date.day).date()
    # print(str(end_date), str(start_date))
    # df = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
    # data = df.filter(["Close"])
    dataset = data.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    train_data = scaled_data[:, :]
    x_all = []
    for i in range(60, len(train_data)):
        x_all.append(train_data[i-60 : i, 0])

    x_all= np.array(x_all)
    # x_all = np.reshape(x_all, (x_all.shape[0], x_all.shape[1], 1))
    predicted = model.predict(x_all)
    all_predicted = scaler.inverse_transform(predicted)
    lst = [float(i) for i in all_predicted[:]]
    return lst


# predict_data(data)
