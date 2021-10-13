import msvcrt as m
import random


guessesTaken = 0


def wait():
    m.getch()


input("Press Enter to continue...")
print('\n' * 100)
print("Hoe heet je?")
name = input('')
print('\n' * 100)
difficulty = input(f"Hi, {name} op wat voor niveau wil je spelen?" + " makkelijk, medium of moeilijk?")
if difficulty == "makkelijk":
    number = random.randint(1, 10)
    print(f"Oke {name} ik ben aan het denken aan een getal tussen de 1 en de 10.")
elif difficulty == "medium":
    number = random.randint(1, 20)
    print(f"Oke {name} ik ben aan het denken aan een getal tussen de 1 en de 20.")
else:
    number = random.randint(1, 50)
    print(f"Oke {name} ik ben aan het denken aan een getal tussen de 1 eb de 50.")

while guessesTaken < 6:
    guess = int(input('Neem een gok...'))
    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Je gok is te laag je moet hoger gokken.")
    elif guess > number:
        print("Je gok is te hoog je moet lager gokken.")
    elif guess == number:
        guessesTaken = guessesTaken
        print(f"Goed gedaan {name}! Je hebt het geraden in {guessesTaken} keer.")
        exit()

print(f"Je hebt het niet goed geraden het getal was {number}")
