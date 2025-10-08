import mina_modules.authmod as auth
import os
user = os.getlogin()
basepath = f"C:\\Users\\{user}\\Desktop"
auth.authenticate(basepath) 

print("yes you got to the core of the program congrats you dik'ead")
