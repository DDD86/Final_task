import sqlite3
from pets import *
from data_files import *
from counter import Counter
import os


def rename_combined_file():
    # Проверка, существует ли файл 'friends_of_humans.txt'
    if os.path.exists("friends_of_humans.txt"):
        print("The file 'friends_of_humans.txt' already exists. Renaming aborted.")
    else:
        os.rename("friends.txt", "friends_of_humans.txt")
        print("File renamed to 'friends_of_humans.txt'.")

def create_database():
    connection = sqlite3.connect("friends_of_humans.db")
    cursor = connection.cursor()
    
    # Создание таблиц
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DomesticAnimals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            breed TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PackAnimals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            breed TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def add_animal_to_db(animal):
    connection = sqlite3.connect("friends_of_humans.db")
    cursor = connection.cursor()
    
    if isinstance(animal, DomesticAnimal):
        cursor.execute("INSERT INTO DomesticAnimals (name, age, breed) VALUES (?, ?, ?)",
                       (animal.name, animal.age, animal.breed))
    elif isinstance(animal, PackAnimal):
        cursor.execute("INSERT INTO PackAnimals (name, age, breed) VALUES (?, ?, ?)",
                       (animal.name, animal.age, animal.breed))

    connection.commit()
    connection.close()

def add_new_animal():
    name = input("Enter the animal's name: ")
    age = int(input("Enter the animal's age: "))
    breed = input("Enter the animal's breed: ")
    animal_type = input("Enter the type (Domestic/Pack): ").strip().lower()

    if animal_type == "domestic":
        animal = DomesticAnimal(name, age, breed)
    elif animal_type == "pack":
        animal = PackAnimal(name, age, breed)
    else:
        print("Invalid animal type!")
        return None

    return animal

def menu():
    with Counter() as counter:
        animal = None  # Объявляем переменную animal в начале
        while True:
            print("\n1. Add new animal")
            print("2. Show animal commands")
            print("3. Train animal")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                animal = add_new_animal()
                if animal:
                    counter.add()
                    add_animal_to_db(animal)  # Добавляем животное в базу данных
                    print(f"{animal.name} has been added. Total animals: {counter.get_count()}")
            elif choice == "2":
                if animal:
                    # Предположим, что у класса Animal есть метод show_commands
                    commands = animal.show_commands()  # Вам нужно добавить этот метод в классы животных
                    print(f"{animal.name}'s commands: {commands}")
                else:
                    print("No animal found!")
            elif choice == "3":
                if animal:
                    command = input("Enter the command to train: ")
                    animal.add_command(command)  # Вам нужно добавить этот метод в классы животных
                    print(f"{animal.name} has learned the command: {command}")
                else:
                    print("No animal found!")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please try again.")

def main():
    create_domestic_animals_file()
    create_pack_animals_file()
    combine_animal_files()
    view_combined_file()
    rename_combined_file()
    
    # Создание базы данных
    create_database()

    # Запуск меню для управления животными
    menu()

if __name__ == "__main__":
    main()
