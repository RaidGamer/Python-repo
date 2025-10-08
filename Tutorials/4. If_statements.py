#tar med lite user input funktioner från förra kapitel
ålder = input("Hur gammal är du?: ")
ålder2 = int(ålder)
if 18<=ålder2<100 : #glöm aldrig kolon efter villkoret
    print("Du är vuxen.") #Om input gäller >= 18 så kommer detta att printas
elif ålder2 >=100:
    print("Du borde va död.") #ElseIf som förkortas elif sätts in om flera villkor behövs
elif ålder2 <0:
    print("Du är inte född.")
else: 
    print("Du är en bebis.") #annars printas detta om integer är inder 18


#-logical operators-
#(and, or, not) = used to check if two or more conditional statements
temp = int(input("Vad är temperaturen där ute?: "))

if temp >= 0 and temp <= 30: #detta kan dock ersättas med "0>=temp>=30" som linje 4
    print("Temperaturen är behaglig!")
    print("Gå ut!")
elif temp < 0 or temp > 30: #detta kan dock skrivas som linje 6 och 8 
    print("Temperaturen är inte behaglig idag!")
    print("Stanna inomhus!")
#om man vill flippa ett villkor utan att behöva skriva om kan man omringa det med not()
if not(temp >= 0 and temp <= 30): 
    print("Temperaturen är inte behaglig idag!")
    print("Stanna inomhus!")
elif not(temp < 0 or temp > 30):
    print("Temperaturen är behaglig!")
    print("Gå ut!")
#det ovan skrivs tvärtom men ger exakt samma output som det emallan linjer 18 och 23
    