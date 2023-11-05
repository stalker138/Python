'''
Created on 11 нояб. 2016 г.

@author: Alex

Запуск модулей и произвольных программ
'''

import os
import sys

print("Run: " + str(sys.argv))
if sys.argv[0].endswith("runfiles.py"):      # Run under Eclipse!!!
    start = sys.argv[0]
#    sys.argv = sys.argv[1:]
else:
    start = "start"

cmd = "%s CmdLine.py" % start
os.system(cmd)
