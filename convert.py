import sys

def s_to_hms(seconds):
    m, sec = divmod(seconds, 60)
    h, m = divmod(m, 60)    
    #print str(int(h)) + ":" + str(int(m)) + ":" + str(int(s))
    return str(int(h)) + ":" + str(int(m)) + ":" + str(int(sec))

def conform_to_srt(s,d):
    s = s.split(':')
    for i,x in enumerate(s):
        if len(x) < 2:
            s[i] = '0'+s[i]
    s = ':'.join(s)
    if len(d) < 3:
        d+=((3-len(d))*'0')
    s += ('.'+d)
    return s
    
def convert_trs(filename):
    with open(filename, mode='r',encoding='latin-1') as myfile:
        try:
            text = myfile.readlines()
        except Exception as e:
            print(e)
        with open(filename.replace('.trs','.srt'), 'w') as newfile:
            i = 1
            for t in text:
                if t[1:5] == 'Turn':
                    
                    starttime = t[t.find('startTime=')+11:t.find('endTime=')-2]
                    starttime_digits = list(starttime)
                    
                    #conform to srt standards (3 decimal places)s
                    if starttime != '0':
                        [starttime_digits.append('0') for x in range(4 - len(starttime_digits[starttime_digits.index('.'):]))]
                    
                    starttime = ''.join(starttime_digits)
                    #preserve 3 decimal values since they will be lost in conversion function
                    starttime_decimals = starttime[-3:]
                    starttime_srt = s_to_hms(float(starttime))
                    starttime_srt = conform_to_srt(starttime_srt,starttime_decimals)
                    
                    #---
                    
                    endtime_digits = []
                    endtime_pos = t.find('endTime=')
                    endtime_str = t[endtime_pos+9:endtime_pos+17]
                    
                    ([endtime_digits.append(x) for x in endtime_str if ((x.isdigit() or x == '.') and (len(endtime_digits) < 7))])
                    
                    #conform to srt standards (3 decimal places)s
                    [endtime_digits.append('0') for x in range(4 - len(endtime_digits[endtime_digits.index('.'):]))]
                    
                    endtime = ''.join(endtime_digits)
                    #preserve 3 decimal values since they will be lost in conversion function
                    endtime_decimals = endtime[-3:]
                    endtime_srt = s_to_hms(float(endtime))
                    endtime_srt = conform_to_srt(endtime_srt,endtime_decimals)
                    
                    #---
                    
                    newfile.write('\n')
                    newfile.write(str(i)+'\n')
                    newfile.write(starttime_srt+' --> '+endtime_srt+'\n')
                    i += 1
                elif t[0] != '<':
                    newfile.write(t)
                
if __name__ == "__main__":
    i = str(sys.argv[-1])
    convert_trs(i)