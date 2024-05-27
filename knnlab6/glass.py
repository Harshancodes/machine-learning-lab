import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter
df=pd.read_csv('glass.csv')
df.head()
y=df['Type'].values
# y to see you y
X=df.drop('Type',axis=1).values
# X to see your i/p
def euclidean(x1,x2):
    d=np.sqrt(np.sum(x1-x2)**2)
    return d
class KNN:
    def __init__(self,k=3):
        self.k=k
    def fit(self,X,y):
        self.X_train=X
        self.y_train=y
    def predict(self,X):
        pred=[self.p(x) for x in X]
        return pred
    def p(self,x):
        d=[euclidean(x,x_train) for x_train in self.X_train]
        k_indices=np.argsort(d)[:self.k]
        k_nearest=[self.y_train[i] for i in k_indices]
        Most_common=Counter(k_nearest).most_common()
        return Most_common[0][0]
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8)

clf=KNN(k=3)
clf.fit(X_train,y_train)
predictions=clf.predict(X_test)
print(predictions)
acc=np.sum(predictions==y_test)/len(y_test)
print(acc)       
