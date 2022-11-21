import peewee
from db_connection import db

class Table10(peewee.Model):
    Part_id = peewee.AutoField()
    Part = peewee.TextField()
    Cat = peewee.CharField()

    class Meta:
        database = db
        db_table = "Table10"

class Table20(peewee.Model):
    Catnumb = peewee.AutoField()
    Cat_name = peewee.CharField(50)
    Price = peewee.CharField(50)

    class Meta:
        database = db
        db_table = "Table20"

Table20.drop_table()
Table10.drop_table()
Table10.create_table()
Table20.create_table()


Apartment = Table10(Part_id=1, Part="Квартиры", Cat=505)
Apartment.save()
Car = Table10(Part_id=2, Part="Автомашины", Cat=205)
Car.save()
Boards = Table10(Part_id=3, Part="Доски", Cat=10)
Boards.save()
Cabinets = Table10(Part_id=4, Part="Шкафы", Cat=30)
Cabinets.save()
Books = Table10(Part_id=5, Part="Книги", Cat=160)
Books.save()

Building_materials = Table20(Catnumb=10, Cat_name="Стройматериалы", Price=105.00)
Building_materials.save()
Real_estate = Table20(Catnumb=505, Cat_name="Недвижимость", Price=210.00)
Real_estate.save()
Transport = Table20(Catnumb=205, Cat_name="Транспорт", Price=160.00)
Transport.save()
Furniture = Table20(Catnumb=30, Cat_name="Мебель", Price=77.00)
Furniture.save()
Technique = Table20(Catnumb=45, Cat_name="Техника", Price=65.00)
Technique.save()