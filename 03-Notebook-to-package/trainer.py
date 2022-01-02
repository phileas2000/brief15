
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from encoders import *
from data import *
from utils import *

class Trainer:

    def __init__(self):
        self.pipeline= self.set_pipeline()
        self.data = get_data()

    def set_pipeline(self):
        pipe=Pipeline([('standardScaler',StandardScaler()),('linearRegression',LinearRegression())])
        self.pipe = pipe
       
   

    def run(self):
        df=self.data
        df['distance']= haversine_vectorized(df)
        df =clean_data(df)
        # set X and y
        y = df["fare_amount"]
        X = df['distance']


        # hold out
        X_train, X_val, y_train, y_val = train_test_split(X.values.reshape(-1,1), y, test_size=0.15)

        # build pipeline
        

        # train the pipeline
        self.pipe.fit(X_train,y_train)
        self.evaluate(self,X_val,y_val)
        
    def evaluate(self,X_test,y_test):
        y_pred = self.pipe.predict(X_test)
        compute_rmse(y_pred,y_test)