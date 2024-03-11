import pandas as pd

# Carregar o arquivo CSV com os códigos de vendedor
df_vendedores = pd.read_csv('C:/Users/taian.rosa/Desktop/vendedores_plano.csv')

# Carregar o arquivo CSV com os planos
df_planos = pd.read_csv('C:/Users/taian.rosa/Desktop/planos.csv',)

# Criar todas as combinações possíveis entre os DataFrames usando uma função lambda
df_resultado = pd.DataFrame(
    [(vendedor, plano) for vendedor in df_vendedores['Codigo'] for plano in df_planos['Plano Comercial'] if pd.notnull(vendedor) and pd.notnull(plano)],
    columns=['Codigo', 'Plano Comercial']
)

# Salvar o resultado em um novo arquivo CSV
df_resultado.to_excel('C:/Users/taian.rosa/Desktop/resultado.xlsx', index=False)
