import datetime
today = datetime.datetime.now()

def start():
    print("Hello You!, ik ben Joeri")
    print("Wat is jouw naam?")

    name = input('')

    print(f"Hello {name}")
    print(f"De datum en tijd is {today}")
    print(f"{name} wil je dit programma nog een keer uitvoeren?\n Type Y/N")

    option = input('')

    if option.lower() == 'y':
        start()
    else:
        exit()


start()
