import numpy as np


class Transform_Data:
    def __init__(self):
        pass
    def linreg(x):

        inp=[x['LSTAT'], x['INDUS'], x['NOX'], x['PTRATIO'], x['RM'], x['TAX'], x['DIS'], x['AGE']]
        result=(np.array(inp)).reshape(1,-1)
        return result

    