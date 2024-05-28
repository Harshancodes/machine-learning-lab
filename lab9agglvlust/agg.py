import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram,linkage
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
df=load_iris()
data=df.data[:6]
data
def prox_matrix(data):
    n=data.shape[0]
    proxmatrix=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            proxmatrix[i][j]=np.linalg.norm(data[i]-data[j])
            proxmatrix[j][i]=proxmatrix[i][j]
    return proxmatrix
def plot_dendrogram(data,method):
    linkage_matrix=linkage(data,method=method)
    dendrogram(linkage_matrix)
    plt.title(f'dendrogram -{method} linkage')
    plt.xlabel('data points')
    plt.ylabel('distance')
    plt.show()
print("proximity matrix")
print(prox_matrix(data))

plot_dendrogram(data,'single')
plot_dendrogram(data,'complete')