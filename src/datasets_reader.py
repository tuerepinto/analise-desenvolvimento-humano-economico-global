import sys as _sys
_sys.path.append('../')
import pandas as pd

def read_gapminder_data():
    """
    Lê o arquivo 'gapminder_full.csv' do diretório 'datasets'.

    Retorna:
        pd.DataFrame: Os dados do arquivo CSV como um DataFrame do pandas.
    """
    file_path = '../datasets/gapminder_full.csv'
    try:
        data = pd.read_csv(file_path, sep=',', encoding='utf-8')
        print(f"Arquivo {file_path} lido com sucesso.")

        return data
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None