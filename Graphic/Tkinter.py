'''
Created on 26 июл. 2018 г.

@author: Stalker

Конфигурация фреймов и сеток
'''

import tkinter as tk
from tkinter import ttk

class MyButton():
    def __init__(self, root, text):
        self.but = tk.Button(root, text=text)
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()
    def printer(self,event):
        print ("Как всегда очередной 'Hello World!'")

class Frame2():
    def __init__(self, root):
        fr = tk.Frame(root,width=300,height=200,bg="green", bd=20)    # Именно он определяет видимые размеры
        fr.grid(row=0, column=1, sticky="nswe")

        fr.columnconfigure(0, pad=20)
        fr.rowconfigure(0, pad=10)

        tk.Label(fr, text="Short", background="lightcyan", width="15", anchor="w", padx="7").grid(sticky="w", padx=17)
        ttk.Label(fr, text="Long Label", style="TLabel").grid(row=1, sticky="w", padx="20", ipadx=15)

        self.dvar = tk.DoubleVar()
        self.svar = tk.StringVar()
        tk.Entry(fr, width=10, bd=3, relief=tk.RAISED, justify=tk.RIGHT, textvariable=self.dvar, state=tk.DISABLED).grid(row=0, column=1)
        tk.Entry(fr, width=10, bd=3, relief=tk.SUNKEN, justify=tk.RIGHT, textvariable=self.svar, state=tk.DISABLED).grid(row=1, column=1)

        self.list = tk.Listbox(fr, height=5, width=15, selectmode=tk.SINGLE)
        self.list.grid(row=2, column=0)
        list2=[u"Канберра",u"Сидней",u"Мельбурн",u"Аделаида"]
        for l in list2:
            self.list.insert(tk.END, l)

        but = tk.Button(fr, text="Button 2")

# TreeView с обработкой выбора и двойного щелчка
def table(parent=None, height=0, headings=tuple(), columns=(), config=(), rows=tuple(), tags=()):
    if not columns:
        columns = headings

    tv = ttk.Treeview(parent, columns=columns, displaycolumns=columns, height=height, show="headings", selectmode="browse")

    for c, head in enumerate(headings):
        tv.heading(columns[c], text=head, anchor=tk.CENTER)
        tv.column(c, None, **config[c])

    for r, row in enumerate(rows):
        tag = tags[r] if tags else ()
        tv.insert('', tk.END, values=tuple(row), tags=tag)

    scrolltable = ttk.Scrollbar(parent, command=tv.yview)
    tv.configure(yscrollcommand=scrolltable.set)
    scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
    tv.pack(expand=tk.YES, fill=tk.BOTH)

    return tv

def topwin(parent, widgets=True):
    ''' Окно вехнего уровня с вкладками '''
    def testf(event=None):
        print("Test", str(event))

    # Независимое окно
    top = tk.Toplevel(parent,relief=tk.SUNKEN,bd=10,bg="lightblue")
    top.title("Якобы главное окно")
    top.minsize(width=400,height=200)

    if not widgets:
        return top

    # Создание вкладок
    tabs = ttk.Notebook(top)  
    tab1 = ttk.Frame(tabs)  
    tab2 = ttk.Frame(tabs)  
    tabs.add(tab1, text='Первая')  
    tabs.add(tab2, text='Вторая')  
    tabs.pack(expand=1, fill='both')  

    # Эта кнопка упорно не хочет отображаться на Toplevel
    butw = tk.Button(top, text="Button Class", command=testf)
    butw.pack()     # !!! Пока не сделать так !!

    return top

def frames(root):
    ''' Демонстрация различных фреймов '''
    def testf(event=None):
        print("Test", str(event))
        select = tree.selection()
        item = tree.item(select)
        print("Item:", item["values"])

    def selection(event):
        ''' Выбор элемента '''
        select = tree.selection()
        item = tree.item(select)
        print("Item:", item["values"])

    fr1 = tk.Frame(root,width=1500,height=100,bg="darkred", bd=20)  # bd обязателен

    fr2 = Frame2(root)
    fr3 = tk.Frame(root,width=500,height=150,bg="darkblue", bd=5)

    fr1.grid(row=0, column=0, sticky="nswe")
    fr3.grid(row=0, column=2, sticky="nswe")

    # Создание кнопок
    #but0 = MyButton(root, "Button 0")
    but1 = MyButton(fr1, text="Button 1")
    but3 = MyButton(fr3, text="Button 3")

    # Список с множественным выбором (Listbox)
    listbox1=tk.Listbox(fr1,height=5,width=15,selectmode=tk.EXTENDED)
    list1=[u"Москва",u"Санкт-Петербург",u"Саратов",u"Омск"]
    for i in list1:
        listbox1.insert(tk.END,i)
    listbox1.pack()

    # Редактируемое поле ввода (Entry)
    val = tk.DoubleVar()
    val.set(1000)
    ent = tk.Entry(fr1, textvariable=val, justify="right")
    ent.pack()

    # Кнопки (CheckButton)
    var1=tk.IntVar()
    var2=tk.IntVar()
    check1=tk.Checkbutton(fr1,text='1 пункт',variable=var1,onvalue=1,offvalue=0)
    check2=tk.Checkbutton(fr1,text='2 пункт',variable=var2,onvalue=1,offvalue=0)
    check1.pack()
    check2.pack()

    # Treeview с обработкой событий
    columns = ("#1", "#2", "#3")
    headings = ("Фамилия", "Имя", "Почта")
    config = ({"anchor": tk.W, "width": 60}, {"anchor": tk.W, "width": 40}, {"anchor": tk.W, "width": 60})
    items = (("Family", "Name", "Mail"), 
            ("Another", "", "Nothing"))
    tag = ("dbl-click",)
    tags = (tag, tag, tag)
    '''# Первыый способ - более универсальный, но посложнее
    tree = ttk.Treeview(fr3, show="headings", columns=columns)
    tree.heading("#1", text="Фамилия")
    tree.heading("#2", text="Имя")
    tree.heading("#3", text="Почта")
    ysb = ttk.Scrollbar(fr3, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=ysb.set)
    for c, cfg in enumerate(config):
        tree.column(c, None, **cfg)
    tree.insert('', tk.END, values=("Family", "Name", "Mail"), tags=tags)
    tree.insert('', tk.END, values=("Another", "", "Nothing"), tags=tags)'''
    tree = table(fr3, columns=columns, headings=headings, config=config, rows=items, tags=tags)
    tree.tag_bind("dbl-click", "<Double-Button-1>", testf)
    tree.bind("<<TreeviewSelect>>", selection)
    #tree.pack()

    # Второй способ - попроще
    tree2 = ttk.Treeview(fr3, show="headings", columns=columns)
    tree2.heading("#1", text="Фамилия")

class Frames(tk.Frame):
    ''' Класс, реализующий окно '''
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        frames(parent)

def main():
    root = tk.Tk()
    root.attributes('-topmost', True)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("TFrame", foreground="black", background="lightgray")
    style.configure("TLabel", background="lightgray", width="20", anchor="w", padx="20")
    style.configure("Treeview.Heading", background = "blue", foreground="Black")

    # Такой вызов frames(root) приводит к появлению какого-то дополнительного непонятного окна
    #root.withdraw()    # Не помогает, появляется только лишнее окно
    #frames(root)
    #root.deiconify()    # Отображаем окно, появляются сразу ДВА лишних

    # !!!А в данном случае таких окон сразу два
    #top = topwin(root, widgets=False)
    #top.mainloop()    # Не помогает

    Frames(root)  # Не помогает

    # !!! А вот это работает. Правда в случае topwin одно лишнее окно все же остается
    def refresh():
        root.after(3000, refresh)
    root.after(3000, refresh)              # Просто вызов почему-то не работает

    root.mainloop()

main()
