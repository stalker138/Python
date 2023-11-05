'''
Created on 19 Р°РІРі. 2014 Рі.

@author: Stalker
'''
import re
from urllib.request import *
from urllib.error import *
from urllib.parse import *

rspaces = re.compile('(&nbsp;){2,}|\s+')    # Удаление пробелов
rwords = re.compile('\W+')                  # Слова
rpass = re.compile('[.!?]+\s+')             # Пассажи

em = ('strong', 'em')

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.curr = ''
        self.tags = []
        self.alts = []
        self.passages = []
        self.syms = 0        # СЃРёРјРІРѕР»С‹
        self.spaces = 0
        self.words = []
        self.stops = 0
        self.imgs = 0
        self.strong = False
#        self.feed('<a class="web" href="http://www.krasko.ru" target="_blank" rel="nofollow" style="text-decoration: line-through !important;"><b>www.krask</b>o.ru</a>')

    def passage(self):
        words = rwords.split(self.curr)
        words.remove('')
        self.words.append()
        self.curr = ''

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        print(attrs)
        self.tag = tag.lower()
        self.tags.append(self.tag)
        if self.tag == 'input':
            pass
        elif self.tag == 'img':
            self.imgs += 1
            for attr in attrs:
                print("     attr:", attr)
                if (attr[0].lower() == 'alt'):
                    self.alts.append(attr[1])
        elif (self.tag in em):
            self.strong = True
        elif self.tag == 'br':
            pass

    def handle_endtag(self, tag):
        print("End tag  :", tag)
        tag = tag.lower()
        while (self.tags.pop() != tag):
            pass
        if tag in ('div', 'p', 'li'):
            self.curr = []

    def handle_data(self, data):
        print("Data     :", data)
        self.data += data
        self.curr += data
        if (self.strong):
            self.strongs.append(data) 

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)
    def handle_decl(self, data):
        print("Decl     :", data)
'''
s = rspaces.sub(' ', 'test&nbsp;&nbsp; test!!  test? ?  test.')
print(s)
p = rpass.split(s)
print(p)
s = rwords.split(s)
s.remove('')
print(s, s.count(''))
'''
#o = urlparse('http://www.cwi.krasko.ru:80/%7Eguido/Python.html')
parser = MyHTMLParser()

#parser.feed('''
'''
<form name="input_adr" action="/ar" method="post">
        
        <input type="hidden" name="sqid" value="ac188806183cc6c7">
        <input type="hidden" name="q" value="напольные покрыти">
        <input type="hidden" name="back" value="http://go.mail.ru/search?q=%D0%BD%D0%B0%D0%BF%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%BE%D0%BA%D1%80%D1%8B%D1%82%D0%B8">
        <input type="hidden" name="errback" value="http://go.mail.ru/search?q=%D0%BD%D0%B0%D0%BF%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%BE%D0%BA%D1%80%D1%8B%D1%82%D0%B8&amp;fr=captcha_error">
        <table style="margin-bottom: 10px;">
            <tbody><tr>
                <td style="padding-right: 10px;"><img src="/ar_captcha?id=ac188806183cc6c7" width="151" height="51" alt=""></td>
                <td>
                    <input type="text" class="turing mb10" maxlength="6" name="SequreWord" autocomplete="off"><br>
                    <input type="submit" value="Продолжить"><br>
                </td>
            </tr>
            
        </tbody></table>
    </form>
'''#)

#parser.feed('<a class="web" href="http://www.krasko.ru"">')# target="_blank" rel="nofollow" style="text-decoration: line-through !important;"><b>www.krask</b>o.ru</a>')
#parser.feed('<!--Comment--><p>Begin<img src="python-logo.png" alt="The Python logo">Middle<tst>Unknown</tst>LF<br/>End</p>')
#parser.feed("<img border=\"0\" src='http://www.stroy-list.ru'/bb/8831.gif' alt='Строй-Лист.Ру - Строительные компании' />")
parser.feed('''
            <div style="width: 182px; float:left;"><a href="/photos/nalivnye-poly-foto/magaziny/"><img class="pb_ismall" style="width:172px; height:96px;" src="/img/obj/nalivnye_poly/photo_001_s.jpg" title="Магазины, торговые залы" alt=""/><br>Магазины</a></div>
            ''')

