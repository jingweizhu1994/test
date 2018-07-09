# -*- coding: UTF-8 -*-
from formatlog import formatlog
txt = 'yuyan1m.txt'
srt = 'yuyan1m.srt'
log = 'yuyan1m.log'
undetected = []
with open(log,'r') as l:
    ll=l.readlines()
    with open(srt,'r') as s:
        sl=s.readlines()
        for i in range(len(ll)):
            t_slice = formatlog(ll[i])
            print t_slice
            flag = False # flag==True represents the t_slice consists in srt
            for j in range(len(sl)):
                if t_slice in sl[j]:
                    content = sl[j+1]
                    content = content.strip()
                    print content
                    flag = True
            if not flag:
                undetected.append(t_slice)
print '***********undetected*****'
print undetected
