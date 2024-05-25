
import pandas as pd
import numpy as np
df=pd.read_csv('fruits.csv')
df.head()
import matplotlib.pyplot as plt

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
plt.boxplot(df['width'])
 
# show plot
plt.show()
import seaborn as sn
sn.heatmap([df['width']])
plt.show()
x=df['width']
y=df['mass']
z=df['height']
plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.show()    