# calculadora
import streamlit as st

st.title('Calculadora')

numero1 = st.number_input('numero')
numero2 = st.number_input('numero', step=0.1)

if st.button('RESULTADO'):
    soma = numero1 + numero2
    st.success(soma)



st.title("calculo do imc")

peso = st.number_input('peso')
altura = st.number_input('altura')

if st.button('calcular imc'):
    calculo = peso / (altura ** 2 )
    st.success(calculo)