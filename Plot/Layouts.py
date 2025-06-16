'''
Created on 11 окт. 2021 г.

@author: Alex
'''

import numpy as np

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def subplot():
    ''' Размещение нескольких графиков
        Уступает subplots в простоте, а gridspec - в универсальности '''
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(4,2,5, sharex=ax1)
    ax3 = fig.add_subplot(427, sharex=ax1)
    ax4 = fig.add_subplot(122)
    ax4.set_title('Second column')
    ax2.text(.200, .400, "425", transform=ax2.transAxes)
    ax3.text(.200, .400, "427", transform=ax3.transAxes)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.97, hspace=0.1, wspace=0.1)
    #plt.show()

def subplots(*grid, widths=None, heights=None, spec=None):
    ''' Размещение нескольких графиков
    !!!Кажется, в данной ситуации возможна только единая конфигурация оси x.
    Причем ее можно назначить для любого окна - она распространится на все.
    Подписи при этом будут только на нижних окнах.'''
    if spec:
        fig, ax = plt.subplots(*grid, figsize=(15, 7), sharex=False,
                                width_ratios=widths, height_ratios=heights)
    else:
        fig, ax = plt.subplots(figsize=(15, 7), sharex=False,
                                width_ratios=widths, height_ratios=heights, gridspec_kw=spec)
    fig.suptitle("Super Title", fontsize=15)
    fig.subplots_adjust(left=0.04, right=0.97, bottom=0.04, top=0.95, hspace=0.1, wspace=0.1)

    if (grid == (1,)):
        ax = np.array([ax])
    else:
        ax = ax.flatten()
    #ax[2][1].xaxis.set_major_locator(ticker.IndexLocator(5, 0))
    #ax[2].xaxis.set_major_locator(ticker.LinearLocator(4))       # Override previous settings!!!
    #plt.show()

def grid(constrained=False, widths=None, heights=None):
    ''' Вроде бы наиболее универсальный способ '''
    fig = plt.figure(figsize=(5, 5),constrained_layout=constrained)
    gs = fig.add_gridspec(ncols=2, nrows=2, width_ratios=widths, height_ratios=heights)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_title('w:1, h:2')

    # Так можно, но совершенно непонятно, как передать срез в качестве параметра
    ax2 = fig.add_subplot(gs[:2, 1])
    # А так, к сожалению, нельзя
    # ax2 = fig.add_subplot(gs[range(0,2), 1])
    # По-видимому, единственный способ - передача строки с вызовом eval
    # Установка ratios, во-первых, перебивается спецификацией,
    # во-вторых, позволяет создавать только "однородные" сетки
    ax2.set_title('w:3, h:2')
    ax2.yaxis.tick_right()

    ax3 = fig.add_subplot(gs[1, 0], sharex=ax1)
    ax1.axes.xaxis.set_visible(False)
    fig.subplots_adjust(left=0.075, right=0.92, top=0.95, hspace=0.0, wspace=0.1)

def nested(constrained=False, widths=None, heights=None):
    ''' Вложенный график '''
    x = np.linspace(0, 2*np.pi, 100)

    fig = plt.figure(figsize=(5, 5), constrained_layout=constrained)
    gs = fig.add_gridspec(ncols=3, nrows=3, width_ratios=widths, height_ratios=heights)
    fig.suptitle("Nested Plot")

    ax = fig.add_subplot(gs[:, :])
    ax.plot(x, np.sin(x))

    axn = fig.add_subplot(gs[0, 2])             # Располагаемся в правом верхнем углу
    axn.grid(True)
    #axn.tick_params(labelbottom=False)          # Удаляет только цифры, но не отсечки
    #axn.set_xticklabels([])                     # То же самое
    #axn.axes.get_xaxis().set_visible(False)     # А вот это работает. Правда, исчезает и сетка!!!
    axn.set_xticks([])                          # Тоже работает с тем же эффектом
    axn.yaxis.set_tick_params(direction='in')   # "Выворачивает" только отсечки
    ticks = axn.yaxis.get_tick_params()
    axn.text(0.5, 0.5, "nested", va="center", ha="center")
    # Удивительным образом после отрисовки текст перемещается непонятно куда
    axn.plot(x, np.cos(x))

#subplot()
#subplots(3, 1, heights = [3, 1, 1], spec={'nrows':3, 'ncols':1})
#grid(widths = [1, 3], heights = [3, 1])
nested()
plt.show()
pass
