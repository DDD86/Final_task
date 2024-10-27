import os

def create_domestic_animals_file():
    with open("domestic_animals.txt", "w", encoding="utf-8") as file:
        file.write("Dog, 3, Labrador\n")
        file.write("Cat, 2, Siamese\n")
        file.write("Hamster, 1, Syrian\n")

def create_pack_animals_file():
    with open("pack_animals.txt", "w", encoding="utf-8") as file:
        file.write("Horse, 5, Thoroughbred\n")
        file.write("Camel, 8, Dromedary\n")
        file.write("Donkey, 4, Mammoth\n")

def combine_animal_files():
    with open("domestic_animals.txt", "r", encoding="utf-8") as domestic_file:
        domestic_data = domestic_file.readlines()

    with open("pack_animals.txt", "r", encoding="utf-8") as pack_file:
        pack_data = pack_file.readlines()

    with open("friends.txt", "w", encoding="utf-8") as combined_file:
        combined_file.writelines(domestic_data)
        combined_file.writelines(pack_data)

def view_combined_file():
    with open("friends.txt", "r", encoding="utf-8") as combined_file:
        content = combined_file.read()
        print(content)

def rename_combined_file():
    if os.path.exists("friends_of_humans.txt"):
        print("The file 'friends_of_humans.txt' already exists. Renaming aborted.")
    else:
        os.rename("friends.txt", "friends_of_humans.txt")
        print("File renamed to 'friends_of_humans.txt'.")
