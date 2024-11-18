import streamlit as st 
import pandas as pd
import pydeck as pdk
import json 

st.title("MDQ-AM: Monitoramento e Denucias de Queimadas no Amazonas")

# Exibição da tabela com os dados
st.subheader('Quantidade de Denúncias por municipio')
df3 = pd.read_json('MDQ.json')

layer = pdk.Layer(
    'ScatterplotLayer',
    data=df3,
    get_position='coordinates',
    get_fill_color='[255, 0, 0, 150]',
    get_radius='DenunciasTotais * 350',
    pickable=True,
    auto_highlight=True
)
view_state = pdk.ViewState(
    latitude=-3.7,
    longitude=-60.1,
    zoom=3,
    pitch=50
)
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{municipio}\nTotal de denuncias: {DenunciasTotais}"}
))

st.title('Quantidades de queimadas do primeiro semestre, por municipio.')
dados_json = '''
[
{"municipio": "Alvarães", "DenunciasTotais": 45, "QuantidadeQueimadas": 413, "coordinates": [-65.775, -3.22727]}, {"municipio": "Amaturá", "DenunciasTotais": 30, "QuantidadeQueimadas": 332, "coordinates": [-68.1983, -3.37444]}, {"municipio": "Anamã", "DenunciasTotais": 60, "QuantidadeQueimadas": 540, "coordinates": [-61.3965, -3.56697]}, {"municipio": "Anori", "DenunciasTotais": 10, "QuantidadeQueimadas": 219, "coordinates": [-61.6586, -3.77141]}, {"municipio": "Apuí", "DenunciasTotais": 90, "QuantidadeQueimadas": 490, "coordinates": [-59.8711, -7.19456]}, {"municipio": "Atalaia do Norte", "DenunciasTotais": 25, "QuantidadeQueimadas": 503, "coordinates": [-70.1963, -4.37028]}, {"municipio": "Autazes", "DenunciasTotais": 85, "QuantidadeQueimadas": 272, "coordinates": [-58.1364, -3.5788]}, {"municipio": "Barcelos", "DenunciasTotais": 15, "QuantidadeQueimadas": 176, "coordinates": [-62.9247, -0.977778]}, {"municipio": "Barreirinha", "DenunciasTotais": 55, "QuantidadeQueimadas": 324, "coordinates": [-57.0672, -2.79278]}, {"municipio": "Benjamin Constant", "DenunciasTotais": 40, "QuantidadeQueimadas": 295, "coordinates": [-70.0284, -4.3774]}, {"municipio": "Borba", "DenunciasTotais": 50, "QuantidadeQueimadas": 412, "coordinates": [-59.5875, -4.3918]}, {"municipio": "Boca do Acre", "DenunciasTotais": 65, "QuantidadeQueimadas": 538, "coordinates": [-67.3967, -8.75333]}, {"municipio": "Boa Vista do Ramos", "DenunciasTotais": 25, "QuantidadeQueimadas": 195, "coordinates": [-59.0623, -2.97444]}, {"municipio": "Canutama", "DenunciasTotais": 90, "QuantidadeQueimadas": 432, "coordinates": [-64.3958, -6.52583]}, {"municipio": "Carauari", "DenunciasTotais": 20, "QuantidadeQueimadas": 303, "coordinates": [-66.9039, -4.88278]}, {"municipio": "Careiro", "DenunciasTotais": 35, "QuantidadeQueimadas": 254, "coordinates": [-60.3619, -3.76833]}, {"municipio": "Careiro da Várzea", "DenunciasTotais": 45, "QuantidadeQueimadas": 167, "coordinates": [-59.8247, -3.31778]}, {"municipio": "Codajás", "DenunciasTotais": 80, "QuantidadeQueimadas": 399, "coordinates": [-62.065, -3.83778]}, {"municipio": "Coari", "DenunciasTotais": 55, "QuantidadeQueimadas": 495, "coordinates": [-63.141, -4.0853]}, {"municipio": "Envira", "DenunciasTotais": 10, "QuantidadeQueimadas": 246, "coordinates": [-70.0371, -7.4386]}, {"municipio": "Eirunepé", "DenunciasTotais": 70, "QuantidadeQueimadas": 323, "coordinates": [-69.8661, -6.66028]}, {"municipio": "Guajará", "DenunciasTotais": 60, "QuantidadeQueimadas": 287, "coordinates": [-72.5914, -7.53917]}, {"municipio": "Humaitá", "DenunciasTotais": 45, "QuantidadeQueimadas": 189, "coordinates": [-63.0383, -7.51148]}, {"municipio": "Iranduba", "DenunciasTotais": 50, "QuantidadeQueimadas": 391, "coordinates": [-60.1953, -3.2875]}, {"municipio": "Ipixuna", "DenunciasTotais": 85, "QuantidadeQueimadas": 187, "coordinates": [-71.694, -7.0575]}, {"municipio": "Itacoatiara", "DenunciasTotais": 65, "QuantidadeQueimadas": 481, "coordinates": [-58.4438, -3.1469]}, {"municipio": "Itamarati", "DenunciasTotais": 35, "QuantidadeQueimadas": 336, "coordinates": [-68.2478, -6.43806]}, {"municipio": "Japurá", "DenunciasTotais": 70, "QuantidadeQueimadas": 230, "coordinates": [-66.9161, -1.88028]}, {"municipio": "Juruá", "DenunciasTotais": 50, "QuantidadeQueimadas": 253, "coordinates": [-66.0719, -3.48444]}, {"municipio": "Jutaí", "DenunciasTotais": 55, "QuantidadeQueimadas": 331, "coordinates": [-66.7597, -2.75722]}, {"municipio": "Lábrea", "DenunciasTotais": 60, "QuantidadeQueimadas": 327, "coordinates": [-64.7872, -7.25861]}, {"municipio": "Manaus", "DenunciasTotais": 25, "QuantidadeQueimadas": 456, "coordinates": [-60.0112, -3.0823]}, {"municipio": "Manacapuru", "DenunciasTotais": 70, "QuantidadeQueimadas": 319, "coordinates": [-60.6358, -3.3186]}, {"municipio": "Manicoré", "DenunciasTotais": 50, "QuantidadeQueimadas": 412, "coordinates": [-61.3077, -5.80429]}, {"municipio": "Maraã", "DenunciasTotais": 55, "QuantidadeQueimadas": 220, "coordinates": [-65.5788, -1.85368]}, {"municipio": "Maués", "DenunciasTotais": 35, "QuantidadeQueimadas": 280, "coordinates": [-57.7275, -3.3786]}, {"municipio": "Nova Olinda do Norte", "DenunciasTotais": 80, "QuantidadeQueimadas": 503, "coordinates": [-59.0942, -3.89222]}, {"municipio": "Novo Aripuanã", "DenunciasTotais": 25, "QuantidadeQueimadas": 187, "coordinates": [-60.3797, -5.12556]}, {"municipio": "Parintins", "DenunciasTotais": 45, "QuantidadeQueimadas": 340, "coordinates": [-56.7433, -2.6303]}, {"municipio": "Pauini", "DenunciasTotais": 70, "QuantidadeQueimadas": 217, "coordinates": [-67.6739, -7.71361]}, {"municipio": "Presidente Figueiredo", "DenunciasTotais": 75, "QuantidadeQueimadas": 275, "coordinates": [-60.0284, -2.03763]}, {"municipio": "Santa Isabel do Rio Negro", "DenunciasTotais": 85, "QuantidadeQueimadas": 488, "coordinates": [-65.0025, -0.410278]}, {"municipio": "Santo Antônio do Içá", "DenunciasTotais": 75, "QuantidadeQueimadas": 294, "coordinates": [-67.9289, -3.095]}, {"municipio": "São Gabriel da Cachoeira", "DenunciasTotais": 70, "QuantidadeQueimadas": 350, "coordinates": [-67.0834, -0.11633]}, {"municipio": "São Paulo de Olivença", "DenunciasTotais": 85, "QuantidadeQueimadas": 206, "coordinates":[-3.45861, -68.9275]}, {"municipio": "Silves", "DenunciasTotais": 9, "QuantidadeQueimadas": 60, "coordinates": [-58.2139, -2.84083]}, {"municipio": "Tabatinga", "DenunciasTotais": 7, "QuantidadeQueimadas": 85, "coordinates": [-69.9358, -4.2222]}, {"municipio": "Tapauá", "DenunciasTotais": 10, "QuantidadeQueimadas": 58, "coordinates": [-63.1884, -5.62234]}, {"municipio": "Tefé", "DenunciasTotais": 7, "QuantidadeQueimadas": 41, "coordinates": [-64.7038, -3.3558]}, {"municipio": "Tonantins", "DenunciasTotais": 5, "QuantidadeQueimadas": 78, "coordinates": [-67.7914, -2.87333]}, {"municipio": "Uarini", "DenunciasTotais": 4, "QuantidadeQueimadas": 46, "coordinates": [-65.2631, -2.99194]}, {"municipio": "Urucará", "DenunciasTotais": 6, "QuantidadeQueimadas": 66, "coordinates": [-57.7709, -2.53861]}, {"municipio": "Urucurituba", "DenunciasTotais": 3, "QuantidadeQueimadas": 73, "coordinates": [-58.1492, -3.12611]}
]
'''

dados = json.loads(dados_json)

# Criar um DataFrame a partir dos dados JSON
df = pd.DataFrame(dados)

# Ajustar o tamanho da elevação com base na quantidade de atendimentos
max_atendimentos = df["QuantidadeQueimadas"].max()
df["elevation"] = df["QuantidadeQueimadas"] / max_atendimentos * 1000  # Escalar a elevação para um valor visível

# Definir a camada do mapa utilizando Pydeck
column_layer = pdk.Layer(
    "ColumnLayer",
    data=df,
    get_position=["coordinates[0]", "coordinates[1]"],
    elevation_scale=100,  # Ajustar a escala de elevação
    radius=300,  # Raio da coluna
    get_fill_color=["255", "140", "0", "140"],  # Cor da coluna com transparência
    pickable=True,
    auto_highlight=True,
)

# Configurar a visualização inicial do mapa
view_state = pdk.ViewState(
    latitude=-3.7,
    longitude=-60.1,
    zoom=6,
    pitch=80,  # Ajustar a inclinação
    #bearing=60,  # Ajustar a direção
)

# Configurar o tooltip
tooltip = {
    "html": "<b>{municipio}</b><br>Queimadas em um mes: <b>{QuantidadeQueimadas}</b>",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

# Renderizar o mapa usando Streamlit e Pydeck
st.pydeck_chart(pdk.Deck(
    layers=[column_layer],
    initial_view_state=view_state,
    tooltip=tooltip
))
