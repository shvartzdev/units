import pandas as pd
import matplotlib.pyplot as plt


def rename_underscore(name):
    return name.lower().replace(' ', '_')


if __name__ == '__main__':
    df = pd.read_csv('2019.csv')

    df = df.rename(columns=rename_underscore)

    corruptionLevel = df \
        .groupby(['country_or_region', 'score', 'social_support'], as_index=False) \
        .aggregate({'perceptions_of_corruption': 'sum'}) \
        .sort_values('perceptions_of_corruption', ascending=False)

    corruptionLevel.plot(y='perceptions_of_corruption', x='country_or_region')
    plt.show()
