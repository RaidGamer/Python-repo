from sys import argv,exit 
#sys.argv är en lista som skapas innan själva programmet startas, alltså tar den flera argument som tex "python commandline_args.py Alexander Olivius" här tar den tre argument,
# namnet på filen, mitt förnamn och efternamn. Alla dessa kommer sedan kopieras som element till en list som vi kan manipulera och därmed göra koden enklare att använda som developer
#istället för att behöva starta programmet, vänta på user input box, och sedan skriva in input. Istället kan vi skriva våran input redan från början i commandlinen!

#1:a exempel
if len(argv) < 2: 
    exit("Too few arguments")
elif len(argv) > 2:
    exit("Too many arguments")

print("hello my name is " + argv[1])



#2:a exempel
if len(argv) < 2:
    exit("Too few arguments")

for arg in argv[1:-1]:
    print("hello, my name is", arg)