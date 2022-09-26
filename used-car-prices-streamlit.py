import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import streamlit as st

data = pd.read_excel("./used-car-prices.xlsx")
data.drop(["transmission","tax"],axis=1,inplace=True)
data = data[data["year"]>1999]
data = data.sort_values("price",ascending=False).iloc[75:]

y = data['price'].values
x = data.drop('price',axis=1).values

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=.3,random_state=10)

scaler = StandardScaler()
xtrain = scaler.fit_transform(xtrain)
xtest = scaler.transform(xtest)

model = Sequential()
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")
model.fit(x=xtrain, y=ytrain, validation_data=(xtest,ytest), batch_size=100, epochs=50)

predict = model.predict(xtest)
hata = mean_absolute_error(ytest,predict)/ytest.mean()
print(f"hata orani = {hata}")


#SIDEBAR
st.sidebar.header('USER INPUT FEATURES')
modelYili = st.sidebar.slider("Arac Kac model?", min_value=2000,max_value=2020,value=1)
mil = st.sidebar.slider("Arac kac milde?", 0,250000, 1)
motorHacmi = st.sidebar.slider("Motor Hacmi Kac Litre?", 1.3,6.2,0.1)
mpg = st.sidebar.slider("Ortalama Yakıt Tüketimi", 10.0,250.0, 1.0)

tahminArac = np.array([modelYili,mil,mpg,motorHacmi])
tahminArac = tahminArac.reshape(-1,4)
tahminArac = scaler.transform(tahminArac)

st.header('Fiyat Tahmini')
if st.button('HESAPLA'):
    st.write("# TAHMINI FIYAT")
    tahminFiyat = model.predict(tahminArac)
    st.write(tahminFiyat[0])