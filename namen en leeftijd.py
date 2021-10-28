Opnieuw = 'doorgaan'
while Opnieuw == "doorgaan":  
    Naam = input("wat is uw naam? ")
    Leeftijd = input("Wat is uw leeftijd? ")
    if (Naam or Leeftijd) == "stop":
        Opnieuw = "stop"
    else:
        def GebruikerNaam(x,y):
            print ("Hallo", x , "je leeftijd is",y, "jaar")

        GebruikerNaam(Naam,Leeftijd)