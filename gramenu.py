x=int(0)
while x==0:
    print("MENU")
    print("")
    print("[1] NOWA GRA")
    print("[2] WCZYTAJ GRĘ")
    print("[3] NAJLEPSZE WYNIKI")
    print("[4] TWÓRCY")
    print("[5] CHOINKA")
    print("[6] WYJŚCIE")
    print("")
    print("CO WYBIERASZ?")
    x=input()
    x=int(x)
    if x==1:
        print("[1] NOWA GRA")
        print("")
        print("WŁAŚNIE STWORZYŁEŚ NOWĄ GRĘ!")
        print("JESTEŚ MĘŻCZYZNĄ [WYBIERZ M] CZY KOBIETĄ [WYBIERZ K]?")
        plec=input()
        nick=input("PODAJ SWÓJ NICK: ")
        print("CZEŚĆ",nick,"ILE LAT MA TWOJA POSTAĆ? ")
        age=input()
        if plec=="M" or plec=="m":
            print("WŁAŚNIE STWORZYŁEŚ POSTAĆ O PSEUDONIMIE",nick,"KTÓRA MA",age,"lat!")
        elif plec=="K" or plec=="k":
            print("WŁAŚNIE STWORZYŁAŚ POSTAĆ O PSEUDONIMIE",nick,"KTÓRA MA",age,"lat!")
        else:
            print("UTWORZONO POSTAĆ O PSEUDONIMIE",nick,"KTÓRA MA",age,"lat!")
        print ("CO CHCESZ DALEJ ZROBIĆ?")
        print("[0] WYJŚCIE")
        print("[1] EDYTOWAĆ NAZWĘ POSTACI")
        x=input()
        x=int(x)
        if x==0:
            print("WYJŚCIE!")
        elif x==1:
            print("EDYTUJESZ NAZWĘ POSTACI!")
            print("[1] ZMIANA PSEUDONIMU NA DUŻE LITERY")
            print("[2] ZMIANA PSEUDONIMU NA MAŁE LITERY")
            print("[3] ZMIANA PSEUDONIMU - WYBRANA LITERA JEST DUŻA,RESZTA LITER JEST MAŁA")
            print("[4] ZMIANA PSEUDONIMU - WYBRANA LITERA JEST MAŁA,RESZTA LITER JEST DUŻA")
            wybor=input()
            wybor=int(wybor)
            if wybor==1:
                nick=nick.upper()
                print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                print("POWRÓT DO MENU")
                x=0
            elif wybor==2:
                nick=nick.lower()
                print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                print("POWRÓT DO MENU")
                x=0
            elif wybor==3:
                nr=input("KTÓRA LITERA TWOJEGO PSEUDONIMU MA ZOSTAĆ ZMIENIONA NA DUŻĄ? LICZYMY OD 0! - ")
                nr=int(nr)
                nr1=nr+1
                nick=nick.lower()
                ostLit=(len(nick))
                print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick[nr-nr:nr]+nick[nr:nr1].upper()+nick[nr1:ostLit].lower())
            elif wybor==4:
                while wybor==4:
                    nr=input("KTÓRA LITERA TWOJEGO PSEUDONIMU MA ZOSTAĆ ZMIENIONA NA MAŁĄ? - ")
                    nr=int(nr)
                    if nr<=len(nick):
                        nr1=nr+1
                        nick=nick.upper()
                        ostLit=(len(nick))
                        print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick[nr-nr:nr]+nick[nr:nr1].lower()+nick[nr1:ostLit].upper())
                        zadowolony=input("CZY JESTEŚ Z NIEGO ZADOWOLONY?" )
                        wybor=0
                        x=0
                    else:
                        print("TWÓJ NICK NIE JEST TAK DŁUGI!")
                        print("CO CHCESZ ZROBIĆ?")
                        print("[0] WYJŚCIE DO MENU")
                        print("[1] PONOWNA EYCJA NICKU")
                        wybor=input()
                        wybor=int(wybor)
                        if wybor==1:
                            print("PONOWNA EDYCJA NICKU")
                            wybor=4
                        else:
                            print("PRZEJŚCIE DO MENU")
                            x=0
            else:
                print("BŁĘDNA KOMENA, DANE NIE ZOSTANĄ ZAPISANE. POWRÓT DO MENU!")
                x=0;
        else:
            print("BŁĘDNA KOMENDA! PRZEKIEROWANIE DO MENU!")
            x=int(0);
    elif x==2: 
        print("[2] WCZYTAJ GRE")
        print("JAKI MOMENT GRY CHCESZ WCZYTAĆ?")
        print("[1] ULUBIONE")
        print("")
        print("[0] WYJSCIE")
        y=input()
        y=int(y)
        if y==0:
            print("WYJŚCIE!")
            del y
            x==0
        elif y==1:
            print("[2.1] ULUBIONE")
            print("TUTAJ SĄ ZAPISANE TWOJE ULUBIONE MOMENTY Z GRY")
            print("")
            print("[0] WYJŚCIE")
            x=input()
            x=int(x)
            if x==0:
                print("PRZEKIEROWANIE DO GŁÓWNEGO MENU!")
                x==0
            else:
                print("BŁĘDNA KOMENDA! PRZEKIEROWANIE DO MENU!")
                x=int(0);
        else:
            print("BŁĘDNA KOMENDA! PRZEKIEROWANIE DO MENU!")
            x=int(0);
    elif x==3: 
        print("[3] NAJLEPSZE WYNIKI")
        wynik = int(1)
        while wynik<11:
            print (wynik,"BRAK NAJLEPSZEGO WYNIKU")
            wynik = wynik + 1
            
        print("[0] WYJŚCIE")
        x=input()
        x=int(x)
        if x==0:
            print("WYJŚCIE")
        else:
            print("BŁĘDNA KOMENDA! PRZEKIEROWANIE DO MENU!")
            x=0;
    elif x==4: 
        print("[4] TWÓRCY")
        print("WSZYSTKO TUTAJ ROBIĘ SAM, NIE BĘDĘ SIĘ ZBĘDNIE ROZPISYWAĆ :)")
        print ("[0] EXIT")
        x=input()
        x=int(x)
        if x==0: 
            print("WYJŚCIE DO MENU!")
        else:
            print("COŚ ŹLE CI SIĘ PRZYCISNĘŁO, PRZEKIEROWANIE DO MENU")
            x=0;
    elif x==5: 
        print("[5] CHOINKA")
        print("TU PO PROSTU WYDRUKUJĘ CHOINKĘ, OK?")
        ok=input()
        print("")
        if ok=="ok" or ok=="OK" or ok=="TAK" or ok=="tak":
            ch=int(0)
            print("ILE POZIOMÓW MA POSIADAĆ CHOINKA? ")
            ch1=input()
            print("Z JAKIEGO ZNAKU POINNA BYĆ CHOINKA? ")
            znak=input()
            znak=str(znak)
            ch1=int(ch1)
            while ch<ch1:
                print(ch*znak)
                ch+=1
            print(znak)
            print("\nCHOINKA O WYSOKOŚCI",ch1,"ZE ZNAKU",znak,"POWINNA BYĆ NARYSOWANA")
            print("CO DALEJ?")
            print ("[0] EXIT")
            x=input()
            x=int(x)
            if x==0:
                print("WYJŚCIE DO MENU!")
            else:
                print("COŚ ŹLE CI SIĘ PRZYCISNĘŁO, PRZEKIEROWANIE DO MENU")
                x=0
        else:
            print("NIE CHCESZ CHOINKI? TO SPADAJ DO MENU\n")
            x=0
    elif x==6: 
        print("[6] WYJŚCIE")
        print("CZY CHCESZ OPUŚCIĆ GRĘ? T/N")
        decyzja=input()
        decyzja=str(decyzja)
        if decyzja=="T" or decyzja=="t":
            print("DO WIDZENIA!")

        elif decyzja=="N" or decyzja=="n":
            print("POWRÓT DO MENU!")
            x=0
        else:
            print("NIEPOPRAWNA KOMENDA, POWRÓT DO MENU")
            x=0
    else:
        print("BŁĘDNIE WYBRANA KOMENDA!")
        x=int(0)