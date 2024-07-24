import pandas as pd
import os

# Dados de exemplo com nulos, duplicados e strings erradas
data = {
    'ID': [1, 2, 3, 4, 5, 5, 6, None],
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Eva', 'Foobar', None],
    'Idade': [23, 34, None, 28, 22, 22, 'twenty', 45],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Porto Alegre', 'Unknown', None]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Diretório onde o arquivo será salvo
directory = 'C:\\teste2\\teste'
os.makedirs(directory, exist_ok=True)  # Cria o diretório se não existir

# Caminho completo do arquivo
file_path = os.path.join(directory, 'exemplo_dados_erroneos.xlsx')

# Salvando o DataFrame em um arquivo Excel
df.to_excel(file_path, index=False)

print(f"Arquivo salvo em: {file_path}")
