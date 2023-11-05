'''
Created on 26 июл. 2018 г.

@author: Stalker
'''

import tkinter as tk
import tkinter.tix as tx
 
if __name__ == "__main__":
    #  Создаем приложение.
    app = tx.Tk()
    #  Если вы не знаете что означают эти две строки, то вам всетаки
    # стоит сначала почитать теорию.
    app.rowconfigure(0, weight=1)
    app.columnconfigure(0, weight=1)
 
    #  Итак, создаем виджет.
    # header=True значит что мы хотим показывать заголовок.
    # columns=4 значит ято у нас будет четыре столбца.
    tab = tx.HList(app, columns=5, header=True)
    tab.grid(row=0, column=0, sticky="nswe")
 
    # Просто скрол. В принципе, есть виджет ScrolledHList.
    scroll = tx.Scrollbar(app, command=tab.yview)
    tab['yscrollcommand'] = scroll.set
    scroll.grid(row=0, column=1, sticky="nwse")

    tab.column_width(3, width=15)
 
    # Создаем заголовки.
    tab.header_create(0, text="1")
    tab.header_create(1, text="2")
    tab.header_create(2, text="3")
    tab.header_create(3, text="4")
    tab.header_create(4, text="5")

    val = tx.DoubleVar()
 
    # Добавим двадцать элементов
    chk = []
    for i in range(20):
        # Добавляется строка.
        # Первый параметр - уникальное имя, он же идентификатор строки.
        # data - ассоциированные данные.
        index = '%s' % i
        tab.add(index, data="--<%s>--" % i)

        # Для каждой строки можно заполнить ячейки (столбцы).
        chk.append(tx.IntVar())
        check = tk.Checkbutton(tab, text='', variable=chk[i],onvalue=1,offvalue=0)
        tab.item_create(index, 0, itemtype=tx.WINDOW, window=check)
        tab.item_create(index, 1, text=('Item2 ' , index))
        tab.item_create(index, 2, text=('Item3 ' + index))
        #  Функция демонстрирует методы конфигурирования ячеек
        # и получения данных.
        def funcgen(index):
            def func():
                print(tab.info_data(index))
                cfg = tab.item_configure(index, 1)
                print(cfg)
                print(str(chk[0].get()))
            return func
        # Добавим кнопку в четвертый столбец.
        button = tx.Button(tab, text='111', command=funcgen(index))
        tab.item_create(index, 3, itemtype=tx.WINDOW, window=button)
        combo = tx.ComboBox(tab)
        combo.append_history("0\t0")
        combo.append_history("1\t1")
        combo.pick(0)
        tab.item_create(index, 4, itemtype=tx.WINDOW, window=combo)

    app.mainloop()
 