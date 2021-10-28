Nummer1 = int(input("Wat is nummer 1? "))
Nummer2 = int(input("Wat is nummer 2? "))

#de plus functie
def addition(number1, number2):
    Answer = number1 + number2
    print (str(number1) ,"+", str(number2) ,"=",  str(Answer))
addition(Nummer1 , Nummer2)

#de min functie
def subtraction(number1, number2):
    Answer = number1 - number2
    print (str(number1) ,"-", str(number2) ,"=", str(Answer))
subtraction(Nummer1, Nummer2)

#de keer functie
def multiplication(number1, number2):
    Answer = number1 * number2
    print (str(number1) ,"*", str(number2) ,"=", str(Answer))
multiplication(Nummer1, Nummer2)

#de deel functie
def division(number1, number2):
    Answer = number1 / number2
    print (str(number1) ,":", str(number2) ,"=", str(Answer))
division(Nummer1, Nummer2)

#de plus 1 functie
def decrement(number):
    Answer = Nummer1 + 1
    print (str(number) ,"+", str(1) ,"=", str(Answer))
decrement(Nummer1)

def decrement(number):
    Answer = Nummer1 - 1
    print (str(number) ,"-", str(1) ,"=", str(Answer))
decrement(Nummer1)
