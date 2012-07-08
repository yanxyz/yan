#!/user/bin/python
# -*- coding: utf-8 -*-
#Copyright (c) 2012 - yan <http://yanxyz.net> 
import os
import sys

import config as cf

yui = sys.path[0] + '\\' + cf.yui
option = cf.yuioption

for arg in sys.argv:
    #you can use os.path.splitext to get the true extention
    ext = arg[-3:]

    if ext == '.js':
        print(arg)
        out = arg.replace('.source', '') if arg.find('.source') > -1 else arg.replace('.js', '-min.js')
        cmd = 'java -jar "' + yui + '" "' + arg + '" -o "' + out + '" ' + option
        os.system(cmd)
    elif ext == 'css':
        print(arg)
        out = arg.replace('.source', '') if arg.find('.source') > -1 else arg.replace('.css', '-min.css')
        cmd = 'java -jar "' + yui + '" "' + arg + '" -o "' + out + '" ' + option
        os.system(cmd)

#os.system('pause')
