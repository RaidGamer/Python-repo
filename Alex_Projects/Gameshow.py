import time as t 
import sys as terminate
import random as r

def main():
    intro()
    #Nedan kan man skriva ja/nej om man vill börja
    while True:
        påbörja_spel = input("Vill du börja spelet? Ja/Nej: ")
        if påbörja_spel in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
            break
        elif påbörja_spel in ["Nej", "nej", " nej", " Nej", "NEJ", " NEJ"]:
            terminate.exit()
    #frågar om ditt namn och checkar om den innehåller nummer och sedan inleder spelet med lite monolog
    while True:
        namn = input("\nVi ser att du inte har ett namn! Vad vill du heta?: ").strip().title()
        if contains_digit(namn) == False:
            if namn.find(" ") != -1:
                ms = namn.find(" ")
                fnamn = namn[:ms]
                print(f"Hej {fnamn}, ditt namn är accepterat")
                break
            else:
                print(f"Hej {namn}, ditt namn är accepterat")
                break
        else:
            print("Ditt namn innehåller väll inte nummer?")
    #lite loading och suspense, loading sekvensen är helt påhittad, det finns inget som egentligen behöver laddas i 5 sekunder
    t.sleep(2)
    print("\nladdar Trivia...")
    t.sleep(3)
    print("Trivia laddat!\n")
    t.sleep(2)
    print("="*40)
    #introduktion och regler där ditt fina namn från förra inputen tas med
    print("\n(Ljuset på scenen tänds, TV-värden stiger in med ett brett leende och en glimt i ögat)\n")
    t.sleep(3)
    print(f"Hej och välkommen, {namn}, till Trivial Pursuit! Här är reglerna för vårt spännande spel. Du kommer att \nfå svara på 10 frågor. För varje fråga har du tre svarsalternativ, men bara ett är rätt. För varje rätt svar \nfår du 1 poäng. Om du lyckas svara rätt på alla 10 frågor, vinner du ett fantastiskt pris! Är du redo att \ntesta dina kunskaper och ha massor av kul? Låt spelet börja!")
    t.sleep(10)
    #om man vill ha mer lästid, skitonödig feature ngl
    while True:
        mer_lästid = input("\nVill du har mer tid på att läsa? Ja/Nej: ")
        if mer_lästid in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
            print("Ok, snabba upp det lite. Publiken är inte här för att kolla på en oläskunnig dräglande apa...")
            t.sleep(1)
            print("\nJag ger dig 10 sekunder!")
            t.sleep(10)
        elif mer_lästid in ["Nej", "nej", " nej", " Nej", "NEJ", " NEJ"]:
            print("Okej då börjar vi!")
            break
    print("="*40)
    
    trivia_frågor = [
    {
        "fråga": "Vad heter den största öknen i världen?\nA) Saharaöknen\nB) Gobiöknen\nC) Kalahariöknen\n",
        "svar": "A"
    },
    {
        "fråga": "Vilken flod rinner genom Egypten?\nA) Amazonas\nB) Nilen\nC) Mississippi\n",
        "svar": "B"
    },
    {
        "fråga": "Vilket är det högsta berget i Europa?\nA) Mont Blanc\nB) Matterhorn\nC) Elbrus\n",
        "svar": "A"
    },
    {
        "fråga": "Vilken stad kallas 'Ljusstaden'?\nA) New York\nB) Tokyo\nC) Paris\n",
        "svar": "C"
    },
    {
        "fråga": "I vilket land ligger staden Timbuktu?\nA) Mali\nB) Niger\nC) Tchad\n",
        "svar": "A"
    },
    {
        "fråga": "Vem spelar huvudrollen i filmen 'Forrest Gump'?\nA) Tom Hanks\nB) Brad Pitt\nC) Leonardo DiCaprio\n",
        "svar": "A"
    },
    {
        "fråga": "Vilken popgrupp var känd för hits som 'Dancing Queen' och 'Mamma Mia'?\nA) The Beatles\nB) ABBA\nC) Bee Gees\n",
        "svar": "B"
    },
    {
        "fråga": "Vilken TV-serie utspelar sig i staden Springfield?\nA) Family Guy\nB) South Park\nC) The Simpsons\n",
        "svar": "C"
    },
    {
        "fråga": "Vem regisserade filmen 'E.T. the Extra-Terrestrial'?\nA) James Cameron\nB) Steven Spielberg\nC) George Lucas\n",
        "svar": "B"
    },
    {
        "fråga": "Vilken artist är känd som 'The King of Pop'?\nA) Elvis Presley\nB) Michael Jackson\nC) Prince\n",
        "svar": "B"
    },
    {
        "fråga": "Vilket år utbröt andra världskriget?\nA) 1914\nB) 1939\nC) 1945\n",
        "svar": "B"
    },
    {
        "fråga": "Vem var den första presidenten i USA?\nA) Abraham Lincoln\nB) Thomas Jefferson\nC) George Washington\n",
        "svar": "C"
    },
    {
        "fråga": "Vilket årtionde ägde den ryska revolutionen rum?\nA) 1910-talet\nB) 1920-talet\nC) 1930-talet\n",
        "svar": "A"
    },
    {
        "fråga": "Vilket imperium styrdes av Julius Caesar?\nA) Grekiska\nB) Romerska\nC) Egyptiska\n",
        "svar": "B"
    },
    {
        "fråga": "Vilket år föll Berlinmuren?\nA) 1987\nB) 1989\nC) 1991\n",
        "svar": "B"
    },
    {
        "fråga": "Vem skrev 'Don Quijote'?\nA) Miguel de Cervantes\nB) Gabriel Garcia Marquez\nC) Federico Garcia Lorca\n",
        "svar": "A"
    },
    {
        "fråga": "Vilken konstnär målade 'Stjärnenatt'?\nA) Claude Monet\nB) Vincent van Gogh\nC) Pablo Picasso\n",
        "svar": "B"
    },
    {
        "fråga": "Vad heter huvudpersonen i 'Moby Dick'?\nA) Ishmael\nB) Ahab\nC) Queequeg\n",
        "svar": "A"
    },
    {
        "fråga": "Vilket århundrade målade Leonardo da Vinci 'Mona Lisa'?\nA) 1400-talet\nB) 1500-talet\nC) 1600-talet\n",
        "svar": "B"
    },
    {
        "fråga": "Vem skrev 'Frankenstein'?\nA) Mary Shelley\nB) Bram Stoker\nC) Robert Louis Stevenson\n",
        "svar": "A"
    },
    {
        "fråga": "Vilken planet är närmast solen?\nA) Venus\nB) Mars\nC) Merkurius\n",
        "svar": "C"
    },
    {
        "fråga": "Vad är den kemiska beteckningen för vatten?\nA) H2O\nB) CO2\nC) O2\n",
        "svar": "A"
    },
    {
        "fråga": "Vilket djur är känt som 'djurens kung'?\nA) Elefant\nB) Lejon\nC) Tiger\n",
        "svar": "B"
    },
    {
        "fråga": "Vilken typ av träd producerar ekollon?\nA) Ek\nB) Lönn\nC) Björk\n",
        "svar": "A"
    },
    {
        "fråga": "Vad heter den största planeten i vårt solsystem?\nA) Saturnus\nB) Jorden\nC) Jupiter\n",
        "svar": "C"
    },
    {
        "fråga": "Vilken sport är Tiger Woods känd för?\nA) Fotboll\nB) Tennis\nC) Golf\n",
        "svar": "C"
    },
    {
        "fråga": "Vilket land vann FIFA World Cup 2018?\nA) Tyskland\nB) Brasilien\nC) Frankrike\n",
        "svar": "C"
    },
    {
        "fråga": "Vilket spel använder pjäser som kallas riddare, löpare och torn?\nA) Schack\nB) Bridge\nC) Backgammon\n",
        "svar": "A"
    },
    {
        "fråga": "Vilken idrottare är känd som 'The Greatest' i boxning?\nA) Mike Tyson\nB) Muhammad Ali\nC) Floyd Mayweather\n",
        "svar": "B"
    },
    {
        "fråga": "Vilken tävling innebär att simma, cykla och springa i följd?\nA) Triathlon\nB) Decathlon\nC) Pentathlon\n",
        "svar": "A"
    }
]
   
    index = 0
    nummerfr = 1
    poäng = 0
    vald = shufflar(trivia_frågor, 10)

    while index < len(vald):
        print("="*40)
        print(f"{nummerfr}) {vald[index]["fråga"]}")
        usersvar = input("\nVad är ditt svar? A, B eller C: ")
        if usersvar == vald[index]["svar"]:
            poäng += 1
            print(f"\nKorrekt!")
        else:
            print(f"\nFel :(, rätt svar är {vald[index]["svar"]}")
        index += 1
        nummerfr += 1
        
    if  poäng == 10:
        print(f"\nJävlar du fick {poäng} poäng!! Du får ett stort pris för din prestation!")
        while True:
            visa_pris = input("Skriv 'Ja' om du vill se ditt pris!: ")
            if visa_pris in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
                break
            else:
                print("\nKom igen! Du vill väll se ditt fina stora pris, eller?")
        print("Ditt pris är *drumroll\ndrrrrrrrrrrr...\n")
        t.sleep(1)
        print("drrrrrrrr...\n")
        t.sleep(1)
        print("drrrrrrrr...\n")
        t.sleep(1)
        print(''' ____  _  _    ___   ___   ___   ___   ___   ___    _____ _   _ ____   ___  
| ___|| || |  / _ \\ / _ \\ / _ \\ / _ \\ / _ \\ / _ \\  | ____| | | |  _ \\ / _ \\ 
|___ \\| || |_| | | | | | | | | | | | | | | | | | | |  _| | | | | |_) | | | |
 ___) |__   _| |_| | |_| | |_| | |_| | |_| | |_| | | |___| |_| |  _ <| |_| |
|____/   |_|( )___/ \\___/ \\___( )___/ \\___/ \\___/  |_____|\\___/|_| \\_\\___/ 
            |/                |/                                            ''')
        print("*Priset får inte användas för personliga köp/ investeringar enligt sektion 54 under vår EULA, bara doneras till välgörenhetsorganisationen TriviaGroup™*")
        lämna = input("\nNu får du lämna, skriv bara 'Ja' när du vill: ")
        if lämna in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
            terminate.exit()
        else:
            print("Det får duga...")
            t.sleep(2)
            terminate.exit()

    elif 9 == poäng:
        print(f"\nOoh så nära, du fick {poäng} poäng! Du får dock ett tröst pris för din prestation!")
        while True:
            visa_pris = input("Skriv 'Ja' om du vill se ditt pris!: ")
            if visa_pris in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
                break
            else:
                print("\nKom igen! Du vill väll se ditt fina tröst pris, eller?")
        print("Ditt pris är *drumroll\ndrrrrrrrrrrr...\n")
        print("drrrrrrrr...\n")
        t.sleep(1)
        print("drrrrrrrr...\n")
        t.sleep(1)
        print(''' _____    _       _       _  ______                     _ _                  
|_   _|  (_)     (_)     | | | ___ \\                   (_) |                 
  | |_ __ ___   ___  __ _| | | |_/ /   _ _ __ ___ _   _ _| |_                
  | | '__| \\ \\ / / |/ _` | | |  __/ | | | '__/ __| | | | | __|               
  | | |  | |\\ V /| | (_| | | | |  | |_| | |  \\__ \\ |_| | | |_                
  \\_/_|  |_| \\_/ |_|\\__,_|_| \\_|   \\__,_|_|  |___/\\__,_|_|\\__|               
                                                                             
                                                                             
           ______               _                _                           
           | ___ \\             | |              | |                          
           | |_/ / ___  _ __ __| |___ _ __   ___| |                          
           | ___ \\/ _ \\| '__/ _` / __| '_ \\ / _ \\ |                          
           | |_/ / (_) | | | (_| \\__ \\ |_) |  __/ |                          
           \\____/ \\___/|_|  \\__,_|___/ .__/ \\___|_|                          
                                     | |                                     
                                     |_|                                     \n''')
        print("*Signierad kopia av Herr John Trivia*")
        lämna = input("\nNu får du lämna, skriv bara 'Ja' när du vill: ")
        if lämna in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
            terminate.exit()
        else:
            print("Det får duga...")
            t.sleep(2)
            terminate.exit()

    elif 7 == poäng == 8:
        print(f"\nBra jobbat du fick {poäng} poäng! Men du kan göra bättre än så.")
        lämna = input("\nNu får du lämna, skriv bara 'Ja' när du vill: ")
        if lämna in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
            terminate.exit()
        else:
            print("Det får duga...")
            t.sleep(2)
            terminate.exit()

    elif 5 < poäng == 6:
        print(f"\nDu gjorde måttligt bra, du fick {poäng} poäng.")
        lämna = input("\nNu får du lämna, skriv bara 'Ja' när du vill: ")
        if lämna in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
            terminate.exit()
        else:
            print("Det får duga...")
            t.sleep(2)
            terminate.exit()

    elif 0 < poäng <= 5:
        print(f"\nDu fick {poäng} poäng, du behöver slipa på dina kunskaper.")
        lämna = input("\nNu får du lämna, skriv bara 'Ja' när du vill: ")
        if lämna in ["Ja", "ja", " ja", " Ja", "JA", " JA"]:
            terminate.exit()
        else:
            print("Det får duga...")
            t.sleep(2)
            terminate.exit()

    elif 0 == poäng:
        print(f"\nI alla mina dagar har jag aldrig sett någon prestera så dåligt som du, ut med dig!")
        t.sleep(5)
        terminate.exit()

        
#TRIVIA intro screen 
def intro():

    print('''\n████████╗██████╗ ██╗██╗   ██╗██╗ █████╗ 
╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗
   ██║   ██████╔╝██║██║   ██║██║███████║
   ██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║
   ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝''')
    print("Python Edition".center(40, "=").upper())
    print("Presenteras av TriviaGroup™\n".center(40))
#funktion som checkar om det finns nummer i ditt namn
def contains_digit(s):
    return any(char.isdigit() for char in s)
#funktion som shufflar flera hundra frågor och tar ut endast tio stycken från de
def shufflar(input, nummer):
    mellan = input[:]
    r.shuffle(mellan)
    output = r.sample(mellan, nummer)
    return output


if __name__ == "__main__":
    main()
 



