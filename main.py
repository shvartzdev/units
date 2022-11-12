import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('2019.csv')
    print(df.columns)
    df = df.rename(columns = {'Overall rank' : 'overall_rank', 'Country or region': 'region', 'GDP per capita' : 'gdp'})
    print(df.columns)

