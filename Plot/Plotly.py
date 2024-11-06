'''
Created on 18 сент. 2020 г.
@author: Alex

Некая альтернатива seaborn (однако, не основанная на matplotlib).
По-видимому, также слишком высокоуровневая
Вообще, подобных библиотек бесчисленное множество (bokeh, bqplot, cufflinks, ...)
Следует сконцентрироваться на одной и не распыляться.
'''

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from plotly.offline import iplot
from plotly import graph_objs as go
#init_notebook_mode(connected = True)

def plotly_df(df, title = ''):
    data = [go.Scatter(
            x = df.index,
            y = df[column],
            mode = 'lines',
            name = column
        ) for column in df.columns]

    layout = dict(title = title)
    fig = dict(data = data, layout = layout)
    try:
        iplot(fig, show_link=False)
    except Exception as e:
        print(e)

users = pd.read_csv('e:/data/hour_online.csv', index_col=['Time'], parse_dates=['Time'])
plotly_df(users, title = "Online users")
pass
