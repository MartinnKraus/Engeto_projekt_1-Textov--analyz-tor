"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martin Kraus
email: martinnkraus@gmail.com
discord: martin_64789
"""

import sys

import task_template    #Import knihovny s textem ze zadání
from users import passwords #Import knihovny s hesly

def has_numbers(inputString):
    """
    Test, zda má vstupní text nějaká čísla
    """
    return any(char.isdigit() for char in inputString)

def count_by_len(seznam, delka):
    """
    Spočítá počet výskytů slov dle zadané délky
    """
    return len([slovo for slovo in seznam if len(slovo) == delka])


username = input("Insert username: ") #zjisti username

if username not in passwords.keys():    #ověř, zda je uživatel registrovaný
    sys.exit("Unregistered user, terminating the program..")

password = input("Insert password: ") #zjisti heslo

if passwords[username] != password:
    #Ukončí program, pokud je uživatel neregistrovaný
    sys.exit("Wrong password, terminating the program..")
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
    slova = [slovo.strip(",.:;-") for slovo in text.split()]
    slova_set = set(slova)
#Výpočty:
    pocet_slov = len(slova) # Celkový počet slov

    pocet_titlecase = len([slovo for slovo in slova if slovo.istitle()])    #Počet slov počínajících velkým písmenem

    pocet_uppercase = len([slovo for slovo in slova if slovo.isupper() and not has_numbers(slovo)])    #Počet slov psaných velkým písmem

    pocet_lowercase = len([slovo for slovo in slova if slovo.islower()])    #Počet slov psaných malým písmem

    pocet_numeric = len([slovo for slovo in slova if slovo.isnumeric()])

    soucet_cisel = sum(int(cislo) for cislo in slova if cislo.isnumeric())

#Knihovna s délkami slov:
    max_delka = max(len(slovo) for slovo in slova)
    pocet_delek = {delka : count_by_len(slova, delka) for delka in range(1, max_delka + 1) if count_by_len(slova, delka) > 0}
    max_vyskytu = max(pocet_delek.values())
#Printy výsledků:
    print(f"There are {pocet_slov} words in the selected text.",
        f"There are {pocet_titlecase} titlecase words.",
        f"There are {pocet_uppercase} uppercase words.",
        f"There are {pocet_lowercase} lowercase words.",
        f"There are {pocet_numeric} numeric strings.",
        f"The sum of all the numbers {soucet_cisel}",
        sep="\n"
        )
#Vytiskni "graf" délek:
    print("-" * 40,
          "LEN|" + "OCCURENCES".center(max_vyskytu + 3) + "|NR.",
          "-" * 40,
          sep="\n"
          )
    for delka in pocet_delek:
        print(str(delka).rjust(3),
              "|",
              ("*" * pocet_delek[delka]).ljust(max_vyskytu + 3),
              "|",
              pocet_delek[delka],
              sep = ""
              )