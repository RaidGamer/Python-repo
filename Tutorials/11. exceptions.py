#keywords = "try" and "except"

try: #prova att ge user denna input
    x = int(input("Vad är x?: "))
except ValueError: #i fallet av en error (i det här fallet ValueError) printa detta meddelande!
    print("x får bara vara ett nummer!")
else:
    print(f"x är {x}!") #om ingen error är skapad kan detta printas då x har ett värde, x har inget värde dock om input är str pga int() och då skrivs except delen








#det ovan kan också skrivas inom en while True loop som aldrig slutas så länge du skriver in ett nummer...
while True:
    try: #prova att ge user denna input
        x = int(input("\nVad är x?: "))
    except ValueError: #i fallet av en error (i det här fallet ValueError) printa detta meddelande!
        print("x får bara vara ett nummer!")
    else: #om ingen error skapas bryts while loopen som därmed gör bool värdet av True till False
        break

print(f"x är {x}!") #Då while loopen bryts printas detta meddelande.











#kan också skrivas som en def funktion...
def main():

    myInt = get_int() #eftersom vi har return x i funktionen kan vi göra literal assignment för funktionen till en variabel "myInt"
    print(f"x is {myInt}") #här printas x är "myInt"


def get_int(): #while loopen är nu definierad inom en funktion som kan kallas närsomhelst
    while True:
        try: 
            x = int(input("\nVad är x?: "))
            return x #för att funktionen inte bara ska vara en bi-effekt utan faktiskt ska ge nånting tillbaka, i det här fallet x, så skriver man "return x" 
                     #den gör också jobbet av att bryta ut ur loopen som break, därför behöver inte break skrivas
        except ValueError: 
            print("x får bara vara ett nummer!") #print() delen kan också bytas ut mot bara pass, då komme inget skrivas men errorn har hanteras och därmed inte crashar programmet
        #else: behöver inte skrivas för return x kan redan skrivas i try delen, eftersom errorn skapas innan x får ett assignment, funkar inte i alla tillfällen dock
            
    



main()



#ett till exempel...
try: #try division med nummer, "int()"" och "result = numerator / denominator" delen är farlig kod för att man vet inte vad usern kan skriva in 
    numerator = int(input("Enter a number to divide by: "))
    denominator = int(input("Enter a number to  divide by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e: #mer specifik exception hantering där en specifik erro då man dividerar med 0 sker, här hanteras den 
    print(e) #man kan printa ut den specifika errorn med ens valfria namn (e) och berätta för usern vad de gjorde fel
    print("Can't divide by zero...")
except ValueError as e: #här hanteras erorrs då man sätter in strings istället för integers, strings kan inte divideras med varandra, duh
    print(e)
    print("Can't divide letters... ")
except Exception as e: #dåligt att skriva "Exception" för alla errors, gör det svårare att fånga bugs i koden om man inte vet de specifika exceptions
    print(e)
    print("Sth went wrong :(")
else: #om inget går fel printa ut detta, genom ett "else:" kan skrivas på andra sätt som visats ovan
    print(result)
finally: #finally är en del av try-except som printas ut oavsett vad som hänt tidigare
    print("kommer alltid att printas oavsett error eller inte")
