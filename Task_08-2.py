# Все 5-буквенные слова, составленные из букв Б, К, Ф, Ц, записаны в алфавитном порядке и пронумерованы.

arr=['Б','К','Ф','Ц']
x=0
for i1 in arr:
    for i2 in arr:
        for i3 in arr:
            for i4 in arr:
                for i5 in arr:
                    x=x+1
                    if x==486:
                        print(x, i1+i2+i3+i4+i5)

# КЦФКК
