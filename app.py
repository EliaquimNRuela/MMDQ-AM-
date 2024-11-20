import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
from src.components import header, metrics, map, charts
from src.data.loader import load_data
from src.utils.processing import process_data_batch, calculate_metrics

st.set_page_config(
    page_title="MDQ-Am: Monitoramento e Denúncias de Queimadas no Amazonas",
    layout="wide",
)

with open('src/styles/main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    header.render_header()
    
    try:
        df = load_data()
        metrics_data = calculate_metrics(df)
        df_processed = process_data_batch(df)
        
        if df.empty:
            st.warning("Nenhum dado encontrado.")
        else:
            metrics.render_metrics_dashboard(metrics_data)
            map.render_map(df_processed)
            
            with st.container():
                st.plotly_chart(
                    charts.create_top_municipalities_chart(df_processed),
                    use_container_width=True,
                    config={'displayModeBar': False}
                )

    except Exception as e:
        st.error(f"Erro na aplicação: {str(e)}")

st.markdown("""
### DENUNCIE QUEIMADAS!

Sua denúncia é fundamental para preservarmos a Amazônia <3
""")

st.markdown("""
---
<div style='text-align: center; color: #666;'>
    © 2024 Amazônia - Desenvolvido por estudantes da FMF Wyden
</div>
""", unsafe_allow_html=True)
