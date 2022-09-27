import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle 

pickle_in = open('model', 'rb')
model = pickle.load(pickle_in)

sc = np.array(pd.read_excel("scaler.xlsx"))
sc = np.delete(sc, 0, 1)
scaler = StandardScaler()
scaler.fit_transform(sc)
   
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
      
