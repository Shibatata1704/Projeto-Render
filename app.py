import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.header('Análise interativa de anúncios de vendas de veículos')
st.write(
    'Este aplicativo permite explorar visualmente dados de anúncios de veículos, '
    'destacando relações importantes como quilometragem, preço e ano do modelo.'
)

# Histograma com botão
hist_button = st.button('Gerar histograma de quilometragem')

if hist_button:
    st.write(
        'O histograma abaixo mostra a distribuição da quilometragem (odômetro) dos veículos anunciados.'
    )

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribuição da quilometragem dos veículos',
        labels={'odometer': 'Quilometragem'}
    )

    st.plotly_chart(fig, use_container_width=True)

# Histograma de preços com checkbox
build_price_histogram = st.checkbox('Exibir histograma de preços dos veículos')

if build_price_histogram:
    st.write(
        'Este histograma mostra a distribuição dos preços dos veículos anunciados, '
        'permitindo identificar faixas de preço mais comuns e possíveis valores atípicos.'
    )

    fig = px.histogram(
        car_data,
        x='price',
        title='Distribuição dos preços dos veículos',
        labels={'price': 'Preço'},
        nbins=50
    )

    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão: odometer vs price
build_scatter = st.checkbox('Exibir gráfico de dispersão: quilometragem vs preço')

if build_scatter:
    st.write(
        'O gráfico de dispersão abaixo permite analisar a relação entre a quilometragem do veículo e o preço anunciado.'
    )

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relação entre quilometragem e preço',
        labels={
            'odometer': 'Quilometragem',
            'price': 'Preço'
        }
    )

    st.plotly_chart(fig, use_container_width=True)
    
# Gráfico de dispersão: model_year vs price
build_year_price_scatter = st.checkbox(
    'Exibir gráfico de dispersão: ano do modelo vs preço'
)

if build_year_price_scatter:
    st.write(
        'Este gráfico mostra como o preço dos veículos varia de acordo '
        'com o ano do modelo, evidenciando o efeito de depreciação.'
    )

    fig = px.scatter(
        car_data,
        x='model_year',
        y='price',
        title='Relação entre ano do modelo e preço',
        labels={
            'model_year': 'Ano do modelo',
            'price': 'Preço'
        }
    )

    st.plotly_chart(fig, use_container_width=True)
