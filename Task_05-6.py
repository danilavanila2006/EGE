'''
Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
1.  Складываются первая и вторая, а также вторая и третья цифры исходного числа.
2.  Полученные два числа записываются друг за другом в порядке убывания (без разделителей).
Пример. Исходное число: 348. Суммы: 3 + 4  =  7; 4 + 8  =  12. Результат: 127.
Сколько существует чисел, в результате обработки которых автомат выдаст число 1715?
'''
for i in range(100, 999+1):
 x = str(i)
 para1 = int(x[0]) + int(x[1])
 para2 = int(x[1]) + int(x[2])
 y = str(max(para1, para2)) + str(min(para1, para2))
 if y == '1715':
     print(y)
     # всего вышло четыре склейки