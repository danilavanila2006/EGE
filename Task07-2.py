'''
В информационной системе хранятся изображения размером 1024 × 768 пикселей.
 Методы сжатия изображений не используются. 
Каждое изображение дополняется служебной информацией, которая занимает 1280 Кбайт. 
Для хранения 2048 изображений потребовалось 4 Гбайт. 
Сколько цветов использовано в палитре каждого изображения?
'''
print(x := 4*1024*1024*1024)
print(x := x/2048)
print(x := x-1280*1024)
print(x := x/1024/768)
print(2**8)
# 256