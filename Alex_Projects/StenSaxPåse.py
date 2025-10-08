import random as r
import sys as ter
import string as s
import time as t

def main():

    intro_screen()
    #Vill du börja spelet eller ej?
    print(" ")
    #skriv ja/nej för att börja eller sluta
    börja_spel()
    #username input- ska innehålla name checker som utesluter nummer i namn
    namn = name_checker()
    #introducera spelaren i spelet till motståndaren... som är jag (Alexander Paul Samuel Olivius)
    print("="*104) 
    if namn != "SKAPARENS opp":
      print(f"\n=> Välkommen {namn}! Till... >", end="")
      input(" ")
      t.sleep(1)
      print(" ")
      print("...'STEN | ", end="")
      t.sleep(1)
      print("SAX | ", end="")
      t.sleep(1)
      print("PÅSE'™ !\n")
      t.sleep(2)
      while True:
        spelaförut = input(f"=> Då kommer den viktiga frågan {namn}... har du spelat förut? J/N: ")
        spfö2 = spelaförut.strip().upper()
        if spfö2 == "N":
            regler_ej = input("\n=> Vill du se reglerna? J/N: ")
            reg_ej2 = regler_ej.strip().upper()
            if reg_ej2 == "J":
              print("="*104)
              print("""\n  ┌──────────────────────────────────────────────────────┐ 
    │┼────────────────────────────────────────────────────┼│ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││       ____  _____ ____ _     _____ ____            ││ 
    ││      |  _ \\| ____/ ___| |   | ____|  _ \\   _       ││ 
    ││      | |_) |  _|| |  _| |   |  _| | |_) | (_)      ││ 
    ││      |  _ <| |__| |_| | |___| |___|  _ <   _       ││ 
    ││      |_| \\_\\_____\\____|_____|_____|_| \\_\\ (_)      ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││      1) Sax slår BARA Påse                         ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││      2) Paper slår BARA Sten                       ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││      3) Sten slår BARA Sax                         ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││      4) ? slår ALLT                                ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││      5) SKAPAREN är oslagbar                       ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││               ┌────────STEN◄───────┐               ││ 
    ││               │                    │               ││ 
    ││               │                    │               ││ 
    ││              s│                    │r              ││ 
    ││              l│                    │å              ││ 
    ││              å│         ?          │l              ││ 
    ││              r│                    │s              ││ 
    ││               │                    │               ││ 
    ││               ▼                    │               ││ 
    ││              SAX────────────────►Påse              ││ 
    ││                       slår                         ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    ││                                                    ││ 
    │┼────────────────────────────────────────────────────┼│ 
    └──────────────────────────────────────────────────────┘ """) #regler
              input("\n=> Tryck ENTER om du vill fortsätta: ")
              print(" ")
              print("="*104)
              t.sleep(2)
              print("\n=> Okej bra nu när du vet reglerna...", end="")
              t.sleep(2)
              print("så finns det en till grej du måste veta. >", end="")
              input(" ")
              t.sleep(2)
              print("\n=> Din motståndare.")
              break

            else:
                t.sleep(2)
                print("\n=> Hoppas du kommer ihåg för nu är det för sent att glömma. >", end="")
                input(" ")
                t.sleep(1)
                print(f"   Dock är det inte för sent,{namn}, att lära dig om...", end="")
                t.sleep(2)
                print("din motståndare. >", end="")
                input(" ")
                break
            
        elif spfö2 == "":
            print("Försök igen!\n")
                
        else:
            t.sleep(2)
            print("\n=> Okej bra bra, men det en grej du måste veta...", end="")
            t.sleep(2)
            print("och det är vem din moståndare är. >", end="")
            input(" ")
            break

      t.sleep(2)
      print("\n=> Din motståndare är...", end="")
      t.sleep(1)
      print("LEGENDAREN", end="")
      t.sleep(1)
      print(", DEN BÄSTA", end="")
      t.sleep(1)
      print(", DEN ALLVETANDE", end="")
      t.sleep(2)
      print("... ", end="")
      t.sleep(2)
      print("öööh...", end="")
      t.sleep(2)
      print("aa iallafall det är...\n\n")
      t.sleep(2)
      print(''' _______  _        _______  _______  _______  _______  _______  _       
(  ____ \\| \\    /\\(  ___  )(  ____ )(  ___  )(  ____ )(  ____ \\( (    /|
| (    \\/|  \\  / /| (   ) || (    )|| (   ) || (    )|| (    \\/|  \\  ( |
| (_____ |  (_/ / | (___) || (____)|| (___) || (____)|| (__    |   \\ | |
(_____  )|   _ (  |  ___  ||  _____)|  ___  ||     __)|  __)   | (\\ \\) |
      ) ||  ( \\ \\ | (   ) || (      | (   ) || (\\ (   | (      | | \\   |
/\\____) ||  /  \\ \\| )   ( || )      | )   ( || ) \\ \\__| (____/\\| )  \\  |
\\_______)|_/    \\/|/     \\||/       |/     \\||/   \\__/(_______/|/    )_)
                                                                            >''', end="")
      input(" ")
      t.sleep(1)
      print("\n=> Det är JAG, SKAPAREN av spelet!! >", end="")
      input(" ")
      t.sleep(2)
      print("\n=> JAG! >", end="")
      input(" ")
      t.sleep(1)
      läskigt = input("\n=> Läskigt eller hur? J/N: ").strip().upper()
      if läskigt == "J":
          t.sleep(1)
          print("\n=> Mhm jag håller med. >", end="")
          input(" ")
      else:
          print("\n=> Ok ut med dig.")
          t.sleep(1)
          print(f"\n=> 'SKAPAREN' sparkade '{namn}' från spelet")
          t.sleep(2)
          ter.exit()
      t.sleep(1)
      print(f"\n=> Iallafall {namn} så har vi en match av 'STEN | SAX | PÅSE'™ att spela.")
      t.sleep(1)
      input("\n=> Tryck 'ENTER' för att börja: ")
      print(" ")
      print("="*104)

    else:
        #här är en utgrening av storyn om du har valt namnet av skaparen, han blir galen (jag blir galen)
        print("\n=> Välkom- väl- Huuh!? >", end="")
        input(" ")
        print("\n=> Det kan inte vara... >", end="")
        input(" ")
        print(f"\n=> {namn}!!! >", end="")
        input(" ")
        print("\n=> Hur VÅGAR du visa dig här! Efter vad du gjorde... >", end="")
        input(" ")
        print("\n=> No more mister nice guy >:)... >", end="")
        input(" ")
        skrämma = input("\nVill du ge 'SKAPAREN' en jumpscare? J/N: ").upper().strip()
        if skrämma == "J":
            t.sleep(1)
            print(f'''\n=> '{namn}' skickar zlawg.jpg -
@@@@=:.                                 -                                      
.*@@@*%#-:-=             ::                             .      ..              
@@@@%*=*= @@+           ..          .+%@@@@##+=.   .=. :*=:       .#@*  .  ::. 
%%@@@%*=*%@@@:      .+#@@@@@@@@%@@@@@@@@@@@@@@@@@@*:.:-:::=:    . :+=:::::=*---
%@@@%%%%%@@@@@%:*@@@@@@@@@@@%-=*#@@@@@@@@@@@@@@@@@@@@@*+=-:....:==-:---:.:=====
 :- :%@@@%@@@@@@@@@@@@@@@@#   #%%@@@@@@@@@@@@@@@@@@@@@@@::-:=+--+**:::+++==***+
        %@@%%%@@@@%%%%%@@.  =@%@@@@@@@@@@@@@@@@@@@@@@@@@@@##*=:+*%%=:=+=+==#%#=
      =%%%*+*%%#%#%%%%%#   =##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%*#**######%@@@@%
      ***#+-=****###%%%:  :=**#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@%@@*
      +:++=:==*****%#%*   -==*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++*##@@@@@@@@@
     .==*=. :=+*+***%%: .==+%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@+=*%@*%@#+#@@@@@@@@@@
      :**=.  ::-=*+#%* .-:-*-  .-*%@%@@@@@@@@@@@@@@@@@@@@@*-: *@%@@@@@@@@@@@@@@
::.  :-=#%+   ..=*%%%  .:==*+*=.  :=+*%@@@@@@@@@@@@@@@@@@%*-  .%@%@@@@@@@@@@@@@
#+:===:.-#%=   :*#%%:  -=+:..   ..     :+%%%@@@@@@@@@@@@@%+:   +%%@%@@@@@@@@@@@
=:.:*%#+:=*%+  .*%%*  :=%%**#=      ::..:*%#%@@@@@%%@@@@@%=    *%#%%#@@@@@@@@@@
::::=-=-:-=#%*.:*%#:*=@%%%#*%@#+%@*:::::=+*%%@@@%%#-::----:    ***##%%@@@@@@@@@
   =%@@@%%%%*#*-%%*@@@@***%%***##**+++==+%@@@@%*=:.            %*-*+==*@@@@@@@@
**+*%%%#*:-#@@+#%=@@@@%++=*#%@%%###%@%%#%@@@@%-::.    . .-===  #=-=-::=#@@@@@@@
%@@@@@@@@@@@@@%@#@@@@@*==+==+****%@@@@@@@@@@@%**+*=  *%+.=*@@*.*=:--:::=%@@@@@@
#%@@@@@@@@@@@@%@@@@@@@%%##*******@@@@@@@@@@@@%%%#+*##%#***@@@*.*=:.:.. :=@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%%%**+**%@@@@@@@@@@@%%%#*+===++%@@@@@:*=.     .*@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##%%@@@@@@@@@@@@%%%*=:-==-%@@@@@@.%=      +@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@%##%@@@@%%%#=::-:#@@@@@@@:@+    -#@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@%=+%%%+@@@@@*##-:::@@@@@@@@@*@* .=*@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@%%@@@@@@@@@@%##--=@@@@@@@@@@@+@+%@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@+*@@@@@@@@@@@@%%@@@@@@@@@@@@%%%@@@@@@@@@@@@:%@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@-=@@@@@@@@@@@@@*-==#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@#+:=@@@@%@%%%@@@@%@#-:.:..-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@**-+@@@@#=%%=:-=*#**=::-= =@@@@@*#*@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@*#*=*%@@@@+==*#***--=***++#@%@@@=-++%@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%%%**#%@@@@@***+**#%#==-:::-*%%#====+*%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%%##*##%@@@@@@@+*++++****+==*=: .:===+*%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#%%###*#%@@@@@@@@@%*==-:-=+=:   .--+==+*#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@=%@%%%#*=*%@@@@@@@@@@#***==:.  .::=-===+##%@@@@@@@@@@@@@@@@@@@@@@@@
                                                                                >''', end="")
            input(" ")
            t.sleep(1)
            print("\n=>AAAAAAAAAAAAAAAAAAAAAAAAAAh va i attans är det däääär!!?? >", end="")
            input(" ")
            t.sleep(1)
            print(f'''\n=> 'SKAPAREN' reagerade med ASH_Baby.jpeg -                                                                                                                                                                                   
                                           :=+=======-. ..                                          
                                           .-=:-+****++.     .                                      
                                            .:::--:=+--:     :                                      
                                               ::..:=-:    ..                                       
                                             .:=+=-:::.                                             
                                              .:+*=:::                  .                           
                                             :+*%%@@@%=:       .    ::-.                            
                                            .-*%@@@@@@@@@-         .:=-                             
                                             .+%@@@@@@@@@@@=       --:                              
                                             :**@@@@@@@@@@@@@:     ..                               
                                             .--*%@@@@@@@@@@@@*.                                    
                                            :---=+#%@@@@@@@@@@@=                                    
                   .*#    =%               :=*-:.:*#%@@@@@@@@@@*            -@=   *+                
                    %#    .@:              =*=:   .@@@@#:-%@@@@#            -@@  :#%:               
               %*   *%=   **               *%*#=  #@@@@@%@@@@@@@:           :@@% :**   #:           
               .#@* .=*=:=@+                 :#=   *@@@@*@@@@@@@=           :@@@#**.  :@            
                 =*=-==-=*@*:  =:            *@-    @@@@: %@@@@@@.      @@@**%@@#*%#=#@             
                  :-=+-  :=:  .@.            %+   :*@@@@@ :@@@@@@.      =@@@@@@%+-+%@@.             
              :#@@@@**#=.    =%             -%         @@: *@@@@@         +@@@@*: :**=#             
               +**#****+=: :#*              +#         .*  *@@@@.       .   =@@#      .:            
                      =+*+#@@*              *%=::          %@@@-             .*# ===                
                        =@@%#@=             :@%==:..      =@%%:               .**@@*                
                        *%%==@@=             %%:#%@%=     #@%=                 -+@@*                
                        ====#@@@-            :@ *@@%.   *:%@#*%=  .          :=.=@@:                
                           :*@@@@%:           +  -@@:  @%*@%-.:::**+=:        *%@@%                 
                           .-%@@@@@@%-            -*=*@@@@*                  .*@@@:                 
                            :+@@@@@@@@=            :+@@@@+                   :#@@*                  
                             :+#@@@@@@@+.         :=#@@@%=:              .= :#@@@                   
                              -*#%%@@@#==: .      .=*#%*+==-:            .=-%@%                     
                              .:=*:=%%#*: :::::*##%%%@@@%%#**==.        :=*=.                       
                                .++  ::-.    .=+==#%%#%*#%#%%##==.    :=:                           
                                                                                                    
                                                                                            >''', end="")
            input(" ")
            print("\n=> HAHAHAHahajhhakhdkahskhkah (skrattar psykotiskt) du, DU ska få får det här!!!! >", end="")
            input(" ")

        else:
            print("\nAa jag trodde väll det, du skulle inte våga skräma mig! >", end="")
            input(" ")
            print("Huh isåfall kommer detta vara lätt...", end="")
            input(" ")

        print("\n=> I en match av 'STEN | SAX | PÅSE'™ utmanar jag dig till en DUEL!")
        t.sleep(1)
        input("\n=> Tryck 'ENTER' för att börja: ")
        print(" ")
        print("="*104)

        

    #gör en game loop där spelarens input som är antingen sax, sten, papper ska matchas med ett random val mellan sax, papper, sten som är motståndarens val (mitt val)
    #game loopen måste innehålla villkor där tex sax mot sax leder inte till poäng och görs därför om och att sten inte kan slå papper osv
    #spelet ska gå till 3 poäng, kanske lägger till ett mode där man kan gå till 100 ish poäng o använda andra saker än sax, sten, papper...
    #försök använda ASCII arten nedan för spelaren och motsåtndarens val!
    Din_P = 0
    AlCr_P = 0
    while True:
        aval = randdescBOT().upper()
        print(f"\n'SKAPAREN' poäng: {AlCr_P}")
        print(f"'{namn}' poäng: {Din_P}")
        print("-"*50)
        t.sleep(1)
        if namn != "SKAPARENS opp":
            print('''\n    ┌────────────────────────────┐ 
    │┼──────────────────────────┼│ 
    ││  __     ___    _         ││ 
    ││  \\ \\   / / \\  | |    _   ││ 
    ││   \\ \\ / //_\\\\ | |   (_)  ││ 
    ││    \\ V / ___ \\| |___ _   ││ 
    ││     \\_/_/   \\_\\_____(_)  ││ 
    ││  ────────────────────    ││ 
    ││                          ││ 
    ││ 1) STEN                  ││ 
    ││                          ││ 
    ││ 2) SAX                   ││ 
    ││                          ││ 
    ││ 3) PÅSE                  ││ 
    ││                          ││ 
    │┼──────────────────────────┼│ 
    └────────────────────────────┘ ''')
            t.sleep(1)
        else:
            print('''\n┌────────────────────────────┐ 
│┼──────────────────────────┼│ 
││  __     ___    _         ││ 
││  \\ \\   / / \\  | |    _   ││ 
││   \\ \\ / //_\\\\ | |   (_)  ││ 
││    \\ V / ___ \\| |___ _   ││ 
││     \\_/_/   \\_\\_____(_)  ││ 
││  ────────────────────    ││ 
││                          ││ 
││ 1) STEN                  ││ 
││                          ││ 
││ 2) SAX                   ││ 
││                          ││ 
││ 3) PÅSE                  ││ 
││                          ││ 
││ 4) ? (mystery item)      ││ 
││                          ││ 
│┼──────────────────────────┼│ 
└────────────────────────────┘ ''')
        if namn != "SKAPARENS opp":
            while True:
                ditt_val = input("\n=> Vad väljer du? 1/2/3: ").strip()
                div2 = int(ditt_val)
                if 1 <= div2 <= 3:
                    print(f"  ↪ Val {div2} valt")
                    break
                elif 1 > div2 > 3:
                    print("\n=> Huh? Vad försöker du välja? Det är FRÅN 1 TILL 3!")
                elif div2 == "":
                    print("\n=> Huh? Vad försöker du välja? Det är FRÅN 1 TILL 3!")
        else:
            while True:
                ditt_val = input("\n=> Vad väljer du? 1/2/3/4: ").strip()
                div2 = int(ditt_val)
                if 1 <= div2 <= 4:
                    print(f"  ↪ Val {div2} valt")
                    break
                elif 1 > div2 > 3:
                    print("\n=> Huh? Vad försöker du välja? Det är FRÅN 1 TILL 4!")
                elif div2 == "":
                    print("\n=> Huh? Vad försöker du välja? Det är FRÅN 1 TILL 4!")


        print(" ")
        print("-"*50)
        print("VÄNTAR FÖR SPELARE:")
        print(f"\n=> {namn} har valt")
        slumptid = randtime()
        t.sleep(slumptid)
        print("=> SKAPAREN har valt")
        t.sleep(1)
        print("\nValen är gjorda!")
        t.sleep(1)
        input("\nTryck 'ENTER' för att fortsätta: ")
        print("-"*50)

        t.sleep(2)
        print(" ")
        print('''  ________ ______  ______  __    __ ________   
 |        \\      \\/      \\|  \\  |  \\        \\ 
 | ▓▓▓▓▓▓▓▓\\▓▓▓▓▓▓  ▓▓▓▓▓▓\\ ▓▓  | ▓▓\\▓▓▓▓▓▓▓▓  
 | ▓▓__     | ▓▓ | ▓▓ __\▓▓ ▓▓__| ▓▓  | ▓▓     
 | ▓▓  \\    | ▓▓ | ▓▓|    \\ ▓▓    ▓▓  | ▓▓     
 | ▓▓▓▓▓    | ▓▓ | ▓▓ \\▓▓▓▓ ▓▓▓▓▓▓▓▓  | ▓▓     
 | ▓▓      _| ▓▓_| ▓▓__| ▓▓ ▓▓  | ▓▓  | ▓▓     
 | ▓▓     |   ▓▓ \\ ▓▓    ▓▓ ▓▓  | ▓▓  | ▓▓     
  \\▓▓      \\▓▓▓▓▓▓ \\▓▓▓▓▓▓ \\▓▓   \\▓▓   \\▓▓     
                                               
                                               
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
                    @@@@@                      
              @@@@@@@@@@@@@@@@                 
                @@@@@@@@@@@@@                  
                  @@@@@@@@@                    
                    @@@@@                      
                      @                        
                                               ''')
        if (div2 == 1 and aval == "STEN") or (div2 == 2 and aval == "SAX") or (div2 == 3 and aval == "PÅSE"): #om valen är likadana, ingen får poäng
            if div2 == 1:
                print(f"{namn} lägger ut STEN")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                t.sleep(1)
                print("\nIngen får poäng >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #sten mot sten
                
            elif div2 == 2:
                print(f"{namn} lägger ut SAX")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                print("\nIngen får poäng >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #sax mot sax
                
            elif div2 == 3:
                print(f"{namn} lägger ut PÅSE")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                print("\nIngen får poäng >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #påse mot påse
                
        elif (div2 == 2 and aval== "STEN") or (div2 == 1 and aval == "SAX"): #om det är sax mot sten eller om det är sten mot sax
            if div2 == 2:
                print(f"{namn} lägger ut SAX")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                t.sleep(1)
                AlCr_P += 1
                print("\nPoängen går till SKAPAREN >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #min sax mot alex sten - ALEX,STEN VINNER
              
            elif div2 == 1:
                print(f"{namn} lägger ut STEN")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                t.sleep(1)
                Din_P += 1
                print(f"\nPoängen går till {namn} >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #min sten mot alex sax - JAG,STEN VINNER               


        elif (div2 == 2 and aval == "PÅSE") or (div2 == 3 and aval == "SAX"): #om det är sax mot påse eller om det är påse mot sax
            if div2 == 2:
                print(f"{namn} lägger ut SAX")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                t.sleep(1)
                Din_P += 1
                print(f"\nPoängen går till {namn} >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #min sax mot alex påse - JAG,SAX VINNER
              
            elif div2 == 3:
                print(f"{namn} lägger ut PÅSE")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                t.sleep(1)
                AlCr_P += 1
                print("\nPoängen går till SKAPAREN >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #min påse mot alex sax - ALEX,SAX VINNER
                
        elif (div2 == 3 and aval == "STEN") or (div2 == 1 and aval == "PÅSE"): #om det är påse mot sten eller om det är sten mot påse
            if div2 == 3:
                print(f"{namn} lägger ut PÅSE")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                t.sleep(1)
                Din_P += 1
                print(f"\nPoängen går till {namn} >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #min påse mot alex sten - JAG,PÅSE VINNER
                
            elif div2 == 1:
                print(f"{namn} lägger ut STEN")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval}")
                t.sleep(1)
                AlCr_P += 1
                print("\nPoängen går till SKAPAREN >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #min sten mot alex påse - ALEX,PÅSE VINNER

        if namn == "SKAPARENS opp":
            if div2 == 4:
                print(f"{namn} tar fram ? (mystery item) och det är >", end="")
                input(" ")
                print(f'''\n      :%#:                                              
        :--===:::=-::::*-=*@*:::..:----:::::::::::::::::#  
        -:--==::.:-:.. .......::::.                    .%% 
        *=+==*=::--:.  .       .   .   ..              .%% 
        @@@@@%%%%%%%%%%%%%%%%%%%@%#@%%#%%@@#%%#########%@  
        +@@@%##%######%%##%=%%%@%@%@@@@@@%%%%%%%%@@@@@*  
        :=@@@##%%%%%%#%@@@@@@%%%%@@%@*++=======-:---.    
            @@%%#%%%###%@@@#*+=:::-=+%=                    
            +@@%%%%%%@#%@@%.:+#%      %                     
            @@%%%%%%%%%@@@%%=  :*   *%@-                    
        @@@%%%#%%%#@@%:.  ===-::...                      
        @@@%%%%%%%%@@%                                    
        @@@%%%%%%%%%@@#                                    
    :@@@@%%%%%@%%@@:                                     
    =@@@%@@@@@%@%@@#                                      
    -@@@@%%%%%%%%@@#                                       
    @@@@%@@%@%%%@@%                                        
    :@@@@%%%%%%%%@@:                                        
    %%@@@@@@@@@@#                                         
    :@@@@@@@@@@-                                          
                                                            
    _   _                 _                              
    | | | | __ _ _ __   __| |_   ____ _ _ __   ___ _ __   
    | |_| |/ _` | '_ \\ / _` \\ \\ / / _` | '_ \\ / _ \\ '_ \\  
    |  _  | (_| | | | | (_| |\\ V / (_| | |_) |  __/ | | | 
    |_| |_|\\__,_|_| |_|\\__,_| \\_/ \\__,_| .__/ \\___|_| |_|
                                        |_|                  >''', end="")
                input(" ")
                t.sleep(1)
                print("|\n|\nVS\n|\n|")
                t.sleep(1)
                print(f"SKAPAREN lägger ut {aval} >", end="")
                input(" ")
                t.sleep(1)
                Din_P += 3
                print("\n=> SKAPAREN lämnade")
                print(f"\n=>Motståndaren ur spelet 3 Poäng går till {namn} >", end="")
                input(" ")
                t.sleep(1)
                print("="*104)
                #min pistol mot alex whatever - JAG VINNER
            
        if Din_P >= 3:
            print(f'''\n  ____           _   _   _           _                                _ _ 
 / ___|_ __ __ _| |_| |_(_)___    __| |_   _  __   ____ _ _ __  _ __ | | |
| |  _| '__/ _` | __| __| / __|  / _` | | | | \\ \\ / / _` | '_ \\| '_ \\| | |
| |_| | | | (_| | |_| |_| \\__ \\ | (_| | |_| |  \\ V / (_| | | | | | | |_|_|
 \\____|_|  \\__,_|\\__|\\__|_|___/  \\__,_|\\__,_|   \\_/ \\__,_|_| |_|_| |_(_|_)''')
            break
        elif AlCr_P >= 3:
            print("Du förlora...")
            break

    input("\nTryck 'ENTER' för att gå ut ur spel: ")
    ter.exit()



def intro_screen():
    introscreen = """
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\
\\ \\/\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ \\/ /
 \\/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\/ / 
 / /\\                                                                                    / /\\ 
/ /\\ \\   ____ _____ _____ _   _   _   ____    _    __  __  _   ____  _   ____  _____    / /\\ \\
\\ \\/ /  / ___|_   _| ____| \\ | | | | / ___|  / \\   \\ \\/ / | | |  _ \\(o) / ___|| ____|   \\ \\/ /
 \\/ /   \\___ \\ | | |  _| |  \\| | | | \\___ \\ / _ \\   \\  /  | | | |_) /_\\ \\___ \\|  _|      \\/ / 
 / /\\    ___) || | | |___| |\\  | | |  ___) / ___ \\  /  \\  | | |  __/ _ \\ ___) | |___     / /\\ 
/ /\\ \\  |____/ |_| |_____|_| \\_| | | |____/_/   \\_\\/_/\\_\\ | | |_| /_/ \\_\\____/|_____|   / /\\ \\
\\ \\/ /                           |_|                      |_|                           \\ \\/ /
 \\/ /                                                                                    \\/ / 
 / /\\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\\ 
/ /\\ \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\/\\ \\
\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 
"""
    print(introscreen)

def börja_spel():
    while True:
        userval = input("Vill du börja spel? J/N: ".rjust(59))
        userval2 = userval.strip().upper()
        if userval2 == "J":
            break
        else:
            ter.exit()
        
def name_checker():
  while True:
    användarnamn = input("\n\nSkriv dit namn => ").strip()

    hasdigit = any(char.isdigit() for char in användarnamn)

    ascciChar = s.punctuation 
    hasASCII = any(char in ascciChar for char in användarnamn)

    längd = len(användarnamn)

    if hasdigit == False and hasASCII == False:
        if längd < 4:
            print("Namn nekat, måste vara större än 3 bokstäver!")
        elif längd > 25:
            print("Namn nekat, måste vara mindre än 25 bokstäver!")
        else:
            print(f"\n'{användarnamn}' accepterat!")
            return användarnamn
    else:
        print("Namn nekat, får bara innehålla bokstäver!")
            
def randdescBOT():
    actions = ["sax", "sten", "påse"]
    BotVAl = r.choice(actions)
    return BotVAl

def randtime():
    olikatider = [1,2,3]
    randtid = r.choice(olikatider)
    return randtid


if __name__ == "__main__":
  main()