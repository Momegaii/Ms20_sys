import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from cals import *


class data:
    def __init__(self,data):
        self.data = pd.read_csv(*arguments, **kwargs)

lngc = 'lung_cancer.csv'
db = 'diabetes.csv'

glc = 'glcx.csv'


class Cals(data):
    def __init__(self, cal100, cal200, cal300,cal1005,cal2005,cal3005,cal1005_5,cal2005_5,cal3005_5):
        self.cal100 = df100
        self.cal200 = df200
        self.cal300 = df300
        self.cal1005 =df100_h5
        self.cal2005 =df200_h5
        self.cal3005 =df300_h5
        self.cal1005_5 =df100_h5_5
        self.cal2005_5 =df200_h5_5
        self.cal3005_5 =df300_h5_5

    
    
        x1 = self.cal100[['steps']]
        y1 = self.cal100['Burned_calories_by_wieght100lb']
     
        x2 = self.cal200[['steps']]
        y2 = self.cal200['Burned_calories_by_wieght200lb']
        
        x3 = self.cal300[['steps']]
        y3 = self.cal300['Burned_calories_by_wieght300lb']
        
        x4 = self.cal1005[['steps']]
        y4 = self.cal1005['Burned_calories_by_wieght100lb']
        
        x5 = self.cal2005[['steps']]
        y5 = self.cal2005['Burned_calories_by_wieght200lb']
        
        x6 = self.cal3005[['steps']]
        y6 = self.cal3005['Burned_calories_by_wieght300lb']
        
        x7 = self.cal1005_5[['steps']]
        y7 = self.cal1005_5['Burned_calories_by_wieght100lb']

        x8 = self.cal2005_5[['steps']]
        y8 = self.cal2005_5['Burned_calories_by_wieght200lb']

        x9 = self.cal3005_5[['steps']]
        y9 = self.cal3005_5['Burned_calories_by_wieght300lb']
    def xtrain100():
        x_train1, x_test1, y_train1, y_test1 = train_test_split(x1, y1, test_size=0.2, random_state=42)
        return x_train1, x_test1, y_train1, y_test1
    def xtrain200():
        x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y2, test_size=0.2, random_state=42)
        return x_train2, x_test2, y_train2, y_test2
    def xtrain300():
        x_train3, x_test3, y_train3, y_test3 = train_test_split(x3, y3, test_size=0.2, random_state=42)
        return x_train3, x_test3, y_train3, y_test3
    def xtrain1005():
        x_train4, x_test4, y_train4, y_test4 = train_test_split(x4, y4, test_size=0.2, random_state=42)
        return x_train4, x_test4, y_train4, y_test4
    def xtrain2005():
        x_train5, x_test5, y_train5, y_test5 = train_test_split(x5, y5, test_size=0.2, random_state=42)
        return x_train5, x_test5, y_train5, y_test5
    def xtrain3005():
        x_train6, x_test6, y_train6, y_test6 = train_test_split(x6, y6, test_size=0.2, random_state=42)
        return x_train6, x_test6, y_train6, y_test6
    def xtrain1005_5():
        x_train7, x_test7, y_train7, y_test7 = train_test_split(x7, y7, test_size=0.2, random_state=42)
        return x_train7, x_test7, y_train7, y_test7
    def xtrain2005_5():
        x_train8, x_test8, y_train8, y_test8 = train_test_split(x8, y8, test_size=0.2, random_state=42)
        return x_train8, x_test8, y_train8, y_test8
    def xtrain3005_5():
        x_train9, x_test9, y_train9, y_test9 = train_test_split(x9, y9, test_size=0.2, random_state=42)
        return x_train9, x_test9, y_train9, y_test9
        
    

class Lung_Cancer(data):
    def __init__(self,lngc):
        self.lngc = data.data(lngc)
    
    def x(self):
        pass

class diabetes(data):
    def __init__(self, db):
        self.db = data.data(db)
    
    def x(self):
        pass

class glcx(data):
    def __init__(self, glc):
        self.glc = data.data(glc)
    
    def x(self):
        pass

