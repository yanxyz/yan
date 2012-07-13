#!/user/bin/python
# -*- coding: utf-8 -*-
#Copyright (c) 2012 - yan <http://yanxyz.net> 
import sys
import urllib2
import re

import config as cf

def indent_html(html,indent):
    html = html.strip()
    n = html.find('<html')
    indented = html[:n].strip() #<!DOCTYPE...
    cont = html[n:] #<head...
    lines = cont.split('\n')
    i = 0
    for line in lines:
        line = line.strip()
        start = 1 if re.search(r'^<([a-z]|!--)', line) else 0 #tag open
        end = 1 if re.search(r'(/[a-z0-6]{0,10}|--)>$', line) else 0 #tag close
        if start > end:
            indented += '\n' + i*indent + line 
            i += 1
        elif start < end:
            i -= 1
            indented += '\n' + i*indent + line 
        else:
            indented += '\n' + i*indent + line
    return indented

for arg in sys.argv[1:]:
    if arg[-3:] == 'php':
        url = arg.lower().replace('\\', '/').replace(cf.htdocs.lower(), cf.localhost)
        print(url)
        
        htmlcont = urllib2.urlopen(url).read()
        htmlcont = indent_html(htmlcont, cf.indent)
        htmlname = arg.replace('.php', '.html')
        fh = open(htmlname, 'w')
        fh.write(htmlcont)
        fh.close() 

#import os
#os.system('pause')
