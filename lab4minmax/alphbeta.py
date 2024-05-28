
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the Titanic dataset
data = pd.read_csv('titanic.csv')

# Preprocessing
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = data.dropna(subset=['Age', 'Fare'])

X = data[['Pclass', 'Sex', 'Age', 'Fare']]
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Naive Bayes classifier
model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

     
Accuracy: 0.7674418604651163