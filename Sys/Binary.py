'''
Created on 22 июля 2016 г.

@author: Alex
'''

import struct
import pickle

class StructHdr(): pass

def StructLoad(fname):
    try:
        f = open(fname, "rb")
        hdr = StructHdr()
        data = f.read(20)
        hdr.id, hdr.nrec, hdr.rsize, hdr.dsize = struct.unpack("8sIII", data)
    except:
        return
    finally:
        if f: f.close()

StructLoad("e:/Seo/Neuro/exe/hagen.dic")
pass