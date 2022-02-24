import pickle
from utils import transform_data

class Linear_regression:
    def __init__(self):
        pass
    def predict(self,x):
        X=transform_data.Transform_Data.linreg(x)
        model=pickle.load("model/linearreg.pkl")
        pred=model.predict(X)
        return pred