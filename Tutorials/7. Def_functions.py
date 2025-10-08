#def = "define" eller att definiera en funktion som inte finns i python

#exempel 1:
def main():
    x = int(input("What's the number x?: "))
    print("x squared is", square(x))

def square(n): #inuti parenteser är parametrar som ändrar funktionen
    return pow(n, 2) #return är ett värde som ges tillbaka till användaren

main() #att ha namnet på funktionen sist är ett sätt att kalla funktionen och initiera den





#exempel 2:
def main2():
    name = input("What's your name?: ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

main2()




#exempel 3:
def main3():
    x = int(input("What is the number x?: "))
    if Odd_Even(x):
        print("Even")
    else:
        print("Odd")

def Odd_Even(n):
    return n % 2 == 0

main3()





#keyword arguments = argument som föregås av en identifierare när vi skickar dem till en funktion. 
#                    Argumentens ordning spelar ingen roll till skillnad från "positional arguments".
#                    Python känner till namnen på argumenten som vår funktion tar emot!
def main4():


    def namn(firstn,melllann,eftern):
        print("Hejsan" + firstn + melllann + eftern)

    namn(eftern = "Olivius",firstn = "Alexander",melllann = "Paul Samuel")

main4()





#nested funktion calls = funktioner som kallas inom funktioner som kallas, kallningarna av funktionerna arbetar sig från inersta parentes till yttersta,
#                        det givna värdet från innersta parentesen ges till den näst innersta osv. En kedjereaktion av givna urkommor som används till nästa kallning av funktioner.

print(round(abs(float(input("Skriv ett helt positivt värde: ")))))

#kan också skrivas så här, nedanför. De är det inte nested funktion calls!

num = input("Skriv ett helt positivt värde: ")
num = float(num)
num = abs(num)
num = round(num)

print(num)





#variable scope = Den regionen där en variabel är igenkänd
#                 En är bara tillgänglig i den region som den var skapad i
#                 En global och lokal version av en variabel kan bli skapad

name = "Alexander" #Global Scope (tillgänglig innuti och utifrån en funktion)

def display_name():
    name = "Olivius" #Local Scope (bara tillgänglig innuti funktionen)
    print(name)

display_name()
print(name)




#*args = parametrar som kommer packa alla givna argument till en tuple, användbar då man vill ha en funktion som kan acceptera en mängd olika argument

def add(*args): #args kan namngivas till vad somhelst men måste behålla "*"
    sum = 0
    stuff = list(args) #om man inte vill ha en tuple från början kan man type-casta den till en list!
    stuff[0] = 0 #nu när tuplen är en list kan man ändra elemntet på index 0 till en integer av 0
    for i in args:
        sum += i
    return sum 

print(add(1,2,3,4,5,6))



#**kwargs = parametrar som kommer packa alla givna argument som keyword argument in till en dictionary, användbar då man vill ha en funktion som kan acceptera en mängd olika argument

def hello(**kwargs): #kwargs kan namngivas till vad somhelst men måste behålla "**"
    # print("Hello" + kwargs["first"] + " " + kwargs["last"])
    print(  "Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title = "Mr ", first = "Alex", middle = "Paul Samuel", last = "Olivius")


#---------------------------------------------------------------------------------------------------------------------------
#Higher order functions - en funktion som man kan passera in en funktion som argument eller att man får en return av en funktion
#------------------------------------------------------------------------------------------------------------------------------

#1:a exempel där funktioner sätts in i en annan funktion

def funk1(text):
    return text.upper()

def funk2(funkn):
    text = funkn("Babajabadoo")
    print(text)

funk2(funk1) #kmr ge BABAJABDOO

#2:a exempel där funktioner returnar som output 

def nämnare(x):
    def täljare(y):
        return y/x
    return täljare

dividera = nämnare(2) #här ges nämnare funktionens argument x värdet 2
print(dividera(32)) #här, eftersom dividera har sammma memory adress som täljare(y) så kan den ta in värdet 32 som argument för y och outputen av allt blir 32/2=16

#---------------------------------------------------------------------------------------------------------------------------
#Lambda funktion - en funktion på en linje, användbara om en funktion behövs bara en gång och är onödig att definiera
#------------------------------------------------------------------------------------------------------------------------------

#vanlig funktion
def dubbel(x):
    return x*2
print(dubbel(5)) #kmr ge 10

#använder lambda funktioner
dubbel = lambda x: x*2
print(dubbel(5)) #kmr också ge 10

#lite mer komplex användning
namn = lambda first, last: first+" "+last
print(namn("Alexander", "Olivius"))

multi = lambda x, y, z: x*y*z
print(multi(1, 2, 3)) #ger 6 eftersom 1*2*3=6