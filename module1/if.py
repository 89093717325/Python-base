cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')

try:
    city[0]
    if city not in cities:
        print('Такого города нет в списке')


    if city.lower() == cities[0].lower():
        print(f"Турист {tourists[1]['user']['name']} возраст {tourists[1]['user']['age']}. Посетил город {city.lower()}")

    if city.lower() == cities[1].lower():
        print( f"Турист {tourists[2]['user']['name']} возраст {tourists[2]['user']['age']}. Посетил город {city.lower()}")

    if city.lower() == cities[2].lower():
        print(f"Турист {tourists[0]['user']['name']} возраст {tourists[0]['user']['age']}. Посетил город {city.lower()}")


except IndexError:
    print('Вы не указали город')
