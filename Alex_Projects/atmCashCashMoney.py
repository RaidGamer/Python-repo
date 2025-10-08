import sys as terminate

def main():

    print('''   █████████   ███████████ ██████   ██████
  ███░░░░░███ ░█░░░███░░░█░░██████ ██████ 
 ░███    ░███ ░   ░███  ░  ░███░█████░███ 
 ░███████████     ░███     ░███░░███ ░███ 
 ░███░░░░░███     ░███     ░███ ░░░  ░███ 
 ░███    ░███     ░███     ░███      ░███ 
 █████   █████    █████    █████     █████
░░░░░   ░░░░░    ░░░░░    ░░░░░     ░░░░░ ''')
    print("AUTOMATED TELLER MACHINE".center(42,"="))
    
    pincode("1234", 3) #funktion for pinkoden, parametrarna är koden och antalet försök
    mainmenu(10000) #funktion för menyn i atm, parametrarna är saldon
    

def pincode(code: str, tries: int):
    print(f"\nDu har {tries} försök för att få Pin-Koden rätt!".upper())
    Realtries = tries
    while Realtries > 0: #loop som sker tills antalet försök når noll
        if str(input("Pin-Kod: ")) == code: #om den inskrivna koden är korrekt bryts loopen och försätter till menyn
            print("Korrekt kod inskriven!\n")
            break
        
        else:
            Realtries -= 1 #för varje försök minskar det med 1
            if Realtries > 0: #om försöken är fortfarande över noll så fortsätter loopen 
                print(f"Fel Pin-Kod, försök igen. Du har {Realtries}st försök kvar!\n")
            else: #om alla försök är använda slutas programmet
                print("Dina tre försök har misslyckats, kom tillbaka senare för att logga in!")
                terminate.exit()

def mainmenu(saldo: int): #menyn för atm
    while True:
        print("="*42)
        print(f"Nuvarande saldo: {saldo:,}")
        print("Val:\n")
        print("1) Ta ut pengar")
        print("2) Sätt in pengar")
        print("3) Exit\n")
        actionUSER = int(input("Välj enligt nummerna, vad du vill göra: "))

        if actionUSER == 1: #om 1 väljs sätt användaren i en loop inanför en loop nedanför, där de antinge kan ta ut pengar eller gå tillbaka till meny loopen
            while True:
                ta_ut= int(input("\nHur mycket vill du ta ut? Om du vill tillbaka skriv '0': "))
                if  0 < ta_ut <= saldo:
                    saldo = saldo - ta_ut
                    print(f"{ta_ut:,}kr togs ut ur kontot")
                    break
                elif ta_ut < 0 or ta_ut > saldo:
                    print("Det gick inte ta ut den efterfrågade summan!")
                else:
                    break


        if actionUSER == 2: #om 2 väljs sätt användaren i en loop inanför en loop nedanför, där de antinge kan sätta in pengar, under 15000, eller gå tillbaka till meny loopen
            while True:
                sätt_in = int(input("\nHur mycket vill du sätta in (Begränsing är 15,000kr)? Om du vill tillbaka skriv '0': "))
                if 0 < sätt_in <= 15000:
                    saldo = saldo + sätt_in
                    print(f"{sätt_in:,}kr sattes in på kontot")
                    break
                elif sätt_in < 0 or sätt_in > 15000:
                    print("Det gick inte ta ut den efterfrågade summan!")
                else:
                    break
        
        if actionUSER == 3: #om 3 väljs kommer meny loopen brytas och därmed programmet avslutas
            print("Användaren lämnade")
            break
            
main()