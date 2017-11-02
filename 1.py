a = [1, True, 'hello', 15.5]	#- список, индексированный массив, изменяемый
a[2] = False
print(a[2])
print(type(a))
b = (1, True, 'hello', 15.5)	# - кортеж, неизменяемый
print(b[2])
#b[2] = False - ошибка
print(dir(b))	#	- узнать методы
