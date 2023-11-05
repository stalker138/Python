'''
Created on 18 мар. 2018 г.

@author: Stalker
'''

import os
from ftplib import *

file = "test.txt"

ftp = FTP("vh54.timeweb.ru", "teo02_ftp", "tG7IsFqzLk")
files = []
dirs = ftp.retrlines('LIST teohim-vr.ru/public_html/.htaccess', lambda f: files.append(f.split()))
dirs = ftp.nlst("teohim-vr.ru/public_html")

#f = open(file, "rb")
#send = ftp.storbinary("STOR "+file, f)

def retrive():
    s = b""
    def retr(block):
        s += block
        print(s)
    ftp.retrbinary("RETR "+file, retr)
retrive()

ftp.close()