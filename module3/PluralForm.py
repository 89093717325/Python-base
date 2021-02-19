def plural_form(number, form1, form2, form3):
    """Функуия согласования окончаний существительных в зависимости от переданного числа
    :param number: число, к которому необходимо подобрать форму существительного
    :param form1: 1-я форма существительного
    :param form2: 2-я форма существительного
    :param form3: 3-я форма существительного"""
    if  number == 11 or number == 12 or number == 13 or number == 14 or number == 15 or number == 16 or number == 17 or number == 18 or number == 19:
         print(f"{number} {form3}")

    elif number == 1 or number % 10 == 1:
        print(f"{number} {form1}")

    elif number >= 2 and number <= 4 or number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        print(f"{number} {form2}")
    
    elif number >= 5  or number % 10 == 6 or number % 10 == 7 or number % 10 == 8 or number % 10 == 9 or number % 10 == 0:
        print(f"{number} {form3}")

plural_form(1, 'яблоко', 'яблока', 'яблок') 
plural_form(2, 'яблоко', 'яблока', 'яблок')
plural_form(11, 'студент', 'студента', 'студентов')
plural_form(15, 'студент', 'студента', 'студентов')
plural_form(3, 'студент', 'студента', 'студентов') 