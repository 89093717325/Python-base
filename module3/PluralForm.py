number = 0
form1 = ''
form2 = ''
form3 = ''

def plural_form(number, form1, form2, form3):
    if number == 1:
        print(f"{number} {form1}")
    
    if number >= 2 and number <= 4:
        print(f"{number} {form2}")
    
    if number >= 5:
        print(f"{number} {form3}")

plural_form(1, 'яблоко', 'яблока', 'яблок') 
plural_form(2, 'яблоко', 'яблока', 'яблок')
plural_form(11, 'студент', 'студента', 'студентов')
plural_form(15, 'студент', 'студента', 'студентов')
plural_form(3, 'студент', 'студента', 'студентов') 