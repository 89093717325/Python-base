import collections


# Создаем список букв
letter_list = list('аабббвгшуатшуктоукптлойуткпойуткплоуктплойукптйулокптйу')

# Создаем счетчик
letter_counter = collections.Counter(letter_list)

# Вычисляем длину счетчика
len_counter = len(letter_counter)

# Разворачиваем последовательность используя срез с шагом -1
result = letter_counter.most_common()[:-(len_counter+1):-1]

# Выводим результат
print(result[0])