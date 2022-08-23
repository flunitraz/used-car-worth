import numpy as np
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

# for i in range(40,80):
#     arac = xtest[i]
#     arac = arac.reshape(-1,4)
#     print(f"\ntahmin edilen fiyat = {model.predict(arac)} \nolmasi gereken = {ytest[i]}")
    
while True:
    try:
        print("\n==========================================================")
        print("fiyat tahmini yapilmasi icin gerekli kriterleri belirleyin")
        print("==========================================================")
        # model yili mil mpg motor hacmi
        modelYili = int(input("model yili: "))
        mil = int(input("yapilan mil: "))
        mpg = float(input("yakit tuketimi (mpg): "))
        motorHacmi = float(input("aracin motor hacmi: "))
        
    except:
        print("\nhatali veya eksik kriter girdiniz")
        continue

    if modelYili<1999 or modelYili>2024:
        print("\ngecerli model yili giriniz")
        continue
    
    if motorHacmi>20 or motorHacmi<=0:
        print("\nmotor hacmini litre cinsinden giriniz (ornek= 3.5, 1.2)")
        continue  
    else:
        tahminArac = np.array([modelYili,mil,mpg,motorHacmi])
        tahminArac = tahminArac.reshape(-1,4)
        tahminArac = scaler.transform(tahminArac)
        print(f"\ntahmin edilen fiyat = {model.predict(tahminArac)}")
        
        devam = input("baska sorgu yapmak istiyorsaniz e yazin..... ")
        if devam == 'e':
            continue
        else:
            break
            
        





