import pandas as pd
import matplotlib.pyplot as plt


def rename_underscore(name):
    return name.lower().replace(' ', '_')


# item – цена товара сейчас, year – кол-во лет
def price_with_inflation(item, year):
    rate_of_inflation = 0.17
    return item * (1 + rate_of_inflation) ** year


# возвращает значение профита с учетом обесценивания для всей колонки
def deprication(profits):
    rate_of_inflation = 0.17
    return profits - (profits * rate_of_inflation)

#возвращает размер единовременного вклада сейчас
def deposit (item, year):
    rate_of_return = 0.11
    return price_with_inflation(item, year) / (1 + rate_of_return) ** year

if __name__ == '__main__':
    df = pd.read_csv('2019.csv')

    df = df.rename(columns=rename_underscore)
    df['depricated'] = df.score.apply(deprication)

    score_level = df \
        .groupby(['country_or_region', 'score', 'depricated'], as_index=False) \
        .aggregate({'score': 'sum'}) \
        .sort_values('score', ascending=False)

    print(price_with_inflation(120000, 1))
    print(deposit(120000, 1))

    score_level.plot(y=['score','depricated'], x='country_or_region')
    plt.show()
