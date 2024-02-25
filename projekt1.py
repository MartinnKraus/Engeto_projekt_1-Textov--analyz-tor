"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martin Kraus
email: martinnkraus@gmail.com
discord: martin_64789
"""

import sys

import task_template
from users import passwords

def has_numbers(inputString):
    """
    Test, zda má vstupní text nějaká čísla
    """
    return any(char.isdigit() for char in inputString)



username = input("Insert username: ")
password = input("Insert password: ")

if passwords[username] != password:
    #Ukončí program, pokud je uživatel neregistrovaný
    print("unregistered user, terminating the program..")
    sys.exit
else:
    #Uvítání a úvod
    print(
        "-" * 40,
        f"Welcome to the app, {username}",
        "We have 3 texts to be analyzed.",
        "-" * 40,
        sep="\n"
    )
#Pobídni uživatele k výběru textu a otestuj jeho vstup:
    cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
    if not cislo_textu.isnumeric():
        sys.exit("Input is not number, terminating the program..")
    elif int(cislo_textu) not in range(1,4):
        sys.exit("Input is not in valid range, terminating the program..")
    else:
        cislo_textu = int(cislo_textu)
    print("-" * 40 )
#Přiřaď text do proměnné a pročisti:
    text = task_template.TEXTS[cislo_textu - 1]
    text.strip()
    slova = text.split()
    slova_set = set(slova)
#Výpočty:
    pocet_slov = len(slova) # Celkový počet slov

    pocet_titlecase = len([slovo for slovo in slova if slovo.istitle()])    #Počet slov počínajících velkým písmenem

    pocet_uppercase = len([slovo for slovo in slova if slovo.isupper() and not has_numbers(slovo)])    #Počet slov psaných velkým písmem

    pocet_lowercase = len([slovo for slovo in slova if slovo.islower()])    #Počet slov psaných malým písmem

    pocet_numeric = len([slovo for slovo in slova if slovo.isnumeric()])

    soucet_cisel = sum(int(cislo) for cislo in slova if cislo.isnumeric())

#Knihovna s délkami slov:


print(pocet_slov, pocet_titlecase, pocet_uppercase, pocet_lowercase, pocet_numeric, soucet_cisel, sep=",")

