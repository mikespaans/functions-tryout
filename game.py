def WitRegel():
    print ("    ")
StartGame = input("type iets om de game te starten ")
WitRegel()
print ("Je bent verdwaald in een onbekend bos.")
print ("In dit bos lopen gevaarlijke beesten.")
print ("Om deze beesten te kunnen verslaan moet je wapens en levens zien te krijgen.")
print ("Je begint met 50 health en geen wapens")
print ("Om meer health te krijgen kan je appels vinden en opeten")
WitRegel()

def VerderLopen():
    print ("Je loopt verder.")
def Overleefd():
    print ("Je hebt het overleefd.")
def NietOverleefd():
    print ("Je hebt het niet overleefd.")
def UitgangZien():
    print ("Je ziet de uitgang van het bos.")
def BoomKlimmen():
    print ("Je klimt de boom in om naar het tasje toe te gaan")
def AppelGegeten():
    print ("Je hebt de appel gegeten en je krijgt 20 health erbij.")
def AppelNietGegeten():
    print ("Je hebt de appel niet gegeten.")
def TotaleHealth():
    print ("Je health is", Health)


GoedeAppel = 20
EerstePadKiezen = input("je komt op een splitsing van 2 paden welke kant ga je op 1. links of 2. rechts? ")
if EerstePadKiezen == "1":
    print ("Je bent het linker pad ingegaan.")
    WitRegel()
    AppelEten = input("Je ziet een appel onder een boom liggen, ga je hem opeten 1. ja of 2. nee? ")
    if AppelEten == "1":
        Health = 70
        AppelGegeten()
        TotaleHealth()
    else:
        Health = 50
        AppelNietGegeten()
        TotaleHealth()

    WitRegel()
    VerderLopen()
    KleinHutje = input("Je ziet een klein hutje 1. kijk erin of 2. loop verder? ")
    if KleinHutje == "1":
        ZakMes = 'gekregen'
        print ("Je gaat naar binnen. ")
        print ("Je bent binnen en ziet een klein zakmes liggen deze neem je mee.")
        print ("Je gaat weer naar buiten")
        WitRegel()
        VerderLopen()
    else:
        ZakMes = 'niet gekregen'
        WitRegel()
        print ("Je gaat niet naar binnen en loopt verder ")
    WitRegel()
    print ("Je ziet een wolf en hij valt je aan.")
    if Health >= "70" and ZakMes == "gekregen":
        print ("De wolf heeft je 1 keer gebeten voordat je hem met je zakmes stak.")
        print ("Je totale health is met 10 afgenomen.")
        print ("Totale health 60.")
        TotalHealth = 60
    elif Health >= "70" and ZakMes == "niet gekregen":
        print ("De wolf heeft je aan gevallen en heeft je 2 keer gebeten voordat hij wegrende.")
        print ("Je totale Health 50.")
        TotalHealth = 50
    elif Health <= "50" and ZakMes == "gekregen":
        print ("De wolf heeft je 1 keer gebeten voordat je hem met je zakmes stak.")
        print ("Je totale health 40")
        TotalHealth = 40
    elif Health <= "50" and ZakMes == "niet gekregen":
        print ("De wolf heeft je 2 keer gebeten voordat hij wegrende.")
        print ("Je totale health 30.")
        TotalHealth = 30
    WitRegel()
    VerderLopen()
    AppelEtenKeuze = input("Je ziet weer een appel liggen eet je hem op 1. ja 2. nee? ")
    if AppelEtenKeuze == ("1"):
        AppelGegeten()
        print ("je totale health is: ")
        print (TotalHealth + GoedeAppel)
        NewHealth = TotalHealth + GoedeAppel
    else:
        AppelNietGegeten()
        TotaleHealth()
    WitRegel()
    print ("je ziet iets liggen in het gras.")
    WapenKeuze = input("Ga je erheen 1. ja of 2. nee? ")
    if WapenKeuze == "1":
        print ("Je loopt er heen.")
        print ("Het is een pistool.")
        print ("Het pistool neem je mee")
        Wapen = 'Gekregen'
    else: 
        print ("je gaat er niet heen")
    VerderLopen()
    WitRegel()
    UitgangZien()
    print ("Maar plotseling komt er een beer")
    KeuzeBeer = input("1. wat doe je naar de uitgang rennen of 2. tegen de beer vechten? ")
    if KeuzeBeer == "2":
        if NewHealth >= 70 and Wapen == "Gekregen":
            WitRegel()
            print ("je hebt de beer neergeschoten en verlaat het bos")
            Overleefd()
        else:
            print ("Helaas de beer was te sterk en heeft je gedood.")
            NietOverleefd()
    else:
        WitRegel()
        print ("Helaas de beer kwam achter je aan en was sneller dan jij.")
        NietOverleefd()
else:
    print ("Je gaat het rechter pad in.")
    AppelEten = input("Je ziet een appel onder een boom liggen, ga je hem opeten 1. ja of 2. nee? ")
    if AppelEten == "1":
        Health = 70
        AppelGegeten()
        print ("Totale health ",Health)
    else:
        Health = 50
        AppelNietGegeten()
        print ("Je health blijft", Health)
    WitRegel()
    VerderLopen()
    print ("Je ziet een huis.")
    HuisKeuze = input("Ga je het huis in 1. ja of 2. nee? ")
    if HuisKeuze == "1":
        ZakMes = 'gekregen'
        print ("Je gaat het huis in.")
        print ("Plotseling word je door een hond gebeten in het huis vervolgens rent deze weg.")
        print ("je nieuwe totale health is:")
        print (Health - 10)
        print ("Je loopt verder door het huis en vind een zakmes")
        print ("Je gaat weer naar buiten.")
    else:
        ZakMes = 'niet gekregen'
        print ("Je gaat niet het huis in.")
    WitRegel()
    VerderLopen()
    print ("Je ziet een tasje in een boom hangen.")
    BoomKeuze = input("wat doe je erheen gaan 1. ja of 2. nee? ")
    if BoomKeuze == ("1"):
        if ZakMes == "gekregen":
            Pistool = 'gekregen'
            WitRegel()
            BoomKlimmen()
            print ("Je hebt het tasje los kunnen snijden.")
            print ("Er zit een pistool in.")
            print ("Je hebt nu een pistool.")
            VerderLopen()
        else:
            BoomKlimmen()
            print ("je bent bij het tasje gekomen maar je kan hem niet pakken.")
            print ("Hij zit vast met een touw en je krijgt hem niet los.")
            VerderLopen()
    else:
        WitRegel()
        VerderLopen()
    WitRegel()
    UitgangZien()
    print ("Maar plotseling verschijnt er een leeuw.")
    LeeuwKeuze = input("Wat doe je 1. naar de uitgang rennen of 2. tegen de leeuw vechten. ")
    if LeeuwKeuze == ("2"):
        if str(Health) >= "60" and Pistool == "gekregen":
            print ("Je hebt de leeuw neergeschoten en verlaat het bos.")
            Overleefd()
        else:
            print ("Helaas de leeuw was sterker dan jij.")
            NietOverleefd()

    else:
        if str(Health) >= "70":
            print ("Je bent snel genoeg het bos uitgerend en de leeuw volgt je niet.")
            Overleefd()
        else:
            print ("Je probeerde het bos uit te rennen.")
            print ("Maar helaas was de leeuw sneller dan jij")
            NietOverleefd()
