#!/usr/bin/env python3

import json

fileName = "zodiac.json" #input("file name:\n>")

with open(fileName, 'r') as file:
    data = json.load(file)


usr_name = input("Please enter your name:\n>").title()
usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))

date = str(usr_date % 12)

print(f"{usr_name}{data[date]}")
