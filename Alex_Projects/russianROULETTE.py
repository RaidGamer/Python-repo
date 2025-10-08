import sys 
import os
import random

def main():
    titlescreen()
    input(" ")
    os.system("cls")
    gameloop()
    
    

def chamber():
    bullet = random.randint(1, 6)
    return bullet

def gameloop():
    item = [
    " ─ ",  # First row of the item
    "│ │",  # Second row of the item
    "│ │",  # Third row of the item
    "│_│"   # Fourth row of the item
]
    
    tries = 0
    while True:
        actualchamber = chamber()
        currentchamber = 1  
        print("="*80)
        print("Nu har en kula placerats i revolvern, försök att inte dö nu!")
        for row in item:
            print(row * tries)
        print('''\nVill du:
1) snurra revolver hjulet
2) snurra inte
Skriv nummret nedan som korresponderar med ditt val''')
        val = input("\nDitt val här -> ").upper().strip()
        if val == "1":
            input("\nTryck enter för att snurra revolver hjulet: ")
            spin = chamber()
            if spin == actualchamber:
                print("DU förlora...", end="")
                input(" ")
                sys.exit()
            else:
                tries += 1 
                currentchamber = 1  
        else:
            if currentchamber == actualchamber:
                print("DU förlora...", end="")
                input(" ")
                sys.exit()
            else:
                currentchamber += 1
                tries += 1

        if currentchamber == 6:
            currentchamber = 1
        if tries == 7:
            print("Nice du överlevde, du är fri att gå!")
            input(" ")
            sys.exit()

def titlescreen():
    print('''\n                     +#########                     
                    -###########                    
                  #####      #####                  
            .#########        #########+            
           #####+ +###.       #### -#####           
          ####       ##.     ##.      ####          
         .###-       -#########        ###+         
          ####       ### ##.+##       ####          
           #####+-+###+#    ++####-+#####           
           ###########++    -+###########           
          -####++#++###-##+#+##+      ####          
         -####++###++##########        ####         
          ####++###++###    ###       -###          
           #####+++###-       ##-    ####.          
            ##########        ##########            
              #########      -########+             
                    ######+#####                    
                     ##########                     
    ______ _   _ _____ _____ _____  ___   _   _     
    | ___ \\ | | /  ___/  ___|_   _|/ _ \\ | \\ | |    
    | |_/ / | | \\ `--.\\ `--.  | | / /_\\ \\|  \\| |    
    |    /| | | |`--. \\`--. \\ | | |  _  || . ` |    
    | |\\ \\| |_| /\\__/ /\\__/ /_| |_| | | || |\\  |    
    \\_| \\_|\\___/\\____/\\____/ \\___/\\_| |_/\\_| \\_/    
   ─────────────────────────────────────────────    
 ______ _____ _   _ _      _____ _____ _____ _____  
 | ___ \\  _  | | | | |    |  ___|_   _|_   _|  ___| 
 | |_/ / | | | | | | |    | |__   | |   | | | |__   
 |    /| | | | | | | |    |  __|  | |   | | |  __|  
 | |\\ \\  \\_/ / |_| | |____| |___  | |   | | | |___  
 \\_| \\_|\\___/ \\___/\\_____/\\____/  \\_/   \\_/ \\____/  
─────────────────────────────────────────────────── ''')

if __name__ == "__main__":
    main()