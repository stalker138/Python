'''
Created on 29 июля 2016 г.

@author: Alex
'''

import re, struct

# Род, число
LEX_R_MA   = 0x00000001   # Мужской род
LEX_R_FE   = 0x00000002   # Женский род
LEX_R_NE   = 0x00000004   # Средний род
LEX_R_PL   = 0x00000008   # Множественное число
LEX_R_ED   = (LEX_R_MA|LEX_R_FE|LEX_R_NE)   # Единственное число

# Падежи
LEX_P_IM =  0x00000010   # Именительный
LEX_P_RO =  0x00000020   # Родительный
LEX_P_DA =  0x00000040   # Дательный
LEX_P_VI =  0x00000080   # Винительный
LEX_P_TV =  0x00000100   # Творительный
LEX_P_PR =  0x00000200   # Предложный
LEX_P_SC =  0x00000400   # Счётный  (100 ампер, 1000 вольт...)
LEX_P_DR =  0x00000800   # Другой: звательный, местный, партитивный  (отче, сынку...)
LEX_PAD  =  0x00000FF0

# Часть речи
LEX_T_SU   = 0x00001000   # Существительное
LEX_T_PR   = 0x00002000   # Прилогательное
LEX_T_GL   = 0x00004000   # Глагол
LEX_T_NA   = 0x00008000   # Наречие
LEX_T_PRI  = 0x00010000   # Причастие
LEX_T_DEE  = 0x00020000   # Деепричастие
LEX_T_MST  = 0x00040000   # Местоимение
LEX_T_CHI  = 0x00080000   # Числительное
LEX_T_PRE  = 0x00100000   # предлог
LEX_T_SUZ  = 0x00200000   # союз
LEX_T_CHA  = 0x00400000   # частица, междуметье
LEX_T_PRD  = 0x00800000   # предикатив

# Форма
LEX_F_ODU  = 0x01000000   # Одушевлённая форма
LEX_F_NEO  = 0x02000000   # Неодушевлённая форма
LEX_F_KRA  = 0x04000000   # Краткая форма
LEX_F_SRA  = 0x08000000   # Сравнительная/Превосходная стерень

# Время
LEX_V_NAS  = 0x10000000   # Настоящее
LEX_V_PRO  = 0x20000000   # Прошедшее
LEX_V_BUD  = 0x40000000   # Будущее
LEX_V_POV  = 0x80000000   # Повелительное наклонение

DIC_ID = b"ZDIC$Mpv"
DIC_SIZE = 40

class SeoDic():
    minblock = 1000000

    def __init__(self):
        self.lexes = {}
        self._sorted = 0            # кол-во отсортированных записей
        self.pool = None

    def Ns(self):
        return len(self.lexes)

    def Last(self):
        return self.lexes[-1]
    
    def Base(self, i):
        return self.pool.Get(self.lexes[i].base)
    #def Base( cPchar val )  { return m_Pool.Add( val ) ; }

    def Value(self, ref):
        return self.pool.Get(ref)

    def FindKey(self, key):
        return self.lexes.get(key, (None, None))

    def Drop(self, i):
        del self.lexes[i]

    def Kill(self, key):
        if key in self.lexes:
            self.lexes.pop(key)

    def New(self, key):
        self.lexes[key] = None
        return self.Last() 

    def NeedSort(self):
        return (self.Ns() - self._sorted) > 10000

    def SortWrd(self):
        #Sort( (QSTYPE*)fCmpSort ) ;
        self._sorted = self.Ns()

    def Clear(self): pass

    def Save(self, fname): pass

    def Load(self, fname):                  # ZDicFile.cpp
        if self.lexes: return True
        try:
            f = open(fname, "rb")
            data = f.read(20)
            id, self.nrec, size, self.size = struct.unpack("8sIII", data)
            if (id != DIC_ID) or (size != DIC_SIZE):
                return False
            data = f.read(self.nrec*size)
            for l in range(self.nrec):
                type, key, base = struct.unpack("I32sI", data[l*size:(l+1)*size])
                self.lexes[key.decode("cp1251").rstrip('\x00')] = (type, base)
            self.pool = f.read(self.size)
            self._sorted = self.Ns()
#        except:
#            return False
        finally:
            if f: f.close()
        return True

    def ToBaseForm(self, iw):
        if isinstance(iw, str):
            type, base = self.FindKey(iw)
            if type is None:
                return 
        bform = self.Base(iw)
        if not bform or (bform[0] == '|'):      # Нет морфологических вариантов
            return self.lexes[iw].word          # Или базовая форма

        return bform

    def CheckBase(self, basewrd, w):
        if (w[0] != '*'): return basewrd.lower() == w.lower()
        for p in w[1:].split('*'):
                if (basewrd.lower() == p.lower()):
                    return True
        return False

    def IsMorpho(self, ia, ib):
        if (ia < 0 or ib < 0): return False
        if (ia == ib): return True

        a = self.lexes[ia]
        aw = self.Value(a.base)
        if not aw: return False         # Нет морфологических вариантов

        b = self.lexes[ib]
        bw = self.Value(b.base)
        if not bw: return False         # Нет морфологических вариантов

        if (aw[0] == '|'): return self.CheckBase(a.word, bw)
        if (bw[0] == '|'): return self.CheckBase(b.word, aw)

        # Оба слова не в базовой форме
        for a in aw.split('*'):
            if a:
                for b in b.split('*'):
                    if b and (a.lower() == b.lower()):
                        return True
        return False

    # Являются ли лексемы морфологическими в разном числе и том же падеже
    def IsAForm(self, ia, ib):
        if (ia < 0 or ib < 0 or ia == ib): return False

        a = self.lexes[ia]
        b = self.lexes[ib]

        # Сначала проверяем по типу
        if (a.type & LEX_R_PL == b.type &LEX_R_PL):
            return False            #Лексемы в одном и том же числе
        if not(a.type & b.type & LEX_PAD):
            return False            # Не совпадают падежи

        # Падеж совпадает, число противоположное.
        # Осталось выяснить, связаны ли они морфологически
        return self.IsMorpho(ia, ib)

dic = SeoDic()
dic.Load("e:/seo/neuro/db/hagen.dic")
pass
