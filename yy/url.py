#!/user/bin/python
# -*- coding: utf-8 -*-
#Copyright (c) 2012 - yan <http://yanxyz.net> 
import sys
import webbrowser

import config as cf

for arg in sys.argv[1:]:
    if arg.find(cf.htdocs):
        url = arg.lower().replace('\\', '/').replace(cf.htdocs.lower(), cf.localhost)
        print(url)
        webbrowser.open_new_tab(url)

#import os
#os.system('pause')
