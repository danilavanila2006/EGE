
#На вход приведённой ниже программе поступает строка, содержащая 40 цифр 7, 40 цифр 9 и 50 цифр 4, расположенных в произвольном порядке. Запишите без разделителей символы, которые имеют порядковые номера 25, 71 и 105 в получившейся строке.
'''
ПОКА нашлось (49) ИЛИ нашлось (97) ИЛИ нашлось (47)
    ЕСЛИ нашлось (47)
        ТО заменить (47, 74)
    ЕСЛИ нашлось (97)
        ТО заменить (97, 79)
    ЕСЛИ нашлось (49)
        ТО заменить (49, 94)
'''
s = '7'*40+'9'*40+'4'*50

while '49' in s or '97' in s or '47' in s:
    if '47' in s:
        s = s.replace('47', '74', 1)
    if '97' in s:
        s = s.replace('97', '79', 1)
    if '49' in s:
        s = s.replace('49', '94', 1)
print(s[24] + s[70] + s[104])
# 794
