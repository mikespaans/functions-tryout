Getal1 = 0
Getal2 = 1
Doorgaan = 'doorgaan'

while Doorgaan == 'doorgaan':
    Getal2 = Getal1 + Getal2
    Getal1 = Getal1 + Getal2
    print (Getal2)
    print (Getal1)
    if Getal1 >= 1000:
        Doorgaan ='stop'