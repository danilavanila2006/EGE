arr = ['А', 'О', 'У']
x = 0
for i1 in arr:
    for i2 in arr:
        for i3 in arr:
            for i4 in arr:
                for i5 in arr:
                    x = x+1
                    if  i1+i2+i3+i4+i5 == 'ОАОАО':
                        print(x, i1+i2+i3+i4+i5)
                        print(len('ООООАОА'))
                      # 92 ОАОАО
