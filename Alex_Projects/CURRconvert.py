import requests 
import os

#TODO catch user error!!!!!!

def convert():
    respo = input("Convert currency (before = after): ").strip().upper()
    hitta = respo.find("=")
    if hitta == -1:
        print("Invalid convertion")
    else:
        None
    before = respo[ :hitta].strip()
    after = respo[hitta+1: ].strip()
    munch = input(f"How much in {before} shall be converted?: ")
    parameter = {
        "from" : before,
        "to" : after,
        "amount" : munch
    }
    return parameter, before, after, munch

def listCURR():
    response = requests.get("https://api.frankfurter.dev/v1/currencies")
    data = response.json()
    for key,value in data.items():
        print(f"{key} -> {value}")

def show_prochange():
    print("Date format is YYYY-MM-DD: ")
    bef = input("Before -> ").upper()
    aft = input("After -> ").upper()
    cur = input("What currency?: ").upper()
    base = "USD" if cur != "USD" else "EUR"

    per = {
            "base" : base,
            "amount" : 1
        }
    
    date_before = requests.get(f"https://api.frankfurter.dev/v1/{bef}", params = per).json()
    rate_before = date_before["rates"][cur]
    date_after = requests.get(f"https://api.frankfurter.dev/v1/{aft}", params = per).json()
    rate_after = date_after["rates"][cur]
    procent_change = ((rate_after-rate_before)/rate_before)*100
    return procent_change, bef, aft, cur, rate_before, rate_after

def get_exchangerates(base, after):
    fun = {
        "base" : base,
        "amount" : 1
    }
    response = requests.get("https://api.frankfurter.app/latest", params= fun)
    data = response.json()
    rate = data["rates"][after]
    return rate


def main():
    while True:
        print("-"*37)
        print("₽ ₹ ¥ £ $ € CURRENCY CALC € $ £ ¥ ₹ ₽")
        print("-"*37)
        print("MENU: ")
        print("1 -> Currency convertion")
        print("2 -> Currency value change (%)")
        print("3 -> Exit\n")
        inp = int(input("↳ choose option: "))
        if inp == 1:
            while True:
                os.system("cls")
                print("="*30)
                print("CURRENCY CONVERTER: \n")
                print("available currencies: ")
                listCURR()
                print(" ")
                par, bef, aft, sal = convert()
                response = requests.get("https://api.frankfurter.app/latest", params = par)
                data = response.json()
                print(f"{float(sal):.2f} in {bef} ➜  {data["rates"][aft]} in {aft} (exchange rate: {get_exchangerates(bef, aft)})")
                yn = input("Return to menu? Y/N: ").upper()
                if yn == "N":
                    os.system("cls")
                else:
                    os.system("cls")
                    break
                
        elif inp == 2:
            while True:
                os.system("cls")
                print("="*30)
                print("CURRENCY VALUE CHANGE (%): \n")
                print("available currencies: ")
                listCURR()
                print(" ")

                proch, datA, datB, valuta, ratA, ratB = show_prochange()
                os.system("cls")
                print(f"\nValue Change info ({valuta}): \n")
                ref = len("|  DATE   |   2006-12-18  |   2025-05-01  |")
                inw = int((ref-10)/2)
                bar = "|"
                tableDAT = "|  DATE   |"
                infoDAT_A = f" {datA.center(inw, ' ')} "
                infoDAT_B = f" {datB.center(inw, ' ')} "
                tableRAT = "|  RATE   |"
                infoRAT_A = f" {str(ratA).center(inw, ' ')} "
                infoRAT_B = f" {str(ratB).center(inw, ' ')} "
                tablePRO = "| %CHANGE |"
                infoPROCH = f" {f'{proch:+.2f}'.center(ref - 8)} "
                upperL = lowerL = "-"*(ref+6)

                print(11*" "+"before".center(inw, " ")+"after".center(inw+7, " "))
                print(upperL)
                print(tableDAT+infoDAT_A+bar+infoDAT_B+bar, end="")
                print("\n"+tableRAT+infoRAT_A+bar+infoRAT_B+bar, end="")
                print("\n"+tablePRO+infoPROCH+bar, end="")
                print("\n"+lowerL)

                yn = input("Return to menu? Y/N: ").upper()
                if yn == "N":
                    os.system("cls")
                else:
                    os.system("cls")
                    break

        elif inp == 3:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid input\n")
            
main()

