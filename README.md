Sistema de monitoramento e visualização de denúncias de queimadas no estado do Amazonas, desenvolvido para o IPAAM (Instituto de Proteção Ambiental do Amazonas).

## 🌳 Funcionalidades

- Visualização de mapa de calor das denúncias
- Métricas em tempo real
- Ranking dos municípios mais afetados
- Processamento automático de dados do INPE

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório

git clone https://github.com/EliaquimNRuela/MMDQ-AM.git

cd MMDQ-AM

2. Crie um ambiente virtual
   
python -m venv venv

3 - Ative o ambiente virtual

Windows:

venv\Scripts\activate

Linux/MacOS:

source venv/bin/activate

4  - rode pip install -r requirements.txt ou instale os pacotes manualmente:

streamlit>=1.28.0

pandas>=2.0.0

pydeck>=0.8.0

plotly>=5.18.0

numpy>=1.24.0

geojson>=3.0.0

5 - execute o comando:
streamlit run app.py



ADICIONAIS

## 📊 Componentes Principais

### Loader (loader.py)
- Carrega e processa dados do arquivo GeoJSON
- Cache automático com TTL de 1 hora
- Tratamento de coordenadas e métricas

### Map (map.py)
- Renderiza mapa de calor usando PyDeck
- Configuração de visualização centrada no Amazonas
- Tooltips interativos com informações municipais

### Metrics (metrics.py)
- Dashboard com métricas principais
- Cálculos automáticos de totais e médias
- Layout responsivo

### Charts (charts.py)
- Gráfico de barras dos municípios mais afetados
- Customização visual com tema IPAAM
- Ordenação automática por número de denúncias

## 🔧 Configurações

O arquivo `app.py` contém as principais configurações:
- Layout wide por padrão
- Carregamento de estilos CSS
- Tratamento de erros global

## 📝 Notas Importantes

1. O arquivo `geojsoninpe.geojson` deve estar na raiz do projeto
2. A logo do IPAAM (`logo_ipaam.png`) é necessária para o header
3. O processamento de dados é limitado a 1000 registros por padrão
4. Métricas são atualizadas automaticamente a cada hora
