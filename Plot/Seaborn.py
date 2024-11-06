'''
Created on 3 нояб. 2022 г.
@author: stalker

Некая надстройка над matplotlib. По-видимому, слишком высокоуровневая.
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Устанавливаем тему по умолчанию:
sns.set_theme()

# Загружаем набор данных для примера:
tips = sns.load_dataset('tips')
# Строим график:
sns.relplot(
    data=tips,
    x='total_bill',
    y='tip',
    col='time',
    hue='sex',
    style='smoker',
    size='size');

penguins = sns.load_dataset("penguins")
def plots(data):
    ''' Различные виды графиков '''
    sns.relplot(data=data,
                kind='line',
                x='body_mass_g',
                y='flipper_length_mm',
                #col='island',        # несколько
                #row='sex',           # графиков
                style='island',       # один
                size='sex',           # график
                hue='species',
                errorbar=None,
                facet_kws={'sharex': False});

    # Линейные графики
    sns.lmplot(data=data,
                x='body_mass_g',
                y='flipper_length_mm',
                col='island',
                row='sex',
                hue='species');

    # Построение распределений
    sns.displot(data=data,
                x='body_mass_g',
                hue='sex',
                col='species',
                bins=30,
                kde=True);

    # Категориальные данные (kind = 'strip')
    sns.catplot(data=data,
                x='species',
                y='body_mass_g', 
                hue='sex');
    sns.catplot(data=data,
                x='species',
                y='body_mass_g',
                hue='sex',
                kind='box'          # ящики с усами
                );
    # Более низкоуровневая ф-ция (на уровне Axes)
    # Не может разграничивать область всей картинки на подграфики, как это умеет catplot()
    sns.boxplot(data=data,
                x='species',
                y='body_mass_g',
                hue='sex');
    # По сути, catplot() использует boxplot() как рабочий инструмент,
    # для создания графиков в каждой отдельной ячейки строки или столбца
    sns.catplot(data=data,
                x='species',
                y='body_mass_g',
                col='island',
                hue='sex',
                kind='box');
    # Если переменных больше чем две, то лучше воспользоваться функцией pairplot(),
    # которая показывает все парные и индивидуальные распределения:
    sns.pairplot(data, hue='sex')
    # Более тонкие настройки
    g = sns.PairGrid(data, hue="species")
    g.map_upper(sns.histplot, bins=30)
    g.map_lower(sns.kdeplot, bw_adjust=0.7)
    g.map_diag(sns.histplot, kde=True);

def heatmap(df):
    ''' И еще один график со своей спецификой - тепловая карта. '''
    plt.figure(figsize=(12,6))
    hmap = sns.heatmap(df.corr(),          # матрица корреляций
                       cmap='BrBG',
                       fmt='.2f',
                       linewidths=2,
                       annot=True)
    hmap.set_title("HeatMap")

plots(penguins)
heatmap(penguins)
plt.show()

pass
