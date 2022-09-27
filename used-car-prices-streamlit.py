import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle 

pickle_in = open('model', 'rb')
model = pickle.load(pickle_in)

sc = np.array(pd.read_excel("scaler.xlsx"))
sc = np.delete(sc, 0, 1)
scaler = StandardScaler()
sc = scaler.fit_transform(sc)


modelYili = float(st.slider("Model Yili Nedir?", 2000,2020))
mil = float(st.slider("Arac Kac Milde?", 250000, 1))
motorHacmi = float(st.slider("Motor Hacmi Kac Litre?", 6.2, 1.3))
mpg = float(st.slider("Galon Basina Mil Orani?", 250.0, 15.0))


tahminArac = np.array([modelYili,mil,mpg,motorHacmi])
tahminArac = tahminArac.reshape(-1,4)
tahminArac = scaler.transform(tahminArac)

st.header('Fiyat Tahmini')
if st.button('HESAPLA'):
    tahminFiyat = int(model.predict(tahminArac))
    st.metric(label = "Tahmin edilen fiyat", value = str(tahminFiyat) +" Sterlin",)
