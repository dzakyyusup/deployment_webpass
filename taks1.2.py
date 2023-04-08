#library
import streamlit as st

#write
st.title('HAI SELAMAT DATANG DI APK PERHITUNGAN')
st.title('GUA BAKAL BANTUIN LU BUAT NGITUNG HEHE :sunglasses:')

# BILANGAN PERTAMA
number1 = st.number_input('masukan bilangan pertama')
st.write(f'bilangan pertama adalah', number1)
#BILANGAN KEDUA
number2 = st.number_input('masukan bilangan kedua')
st.write(f'bilangan kedua adalah', number2)
hasil= number1*number2
#button

if st.button('hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('silakan tekan tombol hitung')
    
import numpy as np
array1 = np.random.randint(10,40, size=(10,))
array2 = np.random.randint(10,40, size=(10,))

import pandas as pd
st.dataframe(pd.DataFrame({'kelas A': array1,
                           'kelas B': array2
                           })
             )