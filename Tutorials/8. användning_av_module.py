import Tutorials.modules.min_module as m #gav våran module en temporär alias som bara m, behöver då inte skriva "meddelanden" varje gång vid användning
#"Tutorials.modules.min_module" är ett sätt att bara specifiera modulen man använder den kan skrivas utan dock så länge man inte har flera med samma namn, dumt att göra så dock
m.Goodbye() #man kan använda ens egna module som alla andra redan tidigare inbygda modules => namnet_på_module.namnet_på_funktion()

# Goodbye() #om man har importerat specifika funktioner från en module kan man bara skriva namnet på funktionen och skippa namnet på modulen
# from min_module import hello_world, Goodbye #kan också importera specifika funktioner så här då behövs m. där nedanför inte skrivas

#lista på alla inbyggda modules som kommer med python gratis
help("modules")