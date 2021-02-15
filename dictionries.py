account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}
account_list = [account1, account2, account3, account4]

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}
user_list = [user1, user2, user3, user4]

key = input('Введите ключ (Name или Account): ')
if str.lower(key) == 'name':
    print('значение ключа name для юзера 1 =', user1['name'])
    print('значение ключа name для юзера 2 =', user2['name'])
    print('значение ключа name для юзера 3 =', user3['name'])
    print('значение ключа name для юзера 4 =', user4['name'])

elif str.lower(key) == 'account':
    print('Значение ключа account для юзера 1 =', user1['account'])
    print('Значение ключа account для юзера 2 =', user2['account'])
    print('Значение ключа account для юзера 3 =', user3['account'])
    print('Значение ключа account для юзера 4 =', user4['account'])

else:
    print('Введеный ключ не найден.')

number = input('Введите порядковый номер: ')
if int(number) <= 0 or int(number) > len(user_list):
    print('Пользователь с указанным номером не найден')
else: 
    print('Данные по юзеру №', number, ' :')
    print('имя: ', user_list[int(number) - 1]['name'])
    print('возраст: ', user_list[int(number) - 1]['age'])
    print('логин: ', account_list[int(number) - 1]['login'])
    print('пароль: ', account_list[int(number) - 1]['password'])

number_append = input('Введите номер пользователя, которого нужно переместить в конец: ')
print('Имя перемещенного юзера: ', user_list[int(number_append) - 1]['name'])
print('Список юзеров до изменения: ', user_list[0]['name'], ', ', user_list[1]['name'],', ',
 user_list[2]['name'], ', ', user_list[3]['name'])

user_list.append(user_list[int(number_append) - 1]) 
user_list.remove(user_list[int(number_append) - 1]) 

print('Список юзеров после изменения: ', user_list[0]['name'], ', ', user_list[1]['name'],', ',
 user_list[2]['name'], ', ', user_list[3]['name'])

average_age = (user_list[0]['age'] + user_list[1]['age'] + user_list[2]['age'] + user_list[3]['age']) / 4
print('Средний возраст всех юзеров: ', average_age)