import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter
df=pd.read_csv('fruits.csv')
df.head()
df.describe()
df.info()
df['fruit_name'].isna
df['fruit_name'] = df['fruit_name'].replace({'apple':1,'mandarin':2,'orange':3,'lemon':4})
y=df['fruit_label'].values
X=df[['fruit_name','mass','width','height','color_score']].values	
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
from sklearn.neighbors import KNeighborsClassifier

k=KNeighborsClassifier(n_neighbors=3)
k
k.fit(X_train,y_train)
pred=k.predict(X_test)
pred
accuracy = np.sum(pred == y_test) / len(y_test)
print(accuracy)
def manh(x1,x2):
    d=np.sum(np.abs(x1-x2))
    return d
class KNN:
    def __init__(self,k=3):
        self.k=k
    def fit(self,X_train,y_train):
        self.X_train=X_train
        self.y_train=y_train
    def predict(self,X_test):
        pred=[self.p(i) for i in X_test]
        return pred
    def p(self,X_test):
        dis=[manh(X_test,X_train) for X_train in self.X_train]
        k_ind=np.argsort(dis)[:self.k]
        val=[self.y_train[i] for i in k_ind]
        mc=Counter(val).most_common()
        return mc[0][0]
model=KNN(5)
model.fit(X_train,y_train)
predicts=model.predict(X_test)
print(predicts)
accuracy=np.sum(predicts==y_test)/len(y_test)
print(accuracy)