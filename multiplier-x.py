Welkgetal = int(input("Van welk getal wilt u de tafel zien? "))
def TafelGetal(x):
    i = 1
    for i in range(1,11):
        print(x * i)
TafelGetal(Welkgetal)
