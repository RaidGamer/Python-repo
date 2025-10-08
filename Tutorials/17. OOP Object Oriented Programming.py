#A class is like a blueprint or template for creating objects (real instances of something).
# Think of a class as the recipe, and objects as the cookies you bake from it.

class Car:

    wheel = 4 #class variable, implemented into each object no matter what

    def __init__(self, _make, _model, _year, _color): #Constructor which sets up the objects 
        self.make = _make                              #Attributes are some things that belong to an object, aka instance variable
        self.model = _model
        self.year = _year
        self.color = _color

    def driving(self, _model): #self refers to the current object, it is filled automatically for you, no need to fill parameter
        print(f'This {_model} is driving!') #method are functions that belong to an object

    def breaking(self, _model):
        print(f'This {_model} is stopping!')

    def change_name(self, new_name): #u can change attributes as well through method functions built in the class
        self.model = new_name

#----------------------------------------------------------------- Imagine we import this class from another file through from x import y

car_1 = Car("Audi", "R8", 2018, "White")
car_2 = Car("Koenigsegg", "Agera RS", 2011, "Carbon")

print(car_1.make)
print(car_2.model)
print(car_1.year)
print(car_2.color)

print(car_1.wheel)
print(car_2.wheel)

car_1.driving(car_1.model)
car_2.breaking(car_2.model)
car_1.change_name("R4")
print(car_1.model)

Car.wheel = 2 #class variables can be changed outside of their class for an instance

#--------------------------------------------------------------------------------------------------------------
#inheritance 
#-------------------------------------------------------------------------------------------------------------- 

class animal: 

    alive = True 

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class rabbit(animal): #genom att sätta klassen anomal inom det nya klassen rabbit's parenteser så ärver rabbit klassen animal klassens funktioner och varibaler
    def run(self):  #förutom att endast ärva från animal klassen kan rabbit tex ha sina egna funktioner som gör den unik ifrån animal klassen så att den får en unik användning
        print("this rabbit is running")
class fish(animal): #Inheritance är användbart just eftersom då slipper man klistra in samma sak om och om igen i klasser som delar karakteristikor
    def swimming(self): 
        print("this fish is swimming")
class hawk(animal):
    def fly(self):
        print("this hawk is flying")

rabbit = rabbit()
fish = fish()
hawk = hawk()

print(rabbit.alive) #printar True om rabbit klasseb har ärvt animal klassens klass varibabel alive som ger som sagt True
fish.eat() #ger ut 'This animal is eating'
hawk.sleep() #ger ut outputen 'This animal is sleeping' av funktionen i dens ärvda klass
fish.swimming()
hawk.fly

#--------------------------------------------------------------------------------------------------------------
#Sedan kan man nesta eller gör s.k. Multilevel inheritance som är klass som ärver av en klass som ärver osv.
#--------------------------------------------------------------------------------------------------------------

class Organism:
    Alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog = Dog()

print(dog.Alive) #kmr ge output True pga av att den har ärvt Alive=True från organism klassen...
dog.eat()
dog.bark()

#--------------------------------------------------------------------------------------------------------------
# Ett steg till så har vi Multiple inheritance som är att child klasser kan ärva från fler än en parent klass
#--------------------------------------------------------------------------------------------------------------

class Predator:
    def hunt(self):
        print("This pred is huntin")

class Prey:
    def flee(self):
        print("This prey is fleein")

class Fish(Prey, Predator): #ärver från både prey och pred klassen
    pass

fish = Fish()
fish.flee() 
fish.hunt()

#--------------------------------------------------------------------------------------------------------------
#Method overriding är när man har en child klass som ärvt en metod/funktion från en parent men vill gör den mer specifik till child klassen genom att skriva om method signature'n i child klassen.
#--------------------------------------------------------------------------------------------------------------

class Water:
    def Wet(self):
        print("This water is wet")

class River(Water):
    def Wet(self):
        print("This river is wet") #skriver om metod signaturen Wet(self) för anpassning till River klassen

river = River()
river.Wet() #Detta skulle ge "This river is wet" inte "This water is wet" eftersom vi method overrida den.

#--------------------------------------------------------------------------------------------------------------
#Method Chaining - man kallar på flera methods sekventiellt 
#--------------------------------------------------------------------------------------------------------------

class Orientation():
    def upp(self):
        print("This is going upp")
        return self
    def down(self):
        print("This is going down")
        return self
    def right(self):
        print("This is going right")
        return self
    def left(self):
        print("This is going left")
        return self

orient = Orientation()

orient.upp().down().right().left() #man kedjar ihop metoderna för ett mer effektivt sätt att kalla de än vad vi sett innan

#--------------------------------------------------------------------------------------------------------------
#Super function - ger access till methods av en parent klass för att de ska ändras, returnar ett temporärt objekt av parent klassen när detta är gjort
#--------------------------------------------------------------------------------------------------------------

class kvadrat:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class rektangel(kvadrat):
    def __init__(self, lenght, width):
        super.__init__(lenght, width)

    def area(self):
        return self.length*self.width
    
class kub(kvadrat):
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width) #istället för att skriva om samma grej för genom method override kan man använda super funktionen för att göra samma grej
        self.height = height
    
    def volym(self):
        return self.lenght*self.width*self.height
    
kub = kub(3, 3, 3)
rekt = rektangel(3, 3)
kub.volym()
rekt.area()

#--------------------------------------------------------------------------------------------------------------
#Abstract Classes = Om man har en eller flera klasser som har definierade funktioner/metoder utan implementation så vill man ju då inte att en user använder dess funktioner, genom
#                   att göra den abstrakt mha abc modulen så kan metoden -er inte framkallas från den.
#--------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod #om det finns en till abstract metod som inte har overridats i child klassen kmr child klassen inte fungera så länge den har inheritance från föräldern 
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("This car is driving")

class Moped(Vehicle):
    def go(self):
        print("This moped is driving") #och om denna def go(self) skulle vara pass så tillåts den inte heller för essentiellt så är det samma som om Vehcile använde sin go(self) pga inheritance

#om en klass ska inherita en abstrakt klass så måste child klassen method overrida parent klassens def go(self)

veh = Vehicle()
veh.go() #detta går inte eftersom klassen är markerad abstract och kmr inte tillåtas användning

#--------------------------------------------------------------------------------------------------------------
#Objects as arguments - man kan passera objekt/ klasser som argument i en funktion som def change_color()
#-------------------------------------------------------------------------------------------------------------- 

class Car:

    color = None


class Moped:

    color = None

def change_color(vehicle, color):

    vehicle.color = color

car1 = Car()
car2 = Car()
car3 = Car()
mop1 = Moped()

change_color(car1, "red")
change_color(car2, "white")
change_color(car3, "blue")
change_color(mop1, "black")

#--------------------------------------------------------------------------------------------------------------
#Duck Typing - koncept där klass typen är mindre viktigt än dess metoder. klass typen är inte checkad så länge minimum metoder och attributer är närvarande. Om den går och kvackar som en anka är det en.
#-------------------------------------------------------------------------------------------------------------- 

class Duck:
    def walk(self):
        print("Ankan går")

    def kvack(self):
        print("Ankan kvackar")

class Chicken:
    def walk(self):
        print("Kycklingen går")

    def kvack(self):
        print("Kycklingen kacklar")

class Person:
    def fånga(self, Duck):
        Duck.walk()
        Duck.kvack()
        print("Du fånga djuret!")

anka = Duck()
kyckling = Chicken()
person = Person()

person.fånga(anka)
person.fånga(kyckling) #kyckling går ändå öven om def fånga specifierar en anka eftersom båda klasserna anka och kyckling delar minimum attributer eller metoder.

#klass typen kollas inte så länge attributerna/ metodrna är detsamma. 

