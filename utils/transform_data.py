import numpy as np


class Transform_Data:
    def __init__(self):
        pass

    def linreg(x):

        inp=[x['LSTAT'], x['INDUS'], x['NOX'], x['PTRATIO'], x['RM'], x['TAX'], x['DIS'], x['AGE']]
        result=(np.array(inp)).reshape(1,-1)
        return result


    def logreg(x):

        inp=[x["rate_marriage"],x["age"],x["educ"],x["occupation"]]
        #inp=[22,22,22,22]
        result=(np.array(inp)).astype(np.float64).reshape(1,-1)
        return result
    
    def dectree(x):
                    
        inp= [x["Pclass"],x["Sex"],x["SibSp"],x["Parch"],x["Fare"]]
        result=(np.array(inp)).reshape(1,-1)
        return result