import pickle
import numpy as np
from utils.transform_data import Transform_Data

class Logistic_Regression:
    def __init__(self):
        pass
    def predict(self,x):
        X=Transform_Data.logreg(x)
        model=pickle.load(open("model/logisticreg.pkl","rb"))
        pred=model.predict(X)
        return pred
