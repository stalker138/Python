'''
Created on 2 апр. 2019 г.

@author: Stalker
'''

from datetime import datetime

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def info(ax):
    ''' Основная информация по графику '''
    print("bounds", str(ax.get_xbound()), str(ax.get_ybound()))
    print("zorder:", str(ax.get_axisbelow()))
    print("scale:", ax.get_xscale(), ax.get_yscale())
    print("frame:", str(ax.get_frame_on()), str(ax.get_aspect()), str(ax.get_adjustable()))
    print("ticks:", str(ax.get_xticks()))
    tl = ax.get_xticklabels()
    print("tick labels:", tl)

def axis(ax, minor=True, margins=(), xticks=None):
    ''' Манипуляции с осями (в первую очередь - X) '''
    if minor:
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

    if margins:
        #ax.set_xmargin(margins[0])    # Расширение интервала на %
        #ax.set_ymargin(margins[1])    # Обрезание на %
        ax.margins(*margins)            # Тот же эффект (возможны различия без автошкалирования)

    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=1, width=1)

    ''' Крайне нежелательно, чтобы ticks "ПЕРЕКРЫВАЛ" bounds'''

    # Такая сложная система условий связана с множеством манипуляций
    # (конкретные значения, значения по умолчанию, отключение, возможно - что-то еще)
    if xticks:
        if not xticks[0] is None:
            ax.set_xticks(xticks[0])
            if not xticks[1] is None:
                ax.set_xticklabels(xticks[1])

def simple(ax=None, size=10):
    ''' Отрисовка различного вида графиков
        Проверка других элементов: title, text, labels, grid '''
    x = np.arange(size)
    y1 = 4*x
    y2 = np.sin(x)

    if ax:
        ax.clear()
    else:
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.suptitle('Simple Test')
        plt.show(block=False)
    ax.twin = ax.twinx()                # Два разномасштабных полотна

    ax.set_title("Графики зависимостей: y1=4*x, y2=x^2", fontsize=16)
    ax.set_xlabel("x", fontsize=14)        
    ax.set_ylabel("y1, y2", fontsize=14)
    ax.grid(which="major", linewidth=1.2)
    ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5, alpha=0.5)

    line, = ax.twin.plot(x, y2, label="y2 = x^2")
    line.set(ydata=y2-.5, color='brown')    # Перерисовать кусочек (типа [-3:]) не получится
    # Меньшее (кратное) кол-во точек 
    scs = ax.scatter(x[0:size:2], y1[0:size:2], c="red", label="y1 = 4*x")
    bars = ax.bar(x, y2-y1, bottom=x, color='green', width=0.5, zorder=1, label="bars")
    bar = bars[4]
    bar.set_color('red')
    bar.set_y(bar.xy[1]-1.)
    lines = ax.vlines(x, np.log(x+1), np.sqrt(x), colors='blue', linewidths=5, zorder=2, label="lines")

    ax.axhline(y=15, color="navy")

    ax.legend()
    ax.text(.200, .400, "Text"
            , color='blue', fontsize=16
            ,horizontalalignment='left', verticalalignment='center'
            ,transform=ax.transAxes
            )

    ax.xaxis.set_zorder(-1)         # спрятать сетку под бары (в вызове grid это не работает)
    #ax.yaxis.tick_right()           # ось справа

    ax.set_xbound(size-20, size)     # В чем отличие ???
    #ax.set_xlim(5, 11)      # Установка видимой области, перекрывает margins
    #ax.set_ybound(0, 200)     # В чем отличие ???
    #ax.autoscale(enable=True, axis='y', tight=True) # tight обнуляет margin

    #ax.set_axis_off()        # Выключение отображения осей

    margins = (0.2, -0.1)
    xticks = ([2, 4, 6, 8], ["1", "3", "5", "7"])
    axis(ax, margins=(), xticks=None)#([6,8,10], None))

    info(ax)
    return ax

def hist(ax, xdate, candles, size):
    ''' '''

def formatters():
    ''' Форматирование даты оси X '''
    def timeFormatter(x, pos):
        print(pos, x)
        x = x*frame + start
        if (x < 0):                 # На всякий случай. 
            return ''               # Иногда то локатор странно себя ведет, то что-то еще
        dt = datetime.fromtimestamp(x)
        s = dt.strftime("%H:%M")
        return s

    xdata = np.arange(1697932800, 1699574400, 1800)
    size = len(xdata)
    # !!!Самый надежный и проверенный способ:
    # нормировать ось x, а все преобразования делать внутри форматтера
    start = xdata[0]
    frame = xdata[1] - start
    x = np.arange(size)
    ydata = np.log(x+1)

    fig = plt.figure()
    ax = [0, 0, 0]
    ax[0] = fig.add_subplot(211)
    ax[1] = fig.add_subplot(4,1,3, sharex=None)
    ax[2] = fig.add_subplot(414, sharex=None)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.97, hspace=0.2, wspace=0.2)

    #  Устанавливаем интервал основных и вспомогательных делений:
    ax[0].xaxis.set_major_locator(ticker.NullLocator())

    ax[1].xaxis.set_major_locator(ticker.LinearLocator(5))      # Ничего нигде не инвертируется
    #ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(1))   # !!! Вообще лучше никогда не применять!!!

    ax[2].xaxis.set_major_locator(ticker.LinearLocator(9))      # как заявлялось ранее
    #ax[2].xaxis.set_major_locator(ticker.IndexLocator(1, 0))   # Почему-то начинается с отступом
    ax[2].xaxis.set_minor_locator(ticker.AutoMinorLocator(3))
    ax[2].grid()

    # Создание и Установка форматера для оси X
    tf = ticker.FuncFormatter(timeFormatter)

    for a in ax:
        a.xaxis.set_major_formatter(tf)
        a.plot(x, ydata)
        a.scatter(x, ydata, c="red")

    # !!! Обязательно должно быть ПОСЛЕ отрисовки!!!
    ax[1].set_xbound(870, 910)
    ax[2].set_xbound(890, 910)
    # Чтобы достичь нужного расположения сетки, мало иметь какой-то одинаковый размер фрейма (20)
    # 891, 911 уже не сработает

    plt.show()

def redraw(plots, flush=True, setx=True, refresh=20):
    ''' Перерисовка графика в различных комбинациях
    На данный момент получается, что включение GUI event (plt.ion) МОЖЕТ "подвешивать" график
    Отчего это зависит - до конца непонятно
    Выключение (plt.ioff), отсутствующее в оригинальном примере, не помогает
    Ясно только, что при flush=False точно ничего НЕ работает
    !!! При refresh>=100 тоже ничего работать не будет'''
    def init(plots, title=""):
        ''' Инициализация '''
        # creating initial data values of x and y
        # что, в общем-то совершенно ненужно, т.к. происходит в draw
        # x = np.linspace(0, 10, 100)
        # y = np.sin(x)
 
        fig, ax = plt.subplots(plots, figsize=(6, 4), sharex=True)
        if title:
            fig.suptitle(title)
        fig.subplots_adjust(left=0.1, right=0.97, top=0.95, hspace=0, wspace=0.2)

        # to run GUI event loop. Можно включить один раз (вне цикла, без периодических отключений)
        # Можно делать это в цикле (on/off), или как сейчас.
        plt.ion()
        # Расположение до или после изначальной прорисовки судя по весму, ни на что не влияет

        return fig, ax

    def draw(a, ax, t, lines, bars, setx=True):
        ''' Изначальная Прорисовка '''
        x = np.linspace(0, t+10, 100)
        y = np.sin(x-0.5*t)             # creating new Y values
        xb = np.arange(t, t+10)
        yb = abs(np.cos(xb))
        if setx:                        # Check must we update x axis?
            ax[a].set_xlim(t, t+10)     # в отличие от анимации здесь это работает
        if lines[a]:
            lines[a].set_xdata(x)       #
            lines[a].set_ydata(y)       #
            last = bars[a][-1]
            # !!! В двух последующих операциях никак не затрагиваются
            # "сопутствующие" атрибуты datavalues, patches, ...
            # т.е. bars фактически является контейнером для Rectangle
            new = ax[a].bar(xb[-1:], yb[-1:], bottom=0, color='red', width=0.2, zorder=1, label="bars")
            last.set(y=0.2, height=0.5, color='orange') # Так можно (атрибуты не меняются)
            bars[a] += new                              # так тоже (вообще исчезают)
            # Впрочем, на прорисовке это, похоже, никак не отражаетя
            #bars[a][-2] = new   #  А вот так уже нет (tuple поддерживает только сложение)
            pass
        else:
            lines[a], = ax[a].plot(x, y)
            bars[a] = ax[a].bar(xb, yb, bottom=0, color='green', width=0.2, zorder=1, label="bars")
            return lines[a]
 
    def _redraw(fig, ax, a, t, lines, bars, flush=False, setx=True):
        ''' Перерисовка в т.н. ИНТЕРАКТИВНОМ режиме '''
        #plt.ion()
        if not flush:
            flush = (a == len(lines)-1) # Сброс только для последнего графика
        draw(a, ax, t, lines, bars, setx=setx)
        if flush:
            print("Plot №"+str(a), fig.texts)
            fig.canvas.draw()       # drawing updated values
            plt.show()              # Без этих двух строк вроде как ничего не работает
            #plt.draw()             # Альтернативные способы
            #fig.show()             # и всевозможные их комбинации ничего не мяняют
            # Без этого то вообще не прорисовывается, то мерцает при перерисовке.
            # Не помогает даже установка block=False в plt.show().
            fig.canvas.flush_events()
            #  НЕПОНЯТНО, ПОМОГАЕТ или НЕТ, но без этого вроде бы НЕ работаЛО!!!
            #plt.ioff()                  # Отключение GUI event loop
            print("Flush!!!", fig.texts)   # работаЛО только в режиме Debug Eclipse!!!

        # В консоли также зависает на show. Однако, после закрытия окна продолжает спокойно
        # выполняться цикл (без нового открытия окна)

    def redraw2(plots):
        ''' Перерисовка графика в режиме "замыкания",
            позволяющим сохранять внутри такие пер-е, как fig, ax, lines '''
        fig, ax = init(plots, "Closure")
        lines = [None]*plots
        bars = [None]*plots
        def _redraw2(t, a, flush=flush, setx=True):
            _redraw(fig, ax, a, t, lines, bars, flush=flush, setx=setx)
        return _redraw2

    # Инициализация для классического обновления
    fig, ax = init(plots, "Common")
    lines = [None]*plots
    bars = [None]*plots
    # ... и для обновления через замыкания
    _redraw2 = redraw2(plots) 

    for t in range(50):
        for a in range(plots):
            _redraw(fig, ax, a, t, lines, bars, flush=flush, setx=False)  # Реализация отдельными функциями
            _redraw2(t, a, setx=setx)                               # Замыкание (fig, ax, lines) скрыты внутри

        # !!! Ключевой момент - нельзя использовать time.sleep()
        print("Pause")
        plt.pause(refresh)
        # Точнее, можно, но обязательно надо ставить на паузу plt
        #print("Sleep")                      # Так можно!
        #time.sleep(refresh)
        print("StandUp!")

def redraw3():
    ''' Перерисовка графика в режиме "очистки"
    !!! Похоже, что это самый правильный и наиболее УНИВЕРСАЛЬНЫЙ способ (работает не только для plot)
    Главное - обязательно установить block=False '''
    ax = None
    for t in range(20):
        print("Draw!")
        ax = simple(ax, (t+1)*20)
        if not t:
            #plt.show(block=False)    # !!! Ф-ю можно вызвать до начала отрисовок (см. simple())
            print("Pause!")
        plt.pause(5)

from matplotlib.animation import FuncAnimation
def animation():
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'r-')
    lim = 5

    def init():
        ax.set_xlim(0, lim)
        ax.set_ylim(-1, 1)
        return line,

    def update(frame):
        x, y = line.get_data()
        size = x.size
        x = np.append(x, frame)
        y = np.append(y, np.sin(frame))
        if (size > lim):                        # !!! Никакой перерисовки оси
            ax.set_xlim(x[size-lim], x[-1])     # не происходит
        line.set_data(x, y)
        print("Updated!!!", len(x), frame, x[-1])
        return line,

    ani = FuncAnimation(fig, update, frames=range(100000), interval=200, init_func=init, blit=True)
    plt.show()

#simple()
#formatters()
#axis()
redraw(3, flush=False)
#redraw3()
#animation()
pass
