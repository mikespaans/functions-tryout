Nummer1 = 0
Nummer2 = 1

def FunctieSom(Getal1,Getal2):
    Doorgaan = 'doorgaan'
    while Doorgaan == 'doorgaan':
        Getal2 = Getal1 + Getal2
        Getal1 = Getal1 + Getal2
        print (Getal2)
        print (Getal1)
        if Getal1 >= 1000:
            Doorgaan ='stop'
FunctieSom(Nummer1, Nummer2)