def data_processing_clear(dataframe):
    """
    Processa o DataFrame para remover linhas ausentes.

    Args:
        dataframe (pd.DataFrame): O DataFrame a ser processado.

    Returns:
        pd.DataFrame: O DataFrame sem linhas ausentes.
    """
    try:
        print("Valores ausentes por coluna:")
        print(dataframe.isnull().sum())
        print(f"\nTotal de linhas com valores ausentes: {dataframe.isnull().any(axis=1).sum()}")
        cleaned_data = dataframe.dropna()
        print("Linhas com valores ausentes removidas com sucesso.")
        return cleaned_data
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")
        return dataframe   

def data_processing_clear_duplicates(dataframe):
    """
    Processa o DataFrame para remover linhas duplicadas.

    Args:
        dataframe (pd.DataFrame): O DataFrame a ser processado.

    Returns:
        pd.DataFrame: O DataFrame sem linhas duplicadas.
    """
    try:
        total_duplicates = dataframe.duplicated().sum()
        duplicates_by_country_year = dataframe.duplicated(subset=['country', 'year']).sum()
        print(f"Total de linhas duplicadas: {total_duplicates}")
        print(f"Duplicatas por país e ano: {duplicates_by_country_year}")
        
        cleaned_data = dataframe.drop_duplicates()
        print("Linhas duplicadas removidas com sucesso.")
        return cleaned_data
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")
        return dataframe