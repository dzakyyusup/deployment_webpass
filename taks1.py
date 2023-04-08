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