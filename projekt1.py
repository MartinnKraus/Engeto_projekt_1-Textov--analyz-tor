"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martin Kraus
email: martinnkraus@gmail.com
discord: martin_64789
"""

import task_template
import sys

#texty = task_template.TEXTS

#Hesla = {Uživatel : Hesla}
passwords = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

username = input("Zadej uživatelské jméno: ")
password = input("Zadej heslo: ")

if passwords[username] == password:
    print("Správné heslo, supr.")
    #Uvítání a úvod
    print(
        "-" * 40,
        f"Vítej v aplikaci {username}",
        "K dispozici pro analýzu jsou 3 texty",
        "-" * 40,
        sep="\n"
    )
    #Pobídni uživatele k výběru textu a otestuj jeho vstup
    cislo_textu = input("Zadej číslo textu mezi 1 a 3: ")
    if not cislo_textu.isnumeric():
        sys.exit("Vstup není číslo! Ukončuji program")
    elif int(cislo_textu) not in range(1,4):
        sys.exit("Vstup není v rozsahu 1-3. Ukončuji program")
    else:
        cislo_textu = int(cislo_textu)
    #Přiřaď text do proměnné a pročisti
    text = task_template.TEXTS[cislo_textu - 1]
    text.strip()
    print("-" * 40 )

    slova = text.split()
    slova_set = set(slova)


    print(slova)

else:
    print("Neregistrovaný uživatel, ukončuji program")



