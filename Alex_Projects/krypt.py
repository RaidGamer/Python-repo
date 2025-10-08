from sys import exit 
from os import system as s
import random as rand
import os
#input
def main():
    while True:
        print("-"*50)
        print("Krypt.py => your own en- to decrypter")
        print("-"*50)
        print("1: Encrypt")
        print("2: Decrypt")
        print("3: Exit")
        try:
            ch = int(input("\nChoose option => "))
            s("cls")
            if ch == 3: 
                exit()
            elif ch == 2:
                cypher = input("Input your cyphertext for decryption => ")
                nyckel = input("Input your priv-key for decryption => ")
                seednyck = input("Input your seed-key for decryption => ")
                if nyckel.isdigit() and seednyck.isdigit():
                    deplain = dekrypt(cypher, nyckel, seednyck)
                    print(f"Decryption of >{cypher}< returned >{deplain}<")
                    input("\nPress enter to go back...")
                    s("cls")
                else:
                    s("cls")
                    print("The privatekey and seedkey contain only numbers!")
            elif ch == 1:
                plain = input("Input your plaintext for encryption => ")
                nyck, unplain, sädnyck = krypt(plain)
                print(f"Decryption of >{plain}< returned >{unplain}< decrypt key is {nyck} and seedkey is {sädnyck}")
                filesavechoice = input("Do you want to save the encryption info to a file on your desktop? Y/N => ").upper()
                if filesavechoice == "Y":
                    user = os.getlogin()
                    with open(f"C:\\Users\\{user}\\Desktop\\Encryption_details.txt", "w") as kryptfile:
                        kryptfile.write(f"Cyphertext: {unplain}\nPriv-key: {nyck}\nSeed-key: {sädnyck}")
                    print("Encryption info stored on device")
                else:
                    print("Encryption info not stored on device")

                input("\nPress enter to go back...")
                s("cls")
            else:
                s("cls")
                print("Not a valid argument!")
        except ValueError:
            s("cls")
            print("Not a valid argument!")

#encrypt func
def krypt(plaintext):
    seedkey = rand.randint(1,50000)
    rng = rand.Random(seedkey)
    charl = list("1234567890+qwertyuiopå¨asdfghjklöä'zxcvbnm,.- !#¤%&/()=?`QWERTYUIOPÅ^ASDFGHJKLÖÄ*ZXCVBNM;:_@£$€{[]}\\~|")
    rng.shuffle(charl)
    pre_inp = list(plaintext)
    pos_inp = []
    pre_indxc = []
    post_indxc = []
    privkey = rand.randint(5, 500)

    #tar plaintext "pre_inp" och översätter den till index positioner hos vår cyphertabell "charl", index pos. sätt i listan pre_indxc
    for i in pre_inp:
        if i in charl:
            pre_indxc.append(charl.index(i))
        else: 
            print(f"Character '{i}' not found! Encryption cancelled.")
            return None, None, None

    #tar varje element eller charl index positioner från pre_indxc och skiftar det ett antal positiva positioner
    for i in pre_indxc:
        skift = i + privkey
        post_indxc.append(skift%len(charl))

    #tar de nya positionerna efter skiftet och översätter det till cyphertext mha charl
    for i in post_indxc:
        pos_inp.append(charl[int(i)])
    
    finkrypt = "".join(pos_inp)

    # print(f"[DEBUG] ursprungs encrypt-indxlista {pre_indxc}")
    # print(f"[DEBUG] efter shuffle encrypt-indxlista {post_indxc}")

    return privkey, finkrypt, seedkey
   

def dekrypt(encrtxt, privkey, seedkey):
    rng = rand.Random(int(seedkey))
    charl = list("1234567890+qwertyuiopå¨asdfghjklöä'zxcvbnm,.- !#¤%&/()=?`QWERTYUIOPÅ^ASDFGHJKLÖÄ*ZXCVBNM;:_@£$€{[]}\\~|")
    rng.shuffle(charl)
    pre_enli = list(encrtxt)
    pre_indxec = []
    post_indxec = []
    pos_enli = []
    for i in pre_enli:
        if i in charl:
            pre_indxec.append(charl.index(i))
        else: 
            print(f"Character '{i}' not found! Decryption cancelled.")
            return None

    for i in pre_indxec:
        skift = int(i) - int(privkey)
        post_indxec.append(skift%len(charl))
    
    for i in post_indxec:
        pos_enli.append(charl[i])

    findekrypt = "".join(pos_enli)

    # print(f"[DEBUG] efter unshuffling decrypt-indxlista {post_indxec}")
    
    return findekrypt


if __name__ == "__main__":
    main()

#.LoB