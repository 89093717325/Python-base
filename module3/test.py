def update_list(object_list, new_object):
    
    # в переменной result будем хранить результат выполнения функции
    # True - если элемент добавили в список
    # False - если не добавили
    # По умолчанию присваиваем в result значение False
    result = False

    # Ищем элемент в списке по ключу title у объекта new_object
    # Если нашли, то присваиваем переменной found значение True
    found = False
    for i in object_list:
        if i['title'] == new_object['title']:
            found = True

    # Если такого элемента в списке нет (т.е. found == False), то добавляем объект new_object в список object_list
    # Если такой элемент там уже есть, то ничего не делаем
    if not found:
        object_list.append(new_object)
        result = True

    return result


item_list = [{'title': 'Яблоко', 'is_fruit': True},
             {'title': 'Апельсин', 'is_fruit': True},
             {'title': 'Банан', 'is_fruit': True},
             {'title': 'Автомобиль', 'is_fruit': False},
             {'title': 'Телефон', 'is_fruit': False},
             {'title': 'Груша', 'is_fruit': True}, ]

# Пользовательский ввод данных
# Введенные пользователем значения, сохраняем в новые переменные
new_object_title = input('Введите название элемента: ')
new_object_is_fruit_text = input('Это фрукт? (Y/N): ')

# Устанавливаем значение по умолчанию для переменной, в которой будет хранится тип объекта
new_object_is_fruit = None

# Проверяем какой тип фрукта выбрал пользователь:
# Если пользователь ввел 'y', то меняем переменную new_object_is_fruit на True.
# Если пользователь ввел 'n', то меняем переменную new_object_is_fruit на False.
# Если пользователь ввел что-то отличное от 'y' или 'n', то значение переменной new_object_is_fruit остается = None
# Сравнение выполняем в нижнем регистре.
if new_object_is_fruit_text.lower() == 'y':
    new_object_is_fruit = True
elif new_object_is_fruit_text.lower() == 'n':
    new_object_is_fruit = False
    
if new_object_is_fruit is not None:
    # Если значение переменной new_object_is_fruit не None, 
    # то добавляем элемент в список
    element_added = update_list(item_list, {'title': new_object_title, 'is_fruit': new_object_is_fruit})
    if element_added:
        print('Добавили новый элемент')
    else:
        print('Такой элемент уже есть в списке')
    print(item_list)
else:
    print('Не удалось определить вид объекта')