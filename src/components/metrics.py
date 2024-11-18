import streamlit as st

def render_metrics_dashboard(metrics):
    st.markdown("""
    <div class="metrics-dashboard">
        <div class="metrics-container">
            <div class="metric-card">
                <h3>Total de Denúncias</h3>
                <p class="metric-value">{:,}</p>
            </div>
            <div class="metric-card">
                <h3>Municípios Monitorados</h3>
                <p class="metric-value">{}</p>
            </div>
            <div class="metric-card">
                <h3>Média de Denúncias</h3>
                <p class="metric-value">{:.1f}</p>
            </div>
        </div>
    </div>
    """.format(
        metrics['total_denuncias'],
        metrics['total_municipios'],
        metrics['media_denuncias']
    ), unsafe_allow_html=True) 