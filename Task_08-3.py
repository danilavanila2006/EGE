# Все четырёхбуквенные слова, составленные из букв П, А, Р, У, С, записаны в алфавитном порядке и пронумерованы

arr=['П','А','Р','У','С']
arr.sort()
print(arr)
x=0
for i1 in arr:
    for i2 in arr:
        for i3 in arr:
            for i4 in arr:
                x=x+1
                if i1 != 'А' and i2 != 'А' and i3 != 'А' and i4 != 'А':
                    print(x, i1+i2+i3+i4)

# 157 ПППП
