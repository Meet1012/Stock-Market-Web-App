import numpy as np
from sklearn.preprocessing import MinMaxScaler
import cv2

# model = load_model("C:/Users/meet2/OneDrive/Desktop/Projects/React_Projects/stock_market/backend_API/stock_pred.h5")

model = cv2.dnn.readNetFromTensorflow('C:\Users\meet2\OneDrive\Desktop\Projects\React_Projects\stock_market\backend_API\stock_pred.h5')
 

def rough():
    p = np.random.random((250,1))
    p.shape
    np.expand_dims(p[-60:],axis=0).shape

def predict_data(data):
    dataset = data.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    train_data = scaled_data[:, :]
    x_all = []
    for i in range(60, len(train_data)):
        x_all.append(train_data[i-60 : i, 0])

    x_all= np.array(x_all)
    predicted = model.predict(x_all)
    all_predicted = scaler.inverse_transform(predicted)
    lst = [float(i) for i in all_predicted[:]]
    return lst

