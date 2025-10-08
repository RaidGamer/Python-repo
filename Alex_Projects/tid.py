def main():
    time()

def time():
    from time import sleep as sle
    from os import system as sys
    from datetime import datetime
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Din nuvarande tid är: {current_time} ")
        sle(1)
        sys("cls")



if __name__ == "__main__":
    main()