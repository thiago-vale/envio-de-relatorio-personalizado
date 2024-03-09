import pandas as pd

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
    }


class Clean():

    def __init__(self):
        self.countries = COUNTRIES

    def country_name(self, country_id):

        """Retrieve the name of a country given its ID.

        Args:
            country_id (str): The ID of the country.

        Returns:
            str: The name of the country corresponding to the given ID.
        """
        return self.countries[country_id]
    
    def rename_columns(self, dataframe):
        
        """Rename columns of a DataFrame to snake case.

        Args:
            dataframe (pandas.DataFrame): The DataFrame to rename columns.

        Returns:
            pandas.DataFrame: The DataFrame with columns renamed to snake case.
        """

        df = dataframe.copy()
        
        def snakecase(x):
            return x.replace(" ", "_").lower()

        cols_old = list(df.columns)

        cols_new = list(map(snakecase, cols_old))
        cols_old = list(map(str.strip, cols_old))  # Removendo espaços extras

        
        # Renomeando as colunas no dataframe
        df.columns = cols_new
        
        return df