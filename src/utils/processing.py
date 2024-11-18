import pandas as pd

def process_data_batch(df, batch_size=1000):
    try:
        total_rows = len(df)
        if total_rows > batch_size:
            return df.sample(n=batch_size, weights='DenunciasTotais')
        return df
    except Exception as e:
        return df

def calculate_metrics(df):
    try:
        return {
            'total_denuncias': df['DenunciasTotais'].sum(),
            'total_municipios': len(df),
            'media_denuncias': df['DenunciasTotais'].mean()
        }
    except Exception as e:
        return {
            'total_denuncias': 0,
            'total_municipios': 0,
            'media_denuncias': 0
        } 