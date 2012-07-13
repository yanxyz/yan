#!/user/bin/python
# -*- coding: utf-8 -*-
#Copyright (c) 2012 - yan <http://yanxyz.net> 
import os
import sys
import shutil
import re

import config as cf

for arg in sys.argv[1:]:
    #use os.path.splitext() to get the real extention
    ext = arg[-3:]

    if ext == '.js':
        print(arg)
        tmp = arg.replace('.js', '.js.bak')
        shutil.copyfile(arg, tmp)
        cmd = 'native2ascii.exe ' + cf.n2a_option + ' "' + tmp + '" ' + '"' + arg + '"'
        os.system(cmd)
    elif ext == 'css':
        print(arg)
        tmp = arg.replace('.css', '.css.bak')
        shutil.copyfile(arg, tmp)
        cmd = 'native2ascii.exe ' + cf.n2a_option + ' "' + tmp + '" ' + '"' + arg + '"'
        os.system(cmd)
        #replace \uxxxx to \xxxx
        fp = open(arg,'r')  
        content = fp.read()  
        fp.close()  
        fp = open(arg,'w')  
        #fp.write(content);  
        #fp.write(content.replace('\\u', '\\'));  
        fp.write(re.sub(r'\\u(?P<hex>[0-9a-fA-F]{4})', r'\\\g<hex>',content));  
        fp.close()


#print('Please delete the temporary file manually!')
#os.system('pause')
