'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1.  Строится двоичная запись числа N.
2.  К этой записи дописываются разряды по следующему правилу:
а)  если число четное, то к двоичной записи числа в конце дописываются 1 и 0;
б)  если число нечетное, то к двоичной записи числа в конце дописывается 01.
Полученная таким образом запись является двоичной записью искомого числа R. Укажите наибольшее число R, меньшее 109, которое может получиться после обработки этого алгоритма. В ответе это число запишите в десятичной системе.
'''
макси = 0
for i in range(109):
    if i % 2 == 0:
        x = int(bin(i) + '10', 2)
    else:
        x = int(bin(i) + '01', 2)
    if x > макси and x < 109:
        макси = x
print(макси)
#106
