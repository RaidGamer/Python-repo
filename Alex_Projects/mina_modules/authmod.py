"""
auth_module.py - A simple profile-based login system using JSON files.

Functions:
- login(path): Prompts user to log in using stored credentials.
- create_prof(folder, name): Creates a new login profile.
- authenticate(basepath): Manages full login/auth logic.
"""

import os
from sys import argv, exit
import json
import datetime as dt


def login(password_path : str):
    try:
        with open(password_path, encoding="utf-8") as jf:
            contentjson = json.load(jf)

        json_username = contentjson.get("username")
        json_password = contentjson.get("password")
        json_profile = contentjson.get("profile")

    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Failed to load profile: {e}\n")
        return False
    n=10
    current_time = dt.time()
    while True:
        
        print(f"Login to profile '{json_profile}': ")
        input_username = input("Username: ")
        input_password = input("Password: ")

        if input_username == json_username and input_password == json_password:
            os.system("cls" if os.name == "nt" else "clear")
            print("Login successsfull!\n")
            return True
            
        elif n > 0:
            n -= 1
            os.system("cls" if os.name == "nt" else "clear")
            print("Login unsuccessfull, try again!\n")

        else:
            pass 
            #Ge ett straff av ngra minuters väntetid som inte tillåter inloggning under den tiden. 

def _get_valid_cred(filename):
    while True:
        print(f"No profile found for current run script/file, create a new profile for {filename}")
        print("Caution! Do NOT change the current run script/file name or risk losing login info!\n")
        print("Create profile:")
        username = input("New username: ")
        password = input("New password: ")
        if not 0 < len(username) < 21:
            os.system("cls" if os.name == "nt" else "clear")
            print("Caution: usernames must be between 1 and 20 characters!")
            print("="*50)
        elif not 51 > len(password) > 4:
            os.system("cls" if os.name == "nt" else "clear")
            print("Caution: passwords must be between 5 and 50 characters!")
            print("="*50)
        else:
            return username, password

def create_prof(folder_path : str, filename : str):
    os.makedirs(folder_path, exist_ok=True)
    while True:

        username , password = _get_valid_cred(filename)

        saveYN = input("\nDo you want to save this profile? Y/N: ").upper().strip()
        if saveYN == "Y":
            data = {
                "profile" : filename,
                "username" : username,
                "password" : password,
            }

            filepath_json = os.path.join(folder_path, f"prof_{filename}.json")

            try:
                with open(filepath_json, "w", encoding="utf-8") as jfile:
                    json.dump(data, jfile, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Profile was successfully saved!\n")
                return data
            
            except IOError as e:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Error writing to file: {e}\n")

            except json.JSONDecodeError as e:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Error encoding JSON: {e}\n")

        else:
            if input(f"\nProfile was not saved! Try again? Y/N: ").strip().upper() != "Y":
                exit()
            else:
                os.system("cls" if os.name == "nt" else "clear")

        

def authenticate(basepath):

    basepath_pr = os.path.join(basepath, "password_registry")

    if "Desktop" not in basepath_pr:
        print("For safety reasons, do you want to continue with this filepath as it is not within the desktop?")
        safe_choice = input("Y for Yes and N for No, Y/N: ").strip().upper()
        if safe_choice == "N":
            exit()

    current_filename = os.path.splitext(os.path.basename(os.path.abspath(argv[0])))[0]
    password_profile = os.path.join(basepath_pr, current_filename)
    password_json = os.path.join(password_profile, f"prof_{current_filename}.json")

    if not os.path.exists(basepath_pr):
        os.makedirs(basepath_pr)

    if not os.path.exists(password_profile):
        profile = create_prof(password_profile, current_filename)
        return profile
    else:
        while True:
            success = login(password_json)
            if success:
                with open(password_json, encoding="utf-8") as jf:
                    return json.load(jf)

            

