import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data = pd.read_excel("used-car-prices.xlsx")
data.drop(["transmission","tax"],axis=1,inplace=True)
data = data[data["year"]>1999]
data = data.sort_values("price",ascending=False).iloc[75:]

y = data['price'].values
x = data.drop('price',axis=1).values

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=.3,random_state=10)

scaler = StandardScaler()

sc = pd.DataFrame(xtrain)
sc.to_excel("scaler.xlsx")

xtrain = scaler.fit_transform(xtrain)
xtest = scaler.transform(xtest)

model = Sequential()
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")
model.fit(x=xtrain, y=ytrain, validation_data=(xtest,ytest), batch_size=100, epochs=200)

predict = model.predict(xtest)
hata = mean_absolute_error(ytest,predict)/ytest.mean()
print(f"hata orani = {hata}")

import pickle
pickle_out = open("model", "wb")
pickle.dump(model, pickle_out)
pickle_out.close()

