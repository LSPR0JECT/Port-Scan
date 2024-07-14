import os
import socket
import threading
import time
import sys
from colorama import init, Fore

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_port(ip, port):
    try:
       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
        s.settimeout(0.5)
       
        result = s.connect_ex((ip, port))
        
        if result == 0:
            service = socket.getservbyport(port)
            print(f"{Fore.GREEN}[+] Port {port} est ouvert - Service : {service}")
        s.close()
    
    except Exception as e:
        pass

def display_menu():
    pseudo = f"{Fore.MAGENTA}Lean"
    print(ascii_art)
    print(pseudo.center(60))
    print(f"{Fore.YELLOW}\nBienvenue dans le Scanner de Ports\n")
    print(f"{Fore.GREEN}1. Commencer le scan")
    print(f"{Fore.RED}2. Quitter")

def main():
    clear_console()
    while True:
        display_menu()
        choice = input(f"{Fore.CYAN}Entrez votre choix : ")
        
        if choice == '1':
            ip = input("Entrez l'adresse IP à scanner : ")
            print(f"{Fore.BLUE}Scan des ports sur {ip}...\n")
            
            threads = []
           
            for port in range(1, 1025):
                thread = threading.Thread(target=scan_port, args=(ip, port))
                thread.start()
                threads.append(thread)
            
            for thread in threads:
                thread.join()
                
            print(f"{Fore.YELLOW}Scan terminé.")
        
        elif choice == '2':
            print(f"{Fore.RED}Au revoir!")
            break
        
        else:
            print(f"{Fore.RED}Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    ascii_art = f"""
{Fore.MAGENTA}
              ('-.      ('-.          .-') _
            _(  OO)    ( OO ).-.     ( OO ) )
 ,--.      (,------.   / . --. / ,--./ ,--,'
 |  |.-')   |  .---'   | \-.  \  |   \ |  |\\
 |  | OO )  |  |     .-'-'  |  | |    \|  | )
 |  |`-' | (|  '--.   \| |_.'  | |  .     |/
(|  '---.'  |  .--'    |  .-.  | |  |\    |
 |      |   |  `---.   |  | |  | |  | \   |
 `------'   `------'   `--' `--' `--'  `--'
"""
    main()
