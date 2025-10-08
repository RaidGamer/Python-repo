import time

# -Infinite loop-
# while 1==1: #eftersom villkoret alltid är sant kommer det att printas i en loop för alltid
#     print("Hjälp, jag är fast i en loop, skibidi.")

# -While loop- 
# = a statement that will execute it's block of code
#   as long as it's condition remains true.
# Tex om ett program frågar efter ditt namn och du skippar det kommer programmet
# fortfarande vara öppet men inte fortsätta.

name = ""

while len(name) == 0: #Som i if statements sluta villkoret med ett kolon
    name = input("Enter your name: ")

print("Hello " + name)








# -For loop- for variabel_namn in funktion
# = a statement that will execute it's block of code 
#   a limited amount of times
#             while loop = unlimited or infinite
#             for loop = limited

for i in range(10): #i är bas variabel i for loops som upprepar en loop av nummer från 0 till 9 mha range()
    print(i+1) #om det bara var i skulle det vara från 0 till 9

for i in range(50, 100+1): 
    print(i)
#Från nummer 50 till 100, sista nummret är uteslutet (101)-
#-och tar bara med nummer från 50 till näst sista nummret

for i in range(50, 100+1,2): #går upp med 2 istället för 1 varje index
    print(i)

for i in "Alexander Olivius":
    print(i)

# #-Countdown timer-
for timer in range(10,0,-1):
    print(timer)
    time.sleep(1)
print("Allahu Ahkbar")








#-Nested loop- 
# = The "inner loop" will finnish all of it's iterations before finishing
#one iteration of the "outer loop"

rows = int(input("Hur många rader vill du ha?: "))
columns = int(input("Hur många kolumner vill du ha?: "))
symbol = input("Vilken symbol vill du använda?: ")

for i in range(rows): #i används för outer loop x-axel
    for j in range (columns): #j används för inner loop y-axel
        print(symbol, end="")
    print()











#-Loop Controls- Break, Continue, Pass

#Break - Avslutar operationen helt och hållet
while True: 
    name = input("Enter your name: ")
    if name != "":
        break

#Continue - skippar till nästa iteration av loopen
telefon = "499-82-14-07"

for i in telefon:
    if i == "-":
        continue
    print(i, end="")

#Pass - gör ingenting mer av placeholder
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
