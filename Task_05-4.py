'''
Автомат обрабатывает натуральное число N по следующему алгоритму.
1.  Строится двоичная запись числа N.
2.  Удаляется первая слева единица и все следующие непосредственно за ней нули. Если после этого в числе не остаётся цифр, результат этого действия считается равным нулю.
3.  Полученное число переводится в десятичную запись.
4.  Новое число вычитается из исходного, полученная разность выводится на экран.

Пример. Дано число N  =  11. Алгоритм работает следующим образом.
1.  Двоичная запись числа N: 1011.
2.  Удаляется первая единица и следующий за ней ноль: 11.
3.  Десятичное значение полученного числа 3.
4.  На экран выводится число 11 – 3  =  8.
Сколько разных значений будет показано на экране автомата при последовательном вводе всех натуральных чисел от 100 до 3000?
'''
arr = []
for i in range (100, 3000+1):
    x = i - int(bin(i)[3:],2)
    if x not in arr:
        arr.append(x)
        print(arr)
        print(len(arr))
# 6
