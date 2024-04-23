'''
Created on 16 нояб. 2023 г.

@author: stalker
'''

import numpy as np

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.ticker as ticker

import tkinter as tk
def mptk():
    root = tk.Tk()
    parent = tk.Frame(root,width=1500,height=100,bg="darkred", bd=20)  # bd обязателен

    fig = plt.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#mptk()

def _print_event(event, attr_list):
    print()
    print('**** {} ****'.format(event.name))
    print('    ' + str(type(event)))
    for attr in attr_list:
        title = 'event.' + attr
        value = getattr(event, attr)
        line = '    {title:20}: {value}'.format(title=title, value=value)
        print(line)

def onMouseEvent(event):
    # type: (matplotlib.backend_bases.MouseEvent) -> None
    ''' Обработчик событий, связанных с мышью '''
    attr_list = ['name',
                 'dblclick', 'button', 'key',
                 'xdata', 'ydata',
                 'x', 'y',
                 'inaxes',
                 'step',
                 'guiEvent']
    _print_event(event, attr_list)

def onKeyEvent(event):
    # type: (matplotlib.backend_bases.KeyEvent) -> None
    ''' Обработчик событий, связанных с клавиатурой '''
    attr_list = ['name',
                 'key',
                 'xdata', 'ydata',
                 'x', 'y',
                 'inaxes',
                 'guiEvent']
    _print_event(event, attr_list)


def events():
    # Расчитываем функцию
    x = np.arange(0, 5 * np.pi, 0.01)
    y = np.sin(x) * np.cos(3 * x)

    # Нарисовать график
    fig = plt.figure()
    plt.plot(x, y)

    # События, связанные с мышью
    button_press_event_id = fig.canvas.mpl_connect('button_press_event',
                                                   onMouseEvent)
    button_release_event_id = fig.canvas.mpl_connect('button_release_event',
                                                     onMouseEvent)
    scroll_event_id = fig.canvas.mpl_connect('scroll_event',
                                             onMouseEvent)

    # События, связанные с клавишами
    key_press_event_id = fig.canvas.mpl_connect('key_press_event',
                                                onKeyEvent)
    key_release_event_id = fig.canvas.mpl_connect('key_release_event',
                                                  onKeyEvent)

    plt.show()

    # Отпишемся от событий
    fig.canvas.mpl_disconnect(button_press_event_id)
    fig.canvas.mpl_disconnect(button_release_event_id)
    fig.canvas.mpl_disconnect(scroll_event_id)
    fig.canvas.mpl_disconnect(key_press_event_id)
    fig.canvas.mpl_disconnect(key_release_event_id)

# custom toolbar with lorem ipsum text
class CustomToolbar(NavigationToolbar2Tk):
    def __init__(self,canvas_,parent_):
        self.toolitems = (
            ('Home', 'Lorem ipsum dolor sit amet', 'home', 'home'),
            ('Back', 'consectetuer adipiscing elit', 'back', 'back'),
            ('Forward', 'sed diam nonummy nibh euismod', 'forward', 'forward'),
            (None, None, None, None),
            ('Pan', 'tincidunt ut laoreet', 'move', 'pan'),
            ('Zoom', 'dolore magna aliquam', 'zoom_to_rect', 'zoom'),
            (None, None, None, None),
            ('Subplots', 'putamus parum claram', 'subplots', 'configure_subplots'),
            ('Save', 'sollemnes in futurum', 'filesave', 'save_figure'),
            )
        NavigationToolbar2Tk.__init__(self,canvas_,parent_)

    def pan(self):
        NavigationToolbar2Tk.pan(self)
        self.mode = "I'm panning!" #<--- whatever you want to replace "pan/zoom" goes here
        self.set_message(self.mode)

    def zoom(self):
        NavigationToolbar2Tk.zoom(self)
        self.mode = "I'm zooming!" #<--- whatever you want to replace "zoom rect" goes here
        self.set_message(self.mode)

class MyApp(object):
    def __init__(self,root):
        self.root = root
        self._init_app()

    # here we embed the a figure in the Tk GUI
    def _init_app(self):
        self.figure = mpl.figure.Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure,self.root)
        self.toolbar = CustomToolbar(self.canvas,self.root)
        self.toolbar.update()
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.show()

    # plot something random
    def plot(self):
        self.ax.imshow(np.random.normal(0.,1.,size=[100,100]),cmap="hot",aspect="auto")
        self.figure.canvas.draw()

def navigator():
    root = tk.Tk()
    app = MyApp(root)
    app.plot()
    root.mainloop()
