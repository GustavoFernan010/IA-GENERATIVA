import streamlit as st

st.title("Tabuada")

numero = st.number_input('Digite um número', step=1, format="%d")

if st.button('Gerar tabuada'):
    st.subheader(f'Tabuada {numero}')

    for i in range(1, 11):
        resultado = numero * i
        st.write(f'{numero} x {i} = {resultado}')