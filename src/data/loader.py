import streamlit as st
import pandas as pd
import json

@st.cache_data(ttl=3600)
def load_data():
    try:
        focos_por_municipio = {}
        
        with open('geojsoninpe.geojson') as f:
            data = json.load(f)
            
            for feature in data['features']:
                props = feature['properties']
                coords = feature['geometry']['coordinates']
                
                if not all(k in props for k in ['Municipio', 'DataHora', 'RiscoFogo', 'FRP']):
                    continue
                    
                municipio = props['Municipio']
                
                if municipio not in focos_por_municipio:
                    focos_por_municipio[municipio] = {
                        'focos_totais': 0,
                        'risco_medio': 0,
                        'frp_total': 0,
                        'latitude': coords[1],
                        'longitude': coords[0],
                        'contagem_risco': 0
                    }
                
                focos_por_municipio[municipio]['focos_totais'] += 1
                
                if props['RiscoFogo'] != -999:
                    focos_por_municipio[municipio]['risco_medio'] += props['RiscoFogo']
                    focos_por_municipio[municipio]['contagem_risco'] += 1
                
                focos_por_municipio[municipio]['frp_total'] += props.get('FRP', 0)
        
        df = pd.DataFrame([
            {
                'municipio': k,
                'DenunciasTotais': v['focos_totais'],
                'risco_medio': v['risco_medio'] / v['contagem_risco'] if v['contagem_risco'] > 0 else 0,
                'frp_total': v['frp_total'],
                'latitude': v['latitude'],
                'longitude': v['longitude']
            }
            for k, v in focos_por_municipio.items()
        ])
        
        df['municipio'] = df['municipio'].astype('category')
        df['DenunciasTotais'] = df['DenunciasTotais'].astype('int32')
        df['risco_medio'] = df['risco_medio'].astype('float32')
        df['frp_total'] = df['frp_total'].astype('float32')
        df['latitude'] = df['latitude'].astype('float32')
        df['longitude'] = df['longitude'].astype('float32')
        
        return df

    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return pd.DataFrame() 