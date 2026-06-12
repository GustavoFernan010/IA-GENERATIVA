#import numpy as np 
#from sklearn.tree import DecisionTreeClassifier

#X= np.array([
 # [1,5],
  #[2,4],
  #[3,3],
  #[4,1],
  #[5,0],
#])

#y= np.array ([1,1,1,0,0])
#modelo = DecisionTreeClassifier()
#modelo.fit(X,y)

#print(modelo.predict([[1,0]]))

#investimento de marketing
import numpy  as np
from sklearn.linear_model import LinearRegression
# investimento em mkt 1mil
X = np.array([[1],[2],[4],[5],[3]])
# vendas 
y =  np.array([2,8,4,6,5])
modelo = LinearRegression()
modelo.fit(X, y)
print(modelo.predict([[6]]))


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# Variável independente (X) e dependente (y)
X = dados_vendas[['investimento']]
y = dados_vendas['faturamento']

# Treinamento do modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Entrada do usuário
investimento_futuro = st.number_input(
    "Informe o investimento em marketing:",
    min_value=0.0,
    value=700.0
)

# Previsão
if st.button("Prever Faturamento"):
    previsao = modelo.predict([[investimento_futuro]])[0]

    st.success(
        f"Faturamento previsto para R$ {investimento_futuro:,.2f} "
        f"em investimento: R$ {previsao:,.2f}"
    )

# Exibir dados utilizados
st.subheader("Dados de Treinamento")
st.dataframe(dados_vendas)