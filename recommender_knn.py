from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

cities = ['sparti', 'kalamata', 'tripoli', 'larisa', 'larisa', 'tripoli', 'athens', 'kalamata', 'athens', 'athens', 'sparti', 'larisa', 'athens', 'kalamata', 'athens', 'kalamata', 'kalamata', 'kalamata', 'kalamata', 'tripoli']

product = ['potato', 'apple', 'tomato', 'peach', 'apple', 'apple', 'peach', 'peach', 'tomato', 'apple', 'apple', 'apple', 'peach', 'peach', 'apple', 'tomato', 'apple', 'peach', 'potato', 'tomato']

price = [0.6, 1.1, 0.5, 0.5, 0.3, 0.7, 0.4, 0.4, 0.8, 1.0, 1.0, 0.6, 0.6, 0.9, 0.8, 0.3, 1.1, 0.2, 0.4, 0.3]

quant = [12, 10, 11, 10, 14, 12, 16, 13, 12, 10, 12, 12, 10, 10, 14, 13, 15, 10, 12, 11]

buy = ['Prod3', 'Prod1', 'Prod3', 'Prod1', 'Prod3', 'Prod3', 'Prod2', 'Prod1', 'Prod2', 'Prod2', 'Prod1', 'Prod1', 'Prod1', 'Prod3', 'Prod1', 'Prod3', 'Prod1', 'Prod3', 'Prod2', 'Prod1']

le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
cities_encoded=le.fit_transform(cities)
product_encoded=le.fit_transform(product)
label=le.fit_transform(buy)
features=list(zip(cities_encoded,product_encoded, price, quant))
model = KNeighborsClassifier(n_neighbors=6)

print(cities_encoded)
print(product_encoded)
print(label)
# Train the model using the training sets
model.fit(features,label)

#Predict Output
predicted= model.predict([[0, 2, 0.55, 12]]) # 0:Athens, 2:Potato
print(predicted) #Result:Prod1
