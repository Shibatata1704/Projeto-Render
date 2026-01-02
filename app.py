import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.header('Jogando uma moeda')

# hist_button = st.button('Criar histograma') # criar um botão
# if hist_button: # se o botão for clicado
# escrever uma mensagem
#     st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

#     criar um histograma
#     fig = px.histogram(car_data, x="odometer")

#     exibir um gráfico Plotly interativo
#     st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:# se a caixa de seleção for selecionada
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncio de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)