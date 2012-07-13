#!/user/bin/python
# -*- coding: utf-8 -*-
#Copyright (c) 2012 - yan <http://yanxyz.net> 
import os
import sys
import time

from PIL import Image
import config as cf

mylist = []

for arg in sys.argv:
    if arg[-3:] in ['png', 'jpg', 'gif']:
        arg = arg.replace('\\', '/')
        name = os.path.basename(arg)
        cwd = os.path.dirname(arg)
        print(name)
        im = Image.open(arg)
        w,h = im.size
        selector = ('.' + name[:-4]) if cf.has_selector else ''
        if cf.has_size:
            code =  selector + '{width:' + str(w) + 'px;height:' + str(h) + 'px;background-image:url(slice/' + name + ');}'
        else:
            code =  selector + '{background-image:url(slice/' + name + ');}'
        mylist.append(code)

if len(mylist):
    os.chdir(cwd)
    os.chdir('../')
    cssname = str(time.time()) + '.css'
    fh = open(cssname, 'w')
    for item in mylist:
        fh.write(item + '\n')
    fh.close()

#os.system('pause')
