# namn = input("Vad heter du min vänn?: ")

# CleanNamn = namn.strip().title()

# mellansteg = CleanNamn.find(" ")

# if CleanNamn.find(" ") != -1:
#     first = CleanNamn[0:mellansteg]
#     last = CleanNamn[mellansteg+1:]
#     print(f"Hej {first} trevligt att träffas!\nDitt efternamn är {last}, eller hur?")
# else:
#     print("Du glömde antingen ditt för- eller efternamn, skriv igen.")


while True:
    namn = input("Vad heter du min vän?: ")

    CleanNamn = namn.strip().title()

    mellansteg = CleanNamn.find(" ")

    if mellansteg != -1:
        first = CleanNamn[:mellansteg]
        last = CleanNamn[mellansteg+1:]
        print(f"Hej {first} trevligt att träffas!\nDitt efternamn är {last}, eller hur?")
        break
    else:
        print("Fullt namn krävs")