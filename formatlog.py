import time

filename = 'warn.log'
def formatlog(l):
    l=l.strip()
    l=l.split('>')
    start=l[0]
    start=start.split('(')
    start=start[1]
    start=start.split(')')
    start=start[0]
    start=start.split('.')
    if len(start) > 1:
        sdot = start[1]
        sdot =sdot +'0'*(3-len(sdot))
    else:
        sdot = '000'
    start=start[0]
    
    end = l[1]
    end = end.split('(')
    end = end[1]
    end = end.split(')')
    end = end[0]
    end = end.split('.')
    if len(end) >1:
        edot = end[1]
        edot=edot+'0'*(3-len(edot))
    else:
        edot = '000'
    end = end[0]
    start = int(start)
    m, s = divmod(start, 60)
    h, m = divmod(m, 60)
    start = ("%02d:%02d:%02d" % (h, m, s))
 
    end = int(end)
    m, s = divmod(end, 60)
    h, m = divmod(m, 60)
    end = ("%02d:%02d:%02d" % (h, m, s))
    return start+','+sdot +' --> '+end+','+edot

if '__name__' == '__main__':
    import time

    filename = 'warn.log'
    with open(filename) as f:
        with open('formatlog.log','w') as outfile:
            for l in f:
                if 'Warn' not in l:
                    result=formatlog(l)
                    outfile.write(result)
                else:
                    outfile.write(l)
