# Из пакета numberandstring импортируем модуль mymodulestr
from numberandstring import mymodulestr

# Из пакета numberandstring импортируем модуль mymodulenumbers
from numberandstring import mymodulenumbers

# Из модуля mymodulenumbers, который входит в пакет numberandstring импортируем только 1 объект - HUNDRED
from numberandstring.mymodulenumbers import HUNDRED


# Обращение к функции make_low из импортированного модуля mymodulestr
print(mymodulestr.make_low('ВСЕ ВнИз'))

# Обращение к объекту HUNDRED
print(HUNDRED)