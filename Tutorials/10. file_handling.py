import os
import shutil as shut
import sys as ter

ter.exit() #safeguard


#-FILE DETECTION-
path = "C:\\Users\\alexa\\Desktop\\test.txt"

if os.path.exists(path): #kollar om den specifierade "path" inom .exists() existerar inom datorn
    print("Den här filen existerar")
    if os.path.isfile(path): #isfile() kollar om "path" leder till en file, i det här fallet ja
        print("Detta är en fil")
    elif os.path.isdir(path): #isdir() kollar om "path" leder till ett directory eller folder i datorn, i det här fallet nej
        print("Detta är ett directory (folder)")
else:
    print("Den här filen existerar inte")






#-FILE READING- 
with open("C:\\Users\\alexa\\Desktop\\test.txt", encoding = "utf-8") as file: #om filen existerar inom samma folder som python filen behöver namnet bara specifieras, 
                                                                              # open() kommer också automatiskt stänga den öppnade filen.
                                                                              #Här måste encoding specifieras eftersom annars kommer åäö inte visas, 
                                                                              # encoding som tex utf-8 kan visa de flesta speciella bokstäver som åäö!
    print(file.read()) #här öppnar vi filen och printar det inom python filen

print(file.closed) #printar True/False baserat på om filen är stängd eller inte

#kan också skrivas inom ett try-except block
try:
    with open("C:\\Users\\alexa\\Desktop\\test.txt", encoding = "utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Fil inte hittad")







#-WRITING FILES-
text = '''Hej hej jag heter alex, bolibompa mitt program ellr nåt sånt hajahajajhajaahajhajhhajhaj''' #om texten ändras här efter filen blev skapad kommer den filens text ändras till den nya 
with open(f"C:\\Users\\alexa\\Desktop\\nyTEXT.txt", "w") as test: #andra argumentet som open() tar är "w" eller "r" eller "a", där w står för write och r står för read och a står för append
    test.write(text)

text = '''Hej hej jag heter alex, bolibompa mitt program ellr nåt sånt hajahajajhajaahajhajhhajhaj'''  #denna text kommer läggas till, inte ersätta som koden over då den var i write mode "w"
with open(f"C:\\Users\\alexa\\Desktop\\nyTEXT.txt", "a") as test: #här är open() i append mode alltså att text läggs till den redan befintliga text i en skapan .txt file.
    test.write(text)








#-COPY A FILE-
#copyfile() - kopierar innehållet av en file
#copy() - copyfile() + permission mode + destination kan vara ett directory 
#copy2() - copy() + kopierar metadatan (specifikationer för tiden då filen skapats och senaste gången den modifierades)

shut.copyfile("C:\\Users\\alexa\\Desktop\\test.txt" , "C:\\Users\\alexa\\Desktop\\Copy_test.txt") #tar två argument källa och destination







#-MOVING FILES-
source = "C:\\Users\\alexa\\Desktop\\test.txt" #källan, kan också flytta directories (folders)
destination = "C:\\Users\\alexa\\Downloads\\test.txt" #vart filen ska flyttas
try: #bäst att ha try-except om det sker en error
    if os.path.exists(destination): #kontrollerar om destinationen finns så att den inte flyttar en fil till ett folder där den redan finns
        print("There is already a file there")
    else:
        os.replace(source, destination) #om filen inte redan finns kan den flyttas till destinationen med .replace() där argumenten är (källa, destination)
        print(source + " was moved")
except FileNotFoundError: #om sker som detta printas ett meddelande
    print(f"File in '{source}' was not found")








#-DELETING FILES-
path = "C:\\Users\\alexa\\Desktop\\delete me python folder\\delete me python.txt"
pathf = "C:\\Users\\alexa\\Desktop\\delete me python folder"
pathfempty = "C:\\Users\\alexa\\Desktop\\delete me python empty folder"
try:
    os.remove(path) #delete file
    os.rmdir(pathfempty) #delete empty directory 
    shut.rmtree(pathf) #delete directory containing files from shutil module
except FileNotFoundError: #filen var inte hittad
    print("That file was not found")
except PermissionError: #du är inte tillåten att ta bort den specifierade filen
    print("You do not have permission to delete that")
except OSError: #om en folder inte är tom och man använder bara "os.rmdir()"" kommer denna errorn behöver speciell funktion för att ta bort icke toma folders alltså "shutil.rmtree()""
    print("You cannot delete that using that function")
else:
    print(f"{path} was deleted")