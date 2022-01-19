import sqlite3
from sqlite3.dbapi2 import connect
from car import Car
conn = sqlite3.connect('car.db')

car1 = Car('Phantom', 'RR', 2016)
c = conn.cursor()
sql_create_table = """
    CREATE TABLE cars(
        name text,
        brand text,
        year integer
    )
"""
sql_insert = f"""
    INSERT INTO cars VALUES(:name, :brand, :year)
"""
def insert_car(car):
    with conn:
        c.execute(sql_insert, {'name': car.name, 'brand': car.brand, 'year': car.year})
        print("Car inserted")    
sql_select = """
    SELECT *FROM cars  WHERE brand = :brand AND rowID = 5
"""
sql_select_all = """
    SELECT rowID, *FROM cars ORDER BY name ASC
"""

def get_all_car():
    with conn:
        c.execute(sql_select_all)
        return c.fetchall()

def get_car_by_brand(brand):
    with conn:
        c.execute(sql_select, {'brand': brand})
        return c.fetchall()
sql_update = """
   UPDATE  cars set name = '720i' WHERE brand = "BMW" 
"""
def update_car(name, brand):
    with conn:
        c.execute(sql_update, {'name':name, 'brand': brand})

sql_delete = """
   DELETE from cars WHERE name = :name
"""
def delete_car(name):
    with conn:
        c.execute(sql_delete, {'name': name})

car1 = Car("Vios", "Toyota", 2010)
try:
    # insert_car(car1)
    # data = get_car_by_brand("BMW")
    # print(data)
    cars = get_car_by_brand("RR")
    for car in cars:
        print(car)
except:
    print("Error")
conn.close()