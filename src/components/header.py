import streamlit as st

def render_header():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("logo_ipaam.png", width=150)
    with col2:
        st.title("MDQ-Am: Monitoramento e Denúncias de Queimadas no Amazonas")
        st.markdown("##### Preservando nossa floresta, protegendo nosso futuro 🌳") 
