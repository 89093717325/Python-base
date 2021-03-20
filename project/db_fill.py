from app import db
from app.models import Car


# создаем экземпляр класса Car

# добавляем изменения в базу данных (при этом база не сохраняется)
db.session.add(Car(name="Volkswagen", description='Вид имеет', price=6, transmission='АТ'))
db.session.add(Car(name="Audi", description='Так себе', price=8, transmission='АТ'))
db.session.add(Car(name="BMW", description='Тигриная', price=9, transmission='АТ'))

# сохраняем изменения в базе
db.session.commit()