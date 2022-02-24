import pickle
import numpy as np
from utils import transform_data

class Linear_regression:
    def __init__(self):
        pass
    def predict(self,x):
        #X=transform_data.Transform_Data.linreg(x)
        model=pickle.load(open("model/linearreg.pkl","rb"))
        arr=np.array(x)
        pred=model.predict(arr.reshape(1,-1))
        return pred