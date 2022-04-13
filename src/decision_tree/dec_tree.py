import pickle
import numpy as np
from utils import transform_data

class Decision_tree:
    def __init__(self):
        pass
    def predict(self,x):
        X=transform_data.Transform_Data.dectree(x)
        model=pickle.load(open("model/dec_tree.pkl","rb"))
        pred=model.predict(X)
        return pred