class AirBall:
    
    def __init__(self, title, price):
        self.title = title
        self.price = price


# Создаем объект класса AirBall
item = AirBall('Красный шарик', 200)

# Обращаемся к атрибутам объекта
print(item.title)
print(item.price)
