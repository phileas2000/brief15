import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class DistanceTransformer(BaseEstimator, TransformerMixin):
    """
        Computes the haversine distance between two GPS points.
        Returns a copy of the DataFrame X with only one column: 'distance'.
    """
   

    def __init__(self,
                 start_lat="pickup_latitude",
                 start_lon="pickup_longitude",
                 end_lat="dropoff_latitude",
                 end_lon="dropoff_longitude"):
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_lat = end_lat
        self.end_lon = end_lon
        
        
    def fit(self, X, y=None):

        return self

      

        
    def transform(self, X, y=None):
        
        X2 = X.copy()
        X2['distance']=haversine_vectorized(X2,self.start_lat,self.start_lon,self.end_lat,self.end_lon)
        
    
        return X2[['distance']]



def transform(self, X, y=None):
        X2 = X.copy()
        hours =[]
        years =[]
        months =[]
        dows=[]
        for e in self.time_column:
            datetim = datetime.strptime(e, '%Y-%m-%d %H:%M:%S UTC')

            #self.fuseau_horaire
            datetim=datetim.astimezone()
            X_ = pd.DataFrame()
           
            hours.append(datetim.hour)
            years.append(datetim.year)
            months.append(datetim.month)
            dows.append(datetim.weekday())
            X_['hour']=hours
            X_['year']=years
            X_['month']=months
            X_['dow']=dows
        return X_[['dow', 'hour', 'month', 'year']]   