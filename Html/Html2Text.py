'''
Created on 19 февр. 2016 г.

@author: Stalker
'''

import re
import html

def html2text(text):
    def entity2char(match):
        code = html.entities.name2codepoint.get(match.group(1), 0xFFFD)
        return chr(code)

    text = re.sub(r"<!--(?:.|\n)*?-->", "", text)
    text = re.sub(r"<Pp][^>]*?(?!</)>", "\n\n", text)
    text = re.sub(r"<[^>]*?>", "", text)
    text = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), text)
    text = re.sub(r"&([A-Za-z]+);", entity2char, text)
    text = re.sub(r"\n(?:[ \xA0\t]+\n)+", "\n", text)
    text = re.sub(r"\n\n+", "\n\n", text.strip())
    return text
