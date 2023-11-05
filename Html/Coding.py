'''
Created on 24 авг. 2016 г.

@author: Alex
'''

encodings = {
    'UTF-8':      'utf-8',
    'CP1251':     'windows-1251',
    'KOI8-R':     'koi8-r',
    'IBM866':     'ibm866',
    'ISO-8859-5': 'iso-8859-5',
    'MAC':        'mac',
}

"""
Определение кодировки текста
"""
def get_codepage(text = None):
    if not text: return None
    
    uppercase = 1
    lowercase = 3
    utfupper = 5
    utflower = 7
    codepages = {}
    for enc in encodings.keys():
        codepages[enc] = 0

    last_simb = 0
    for simb in text:
        simb_ord = ord(simb)

        """non-russian characters"""
        if simb_ord < 128 or simb_ord > 256:
            continue

        """UTF-8"""
        if last_simb == 208 and (143 < simb_ord < 176 or simb_ord == 129):
            codepages['UTF-8'] += (utfupper * 2)
        if (last_simb == 208 and (simb_ord == 145 or 175 < simb_ord < 192)) \
            or (last_simb == 209 and (127 < simb_ord < 144)):
            codepages['UTF-8'] += (utflower * 2)

        """CP1251"""
        if 223 < simb_ord < 256 or simb_ord == 184:
            codepages['CP1251'] += lowercase
        if 191 < simb_ord < 224 or simb_ord == 168:
            codepages['CP1251'] += uppercase

        """KOI8-R"""
        if 191 < simb_ord < 224 or simb_ord == 163:
            codepages['KOI8-R'] += lowercase
        if 222 < simb_ord < 256 or simb_ord == 179:
            codepages['KOI8-R'] += uppercase

        """IBM866"""
        if 159 < simb_ord < 176 or 223 < simb_ord < 241:
            codepages['IBM866'] += lowercase
        if 127 < simb_ord < 160 or simb_ord == 241:
            codepages['IBM866'] += uppercase

        """ISO-8859-5"""
        if 207 < simb_ord < 240 or simb_ord == 161:
            codepages['ISO-8859-5'] += lowercase
        if 175 < simb_ord < 208 or simb_ord == 241:
            codepages['ISO-8859-5'] += uppercase

        """MAC"""
        if 221 < simb_ord < 255:
            codepages['MAC'] += lowercase
        if 127 < simb_ord < 160:
            codepages['MAC'] += uppercase

        last_simb = simb_ord

    idx = ''
    max = 0
    for item in codepages:
        if codepages[item] > max:
            max = codepages[item]
            idx = item
    return idx

data = open("Input.txt", "rt", encoding="utf-8").read()
print(get_codepage(data))