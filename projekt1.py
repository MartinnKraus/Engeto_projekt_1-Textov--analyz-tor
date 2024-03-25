"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martin Kraus
email: martinnkraus@gmail.com
discord: martin_64789
"""

import sys

from task_template import TEXTS   #Import knihovny s textem ze zadání
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
password = input("Insert password: ") #zjisti heslo
if username not in passwords.keys():    #ověř, zda je uživatel registrovaný
    sys.exit("Unregistered user, terminating the program..")


elif passwords[username] != password:
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
    text = TEXTS[cislo_textu - 1]
    slova = [slovo.strip(",.:;-") for slovo in text.split()]
    slova_set = set(slova)
#Statistiky:
    #new - ulož do knihovny:
    statistiky = {}
    statistiky["pocet_slov"] = len(slova)
    for slovo in slova:
        if slovo.istitle():
            statistiky["pocet_titlecase"] = statistiky.setdefault("pocet_titlecase", 0) + 1
        if slovo.isupper() and not has_numbers(slovo):
            statistiky["pocet_uppercase"] = statistiky.setdefault("pocet_uppercase", 0) + 1
        if slovo.islower():
            statistiky["pocet_lowercase"] = statistiky.setdefault("pocet_lowercase", 0) + 1
        if slovo.isnumeric():
            statistiky["pocet_numeric"] = statistiky.setdefault("pocet_numeric", 0) + 1
        if slovo.isnumeric():
            statistiky["soucet_cisel"] = statistiky.setdefault("soucet_cisel", 0) + int(slovo)

#Knihovna s délkami slov:
    max_delka = max(len(slovo) for slovo in slova)
    pocet_delek = {delka: count_by_len(slova, delka) for delka in range(1, max_delka + 1) if count_by_len(slova, delka) > 0}
    max_vyskytu = max(pocet_delek.values())
#Printy výsledků:
    print(f"There are {statistiky.get("pocet_slov")} words in the selected text.",
        f"There are {statistiky.get("pocet_titlecase")} titlecase words.",
        f"There are {statistiky.get("pocet_uppercase")} uppercase words.",
        f"There are {statistiky.get("pocet_lowercase")} lowercase words.",
        f"There are {statistiky.get("pocet_numeric")} numeric strings.",
        f"The sum of all the numbers {statistiky.get("soucet_cisel")}",
        sep="\n"
        )
#Vytiskni "graf" délek:
    print("-" * 40,
          "LEN|" + "OCCURENCES".center(max_vyskytu + 3) + "|NR.",
          "-" * 40,
          sep="\n"
          )
    for delka in pocet_delek:
        print(str(delka).rjust(3), "|", ("*" * pocet_delek[delka]).ljust(max_vyskytu + 3),
              "|", pocet_delek[delka], sep = ""
              )