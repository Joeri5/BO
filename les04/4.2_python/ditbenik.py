def start():
    print("Hi, welkom bij dit keuzeverhaal.")
    name = input('Wat is je naam? >>')

    print (f"{name} welk land kies je?")
    print("A Nederland")
    print("B Syrië")
    print("C Afghanistan")

    afkomst = input('>>')

    if afkomst.lower() == 'a':
        print("Je bent in Nederland. Je moet van de regering een bepaald geloof aannemen. Wat doe je?")
        print("A Je neemt het geloof dat ze je dwingen aan te nemen, aan.")
        print("B Je gaat er tegen in, en neemt het geloof niet aan.")

        keuze_a = input('>>')

        if keuze_a.lower() == 'a':
            print("Je hebt het geloof aangenomen.")
            print("De overheid heeft besloten dat je niet meer je eigen mening mag hebben. Je moet het altijd met de mening van de overheid eens zijn.")
            print("Wat ga je doen?")
            print("A Je bent het er niet mee eens en je gaat er tegen in.")
            print("B Je vlucht weg van de overheid omdat je, je mening wilt uiten hoe jij dat wilt.")

            keuze_a1 = input('>>')

            if keuze_a1.lower() == 'a':
                print("Je hebt er voor gekozen om er tegen in te gaan en de overheid wilt je nu oppakken. Je moet vluchten. Waar ga je naartoe vluchten?")
                print("A Amsterdam")
                print("B München")

                keuze_a2 = input('>>')

                if keuze_a2.lower() == 'a':
                    print("Je bent naar Amsterdam gevlucht. De overheid heeft je opgepakt en doodgeschoten.")
                    print("GAME OVER!")
                elif keuze_a2.lower() == 'b':
                    print("Je bent naar München gevlucht. Je bent nu veilig en leeft gelukkig verder.")

        elif keuze_a.lower() == 'b':
            print("Je hebt het geloof niet aangenomen, en je hebt een slecht artikel over de overheid geschreven.")
            print("De overheid heeft je opgepakt en proberen hun je te overtuigen van hun mening via marteling. Wat doe je?")
            print("A Je geeft toe aan de overheid en neemt hun mening aan.")
            print("B Je geeft niet toe aan de overheid en blijft bij je eigen standpunt.")

            keuze_a3 = input('>>')

            if keuze_a3.lower() == 'a':
                print("Je neemt de mening aan van de overheid en ze laten je vrij. Wat doe je?")
                print("A Je vlucht")
                print("B Je blijft in Nederland.")

                keuze_a4 = input('>>')

                if keuze_a4.lower() == 'a':
                    print("Je bent veilig gevlucht uit Nederland en je leeft gellukig verder.")
                elif keuze_a4.lower() == 'b':
                    print("Je bent in Nederland gebleven en je bent alsnog doodgemaakt door de overheid.")
                    print("GAME OVER!")

            if keuze_a3.lower() == 'b':
                print("Je geeft niet toe aan de mening van de overheid en je word doodgemaakt door middel van marteling.")
                print("GAME OVER!")

    elif afkomst.lower() == 'b':
        print("Je bent in Syrië. Er is een burgeroorlog. Wat doe je?")
        print("A Je vecht mee in de burgeroorlog.")
        print("B Je vlucht weg van de oorlog.")

        keuze_b = input('>>')

        if keuze_b.lower() == 'a':
            print("Je gaat mee vechten. Je komt om in een schietgevecht.")
            print("GAME OVER!")

        elif keuze_b.lower() == 'b':
            print("Je gaat vluchten. Waar ga je naartoe vluchten?")
            print("A Nederland")
            print("B Turkijë")

            keuze_b2 = input('>>')

            if keuze_b2.lower() == 'a':
                print("Je vlucht naar Nederland, je moet eerst naar Turkijë vluchten om naar Nederland toe te gaan. Maak een keuze :")
                print("1")
                print("2")

                keuze_b3 = input('>>')

                if keuze_b3.lower() == '1':
                    print("Je bent veilig in Turkijë aangekomen.")
                    print("Je stapt op een vliegtuig naar Nederland en je krijgt daar een verblijfsvergunning.")
                elif keuze_b3.lower() == '2':
                    print("Je hebt de verkeerde keuze gemaakt en je bent doodgeschoten.")
                    print("GAME OVER!")

            elif keuze_b2.lower() == 'b':
                print("Je vlucht naar Turkijë.")
                print("Je bent veilig in Turkijë gekomen en je leeft lang en gelukkig.")

    elif afkomst.lower() == 'c':
        print("Je bent in Afghanistan. De taliban zit in het land.De Verenigde Staten valt binnen. Wat doe je?")
        print("A Je helpt de Verenigde Staten helpen om de taliban weg te krijgen uit Afghanistan.")
        print("B Je vlucht weg van de oorlog.")

        keuze_c = input('>>')

        if keuze_c.lower() == 'a':
            print("Je gaat de Verenigde Staten helpen de taliban weg te krijgen uit Afghanistan.")
            print("vecht je mee met de Verenigde staten?")
            print("A Ja")
            print("B Nee")

            keuze_c1 = input('>>')

            if keuze_c1.lower() == 'a':
                print("Je word doodgeschoten door de taliban.")
                print("GAME OVER!")
            elif keuze_c1.lower() == 'b':
                print("Je bent veilig weggevlucht en je leeft lang en gelukkig.")

        elif keuze_c.lower() == 'b':
            print("Je vlucht weg van de oorlog.")
            print("Je leeft lang en gelukkig.")
    else:
        print("Dit is geen geldige keuze.")
        print(f"{name} wil je het nog een keer proberen?\n type Y/N")

        option = input('>>')

        if option.lower() == 'y':
            start()
        else:
            exit()



start()
