#Автомат обрабатывает натуральное число N по следующему алгоритму:
#1.  Строится двоичная запись числа N.
#2.  Складываются все цифры полученной двоичной записи. В конец записи (справа) дописывается остаток от деления суммы на 2.
#3.  Предыдущий пункт повторяется для записи с добавленной цифрой.
#4.  Результат переводится в десятичную систему и выводится на экран.
#Пример. Дано число N  =  13. Алгоритм работает следующим образом:
#1.  Двоичная запись числа N: 1101.
#2.  Сумма цифр двоичной записи  — 3, остаток от деления на 2 равен 1, новая запись: 11011.
#3.  Сумма цифр полученной записи  — 4, остаток от деления на 2 равен 0, новая запись: 110110.
#4.  На экран выводится число 54.
#Какое наименьшее число, большее 93, может появиться на экране в результате работы автомата?
for i in range(0,1000):
    бин = bin(i)
    остат = str(бин.count('1') % 2)
    бинплюс1 = бин+остат
    остат = str(бинплюс1.count('1') % 2)
    бинплюс2 = бинплюс1+остат
    десятир =  int(бинплюс2,2)
    if десятир > 93:
        break    
print(десятир)
#96
