'''
Created on 25 июл. 2018 г.

@author: Stalker
'''

import tkinter as tk
import tkinter.ttk as ttk

class Table1(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, columns=headings, displaycolumns=headings, show="headings", selectmode="browse")
#        table["columns"]=headings
#        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
        table.column(0, width=20)
        ttk.Style().configure("Treeview.Heading",background = "Black",foreground="Red")

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

class Cell(tk.Entry): 
    def __init__(self, parent):
        self.value = tk.StringVar()
        tk.Entry.__init__(self, parent, textvariable = self.value)

class Table2(tk.Frame):
    def __init__(self, parent, columns = 4, rows = 10):
        tk.Frame.__init__(self, parent)
        self.cells = [[Cell(self) for i in range(columns)] for j in range(rows)]
        [self.cells[i][j].grid(row = i, column = j) for i in range(rows) for j in range(columns)]

class MyTree(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Элементам с тегом green назначить зеленый фон, элементам с тегом red назначить красный фон
        self.tag_configure('green', background='green')
        self.tag_configure('red', background='red')
        self.tag_configure('yellow', background='yellow')

    def insert(self, parent_node, index, **kwargs):
        '''Назначение тега при добавлении элемента в дерево'''

        item = super().insert(parent_node, index, **kwargs)

        values = kwargs.get('values', None)

        if values:
            if values[2]=="Сдана":
                super().item(item, tag='green')
            elif values[2]=="Просрочена":
                super().item(item, tag='red')
            elif values[2]=="На руках":
                super().item(item, tag='yellow')

        return item

def main():
    style = ttk.Style()
    style.theme_use("default")

    # Решение проблемы с подсветкой строк на Python 3.8
    # Взято отсюда: https://bugs.python.org/issue36468
    def fixed_map(option):
        return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]
    #style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

    root = tk.Tk()

    table1 = Table1(root, headings=('aaa', 'bbb', 'ccc'), rows=((123, 456, 789), ('abc', 'def', 'ghk')))
    table1.pack(expand=tk.YES, fill=tk.BOTH)

    table2 = Table2(root)
    table2.pack()
    table2.cells[1][1].value.set('test')
    table2.cells[2][2].value.set( table2.cells[1][1].value.get() )

    # Создание таблицы с заданными колонками
    columns = ("Tree", "Название", "Автор", "Статус")
    tree = MyTree(root, columns=columns[1:])
    tree.pack()
    for i, heading in enumerate(columns):
        tree.heading('#'+str(i), text=heading)

    # Добавление записей
    root_item = tree.insert('', tk.END, text="root", open=True)
    items = (('Капитанская дочка', 'Пушкин', 'На руках'),
             ('Книга 2', 'Автор 2', 'Просрочена'),
             ('Книга 3', 'Автор 2', 'Сдана'))
    item0 = tree.insert(root_item, tk.END, text="Книга 1", values=items[0])
    tree.insert(root_item, tk.END, text="Книга 2", values=items[1])
    tree.insert(root_item, tk.END, text="Книга 3", values=items[2])
    sel = tree.selection()              # sel = ()
    tree.selection_set(item0)           # Так работает
    #tree.selection_set(items[1])        # А так выдает ошибку
    tree.selection_set('I003')          # Так тоже работает! Нумерация начинается с root_item (I001)
    sel = tree.selection()              # sel = ('I003',)
    try:
        tree.selection_set('I005')          # Exception
    except Exception as e:
        print("No SuchItem!", e)

    root.mainloop()

main()
