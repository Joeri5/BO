import time
import sys

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "Yes", "yes"]
no = ["N", "n", "No", "no"]

required = ("\n Gebruik alleen A, B of C \n")


def begin():
    print("Er is een diktator in Syrië, en hij neemt de vrijheid af van iedereen die het niet met hem eens is. Je wilt iets doen, wat ga je doen?")
    print("A | Je spreekt je mening uit.")
    print("B | Je doet niks.")
    print("C | Je gaat bij het verzet.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_mening()
    if choice in answer_B:
        option_niks()
    if choice in answer_C:
        option_verzet()
    else:
        print(required)
        begin()


def option_mening():
    print("Doordat je je mening hebt uitgesproken wordt je nu gezocht door de overheid. Ze willen je dood hebben, wat ga je doen?")
    print("A | Je gaat vluchten.")
    print("B | Je geeft je over.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_vluchten()
    if choice in answer_B:
        print("Je hebt er voor gekozen om jezelf over te geven aan de overheid. De overheid heeft je gevangen genomen en gemarteld. Je bent overleden.")
        sys.exit()
    else:
        print(required)
        option_mening()


def option_vluchten():
    print("Je hebt er voor gekozen om te vluchten, je hebt een aantal opties op de manier hoe je vlucht.")
    print("A | Je gaat met de auto naar Libanon.")
    print("B | Je gaat met de boot naar Cyprus.")
    print("C | Je gaat met de auto naar Turkijë.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortlibanon()
    if choice in answer_B:
        option_paspoortcyprus()
    if choice in answer_C:
        option_paspoortturkije()
    else:
        print(required)
        option_vluchten()


def option_paspoortlibanon():
    print("Om het land binnen te komen heb je een paspoort nodig. Heb je die mee?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeelibanon()
    if choice in answer_B:
        print("Je hebt je paspoort niet meegenomen. Je wordt opgepakt door de politie, ze gooien je in de gevangenis en je wordt gemarteld tot de dood.")
        sys.exit()
    else:
        print(required)
        option_paspoortlibanon()


def option_paspoortmeelibanon():
    print("Je hebt je paspoort meegenomen en je bent veilig in Libanon aangekomen. Je gaat met het vliegtuig naar Nederland.")
    time.sleep(1)
    print("Eenmaal veilig aangekomen in Nederland, word je opgepakt door de politie. Je moet 10 jaar de gevangenis in wegens illegaal het land in komen.")
    time.sleep(10)
    print("Je bent uit de gevangenis gekomen, en je hebt een verblijfsvergunning gekregen.")
    print("Je moet een beroep kiezen voor je toekomst in Nederland.")
    print("A | Tandarts")
    print("B | Supermarkt Manager")
    print("C | Bouwvakker")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden.")
        time.sleep(1)
        print("Je gaat wonen in een mooi huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent supermarkt manager geworden.")
        time.sleep(1)
        print("Je gaat wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent bouwvakker geworden.")
        time.sleep(1)
        print("Je komt te overlijden door een bedrijfsongeval.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden.")
        time.sleep(1)
        print("Je gaat wonen in een prachtige villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_paspoortmeelibanon()


def option_niks():
    print("Je ziet dat mensen in je omgeving in het verzet gaan, je wilt iets doen. Wat ga je doen?")
    print("A | Je gaat in het verzet.")
    print("B | Je gaat vluchten.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je hebt besloten om in het verzet te gaan. De overheid heeft je opgepakt en gemarteld tot de dood.")
        sys.exit()
    if choice in answer_B:
        option_vluchten()
    else:
        print(required)
        option_niks()


def option_verzet():
    print("Je hebt besloten om in het verzet te gaan. De overheid zoekt je en wilt je dood hebben, wat doe je?")
    print("A | Je geeft je over.")
    print("B | Je vlucht.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je hebt er voor gekozen om jezelf over te geven aan de overheid. De overheid heeft je gevangen genomen en gemarteld. Je bent overleden.")
        sys.exit()
    if choice in answer_B:
        option_vluchten()
    else:
        print(required)
        option_verzet()


def option_paspoortcyprus():
    print("Om het land binnen te komen heb je een paspoort nodig. Heb je die mee?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeecyprus()
    if choice in answer_B:
        print("Je hebt je paspoort niet meegenomen. Je wordt opgepakt door de politie, ze gooien je in de gevangenis en je wordt gemarteld tot de dood.")
        sys.exit()
    else:
        print(required)
        option_paspoortcyprus()


def option_paspoortmeecyprus():
    print("Je moet vanuit Cyprus met de boot naar Griekenland.")
    print("Kies A of B")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_veilignederland()
    if choice in answer_B:
        print("De boot is gezonken, je kan niet zwemmen en bent daardoor verdronken.")
        sys.exit()
    else:
        print(required)
        option_paspoortmeecyprus()


def option_veilignederland():
    print("Je bent veilig aangekomen in Griekenland en gaat met het vliegtuig naar Nederland.")
    time.sleep(1)
    print("Je bent veilig aangekomen in Nederland. Je krijgt een verblijfsvergunning, nu is het tijd om een beroep te kiezen.")
    print("A | Tandarts")
    print("B | Supermarkt Manager")
    print("C | Bouwvakker")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden.")
        time.sleep(1)
        print("Je gaat wonen in een mooi huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent supermarkt manager geworden.")
        time.sleep(1)
        print("Je gaat wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent bouwvakker geworden.")
        time.sleep(1)
        print("Je komt te overlijden door een bedrijfsongeval.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden.")
        time.sleep(1)
        print("Je gaat wonen in een prachtige villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_veilignederland()


def option_paspoortturkije():
    print("Om het land binnen te komen heb je een paspoort nodig. Heb je die mee?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeeturkije()
    if choice in answer_B:
        print("Je hebt je paspoort niet meegenomen. Je wordt opgepakt door de politie, ze gooien je in de gevangenis en je wordt gemarteld tot de dood.")
        sys.exit()
    else:
        print(required)
        option_paspoortturkije()


def option_paspoortmeeturkije():
    print("Je gaat vanuit Turkijë naar Nederland met het vliegtuig.")
    time.sleep(1)
    print("Je bent veilig aangekomen in Nederland. Je krijgt een verblijfsvergunning, nu is het tijd om een beroep te kiezen.")
    print("A | Tandarts")
    print("B | Supermarkt Manager")
    print("C | Bouwvakker")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden.")
        time.sleep(1)
        print("Je gaat wonen in een mooi huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent supermarkt manager geworden.")
        time.sleep(1)
        print("Je gaat wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent bouwvakker geworden.")
        time.sleep(1)
        print("Je komt te overlijden door een bedrijfsongeval.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden.")
        time.sleep(1)
        print("Je gaat wonen in een prachtige villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_paspoortturkije()


begin()
