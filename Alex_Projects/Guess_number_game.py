import random 
import sys as ter
#majoritet av koden gjordes mha AI några villkor och nammn på variabler ändrades, ville lära mig loops

def Nummer_leken():
    random_number = random.randint(1, 100)
    tries = 10 

    print("="*71)
    print("Välkommen till 'Gissa Nummret'!".upper())
    print("I detta spel kommer du gissa ett nummer från 1 till 100.")
    print(f"Du har {tries}st försök för att gissa rätt svar.\n")

    #Game Loop
    while tries > 0:
        gissning = int(input("Vad gissar du för nummer?: "))

        if gissning == random_number:
            print("Yay, du gissade korrekt nummer!")
            break
        elif gissning < random_number:
            print("Nummret är för litet!")
        
        else:
            print("Nummret är för stort!")

        tries -= 1
        print(f"Du har {tries}st försök kvar\n")

    if tries == 0:
        print(f"Ojsan dojsan du fick slut på dina försök, det rätt nummret var {random_number}.\nBättre lycka nästa gång!")
        

    print("="*71)

Nummer_leken()