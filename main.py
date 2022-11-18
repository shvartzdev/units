import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('2019.csv')
    print(df.describe())
    df = df.rename(columns = {'Overall rank' : 'overallRank',
                              'Country or region': 'region',
                              'Score' : 'score',
                              'GDP per capita' : 'gdp',
                              'Social support' : 'socialSupport',
                              'Healthy life expectancy' : 'healthyLifeExpectancy',
                              'Freedom to make life choices' : 'freedomForChoices',
                              'Generosity' : 'generosity',
                              'Perceptions of corruption' : 'corruptionLevel'})

    corruptionLevel = df \
        .groupby(['region', 'score'], as_index=False) \
        .aggregate({'corruptionLevel': 'sum'}) \
        .sort_values('corruptionLevel', ascending=False)

    corruptionLevel.plot(y='corruptionLevel', x='region')
    plt.show()
