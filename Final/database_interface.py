import sqlite3
from pets import DomesticAnimal, PackAnimal

class DatabaseInterface:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS DomesticAnimals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                breed TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS PackAnimals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                breed TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_animal(self, animal):
        if isinstance(animal, DomesticAnimal):
            self.cursor.execute("INSERT INTO DomesticAnimals (name, age, breed) VALUES (?, ?, ?)",
                                (animal.name, animal.age, animal.breed))
        elif isinstance(animal, PackAnimal):
            self.cursor.execute("INSERT INTO PackAnimals (name, age, breed) VALUES (?, ?, ?)",
                                (animal.name, animal.age, animal.breed))
        self.connection.commit()

    def close(self):
        self.connection.close()
