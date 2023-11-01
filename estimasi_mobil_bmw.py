import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_bmw.sav', 'rb'))

st.title('Estimasi harga mobil bekas BMW')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Mobil')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year,mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi harga mobil bekas Toyota dalam ponds :', predict)