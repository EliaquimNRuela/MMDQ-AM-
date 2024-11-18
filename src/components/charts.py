import plotly.express as px

def create_top_municipalities_chart(df, n=10):
    top_municipios = df.nlargest(n, 'DenunciasTotais')[['municipio', 'DenunciasTotais']]
    fig = px.bar(
        top_municipios,
        x='municipio',
        y='DenunciasTotais',
        color='DenunciasTotais',
        color_continuous_scale=['#1B4D3E', '#2D6A4F', '#4CAF50'],
        title=f'Top {n} Municípios com Mais Denúncias',
    )
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=450,
        title_x=0.5,
        title_font_size=20,
        title_font_color='#1B4D3E',
        xaxis_title="Município",
        yaxis_title="Total de Denúncias",
        xaxis_tickangle=-45,
        showlegend=False,
        xaxis=dict(gridcolor='rgba(0,0,0,0.1)', zerolinecolor='rgba(0,0,0,0.1)'),
        yaxis=dict(gridcolor='rgba(0,0,0,0.1)', zerolinecolor='rgba(0,0,0,0.1)'),
        font=dict(family="Helvetica", color='#1B4D3E')
    )
    
    for trace in fig.data:
        trace.marker.line.width = 1
        trace.marker.line.color = 'rgba(0,0,0,0.1)'

    return fig 