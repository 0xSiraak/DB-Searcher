import os
import pyfiglet
from colorama import Fore, Back, Style

r = pyfiglet.figlet_format("DB Searcher")
print(Fore.CYAN + r)
print(Fore.CYAN + "Developped by 0xSiraak on GitHub")

user = input(Fore.GREEN + "\n[+] - Username, Email, IP, UUID : ")

print(Fore.GREEN + "[+] - Results : \n")
os.system("cat /databases/* | grep " + user)
print(Fore.CYAN + "[+] - Finished research...")
