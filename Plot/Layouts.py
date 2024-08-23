'''
Created on 11 окт. 2021 г.

@author: Alex
'''

import numpy as np

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.ticker as ticker

def subplot():
    ''' Размещение нескольких графиков '''
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(4,1,3, sharex=ax1)
    ax3 = fig.add_subplot(414, sharex=ax1)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.97, hspace=0.1, wspace=0.1)
    #plt.show()

def subplots():
    ''' Размещение нескольких графиков
    !!!Кажется, в данной ситуации возможна только единая конфигурация оси x.
    Причем ее можно назначить для любого окна - она распространится на все.
    Подписи при этом будут только на нижних окнах.'''
    fig, ax = plt.subplots(3, 2, figsize=(15, 7), sharex=False)
    fig.suptitle("Super Title", fontsize=15)
    fig.subplots_adjust(left=0.04, right=0.97, bottom=0.04, top=0.96, hspace=0.2, wspace=0.1)

    #ax[2][1].xaxis.set_major_locator(ticker.IndexLocator(5, 0))
    ax[1][0].xaxis.set_major_locator(ticker.LinearLocator(4))       # Override previous settings!!!
    #plt.show()

def grid1():
    fig = plt.figure(figsize=(9, 4), constrained_layout=False)
    gs = fig.add_gridspec(4, 1)
    ax1 = fig.add_subplot(gs[0:2, 0])
    ax2 = fig.add_subplot(gs[2, 0], sharex=ax1)
    ax3 = fig.add_subplot(gs[3, 0], sharex=ax1)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.97, hspace=0.0, wspace=0.1)
    ax1.axes.xaxis.set_visible(False)
    ax2.axes.xaxis.set_visible(False)
    #plt.show()

def grid2():
    fg = plt.figure(figsize=(5, 5),constrained_layout=True)
    widths = [1, 3]
    heights = [2, 0.7]
    gs = fg.add_gridspec(ncols=2, nrows=2, width_ratios=widths, height_ratios=heights)
    ax_1 = fg.add_subplot(gs[0, 0])
    ax_1.set_title('w:1, h:2')
    ax_2 = fg.add_subplot(gs[0, 1])
    ax_2.set_title('w:3, h:2')
    ax_3 = fg.add_subplot(gs[1, 0])
    ax_3.set_title('w:1, h:0.7')
    ax_4 = fg.add_subplot(gs[1, 1])
    ax_4.set_title('w:3, h:0.7')

#subplot()
subplots()
#grid1()
plt.show()
pass
