#!/user/bin/python
# -*- coding: utf-8 -*-
#Copyright (c) 2012 - yan <http://yanxyz.net> 
import os
import sys
import codecs

import config as cf

for arg in sys.argv[1:]:
    if arg[-3:] == 'css': 
        fh = open(arg)
        content = fh.read()
        if content.find('#CssGagaSprite{}') == -1:
            fh.close()

            name = os.path.basename(arg)[:-4]
            bg = 'background-image:url(sprite/' + name
            bgs,s,lines = [],[],[]
            n = len(cf.exts)
            
            for i in range(n):
                bgs.append(bg + cf.exts[i] + ');')
                s.append([])
            #print(bgs)

            #utf8 bom
            if content[:3] == codecs.BOM_UTF8: content = content[3:]
            if content.find('\n') > -1:
                alist = content.split('\n')  
            else:
                content.split('}')
            for line in alist:
                #print(line)
                if line.find(bg) > -1:
                    selector = line[:line.find('{')]
                    for i in range(n):
                        if line.find(bgs[i]) > -1:
                            s[i].append(selector)
                            line = line.replace(bgs[i],'')
                            #print(line)
                lines.append(line)
            #print(s)
            #print(lines)

            group = '#CssGagaSprite{}' 
            for i in range(n):
                if len(s[i]):
                 group = group + ','.join(s[i]) + '{' + bgs[i] + '}'
            cont = '\n'.join(lines).replace('#GeneratedByCssGaga', group + '\n#GeneratedByCssGaga')
            if not cf.breakline: cont.replace('\n','')
            #print(cont)

            fh = open(arg,'w')
            fh.write(cont)
        fh.close()

#os.system('pause')
