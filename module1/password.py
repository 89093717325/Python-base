password = input('Введите пароль:')

try:
    result = 2/len(password)
    result = int(password)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')

except ValueError:
    print('Требования к паролю соблюдены')
