import streamlit as st
import pydeck as pdk

def create_map_layer(df):
    map_data = df[['latitude', 'longitude', 'DenunciasTotais', 'municipio']].copy()
    
    return pdk.Layer(
        "HeatmapLayer",
        data=map_data,
        get_position=['longitude', 'latitude'],
        get_weight="DenunciasTotais",
        radius_pixels=60,
        color_range=[
            [65, 182, 196, 180],
            [227, 26, 28, 180],
            [189, 0, 38, 180],
        ],
        pickable=True
    )

def render_map(df_processed):
    map_layer = create_map_layer(df_processed)
    view_state = pdk.ViewState(
        latitude=-3.7,
        longitude=-60.1,
        zoom=5,
        pitch=0,
        bearing=0
    )
    
    st.pydeck_chart(pdk.Deck(
        layers=[map_layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/dark-v10",
        tooltip={"html": "<b>{municipio}</b><br>Denúncias: <b>{DenunciasTotais}</b>"}
    )) 