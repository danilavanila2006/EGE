# Значение выражения 36**7 + 6**19 − 18? записали в системе счисления с основанием 6.
# Сколько цифр 0 содержится в этой записи?
x10 = 36**7 + 6**19 - 18
print(x10)

x6 = ''
while x10 != 0:
    x6 = str(x10 % 6) + x6
    x10 = x10 // 6
    print(x10, x6)
    print(x6)
  # 6