import os 
import sys
from PIL import Image
import magic


# ter.exit()

def folder_paths(path):

    print('🧭  File Nav - Quarantine Ver 1.7: \n')
    entries = os.listdir(path)
    folders = [e for e in entries if os.path.isdir(os.path.join(path, e))]
    files = [e for e in entries if os.path.isfile(os.path.join(path, e))]

    print('📁  Folders:')
    for idx, folder in enumerate(folders):
        newdir_idx = idx+1
        print(f' {newdir_idx} {folder}')

    print('\n📄  Files: ')
    for idx, f in enumerate(files):
        newf_idx = idx+1
        print(f' f-{newf_idx} {f}') 
    
    return folders, files


def nav(base_path):
    current_path = base_path

    while True:

        print(f'Current path => {current_path}')
        folders, files = folder_paths(current_path)  
        print('\n-Type corresponding number to select folder.')
        print('-Type corresponding f-number to select file.')
        print('-Type ".." to go up a level.')
        print('-Type "exit" to... well exit.')

        choice = input(f'\n>> ').strip()

        if choice == "exit":
            os.system('cls')
            break

        elif choice == "..":
            if os.path.abspath(current_path) != os.path.abspath(base_path):
                current_path = os.path.dirname(current_path)
                os.system('cls')
            else:
                os.system('cls')
                print('🚫  Top directory reached!')
                
        elif choice.isdigit() and (int(choice)-1) < len(folders):
            new_folder = folders[(int(choice)-1)]
            current_path = os.path.join(current_path, new_folder)
            os.system('cls')

        elif choice[:2]=='f-':
            cnum = int(choice[2:None])
            if (int(cnum)-1) < len(files):
                fsize = os.path.getsize(os.path.join(current_path, files[cnum-1]))
                if fsize != 0:
                    try:
                        with open(os.path.join(current_path, files[cnum-1])) as file:
                            os.system('cls')
                            print("-"*65)
                            print(file.read())
                            print("-"*65)
                            print('\n-Type ".." to go back.')
                            input('>> ')
                            os.system('cls')
                    except UnicodeDecodeError:
                        im = Image.open(os.path.join(current_path, files[cnum-1]))
                        im.show()

                else:
                    os.system('cls')
                    print('The file which you requested does not contain any data!')
                    print('\n-Type ".." to go back.')
                    input('>> ')
                    os.system('cls')

        else:
            os.system('cls')
            print('❌  Input not accepted!')
    
print("="*70)
print('⚙️  FILE SETTINGS (permanent per session): ')
folderlim = input('-Folder (in Desktop) which this navigator should be limited to: ')
user = os.getlogin()
base_path = f'C:\\Users\\{user}\\Desktop\\{folderlim}'
if os.path.exists(base_path):
    os.system('cls')
    nav(base_path)
    
else:
    os.system('cls')
    print('This path does not exist!')