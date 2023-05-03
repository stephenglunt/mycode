#!/usr/bin/env python3

import requests

def printCategories():
    print("Any Category: leave blank")
    print("General Knowledge: 9")
    print("Entertainment: Books: 10")
    print("Entertainment: Film: 11")
    print("Entertainment: Music: 12")
    print("Entertainment: Musicals & Theatres: 13")
    print("Entertainment: Television: 14")
    print("Entertainment: Video Games: 15")
    print("Entertainment: Board Games: 16")
    print("Science & Nature: 17")
    print("Science: Computers: 18")
    print("Science: Mathematics: 19")
    print("Mythology: 20")
    print("Sports: 21")
    print("Geography: 22")
    print("History: 23")
    print("Politics: 24")
    print("Art: 25")
    print("Celebrities: 26")
    print("Animals: 27")
    print("Vehicles: 28")
    print("Entertainment: Comics: 29")
    print("Science: Gadgets: 30")
    print("Entertainment: Japanese Anime & Manga: 31")
    print("Entertainment: Cartoon & Animations: 32")

def main():
    baseUrl = "https://opentdb.com/api.php?"

    numQuestions = "amount=" + input("How many questions do you want?\n>")

    printCategories()
    category = input("What category (9 - 32 or blank) do you want?\n>")
    if category:
        category = "&category=" + category

    difficulty = input("Easy, Medium, or Hard?\n>").lower()
    if difficulty:
        difficulty = "&difficulty=" + difficulty

    qType = input("multiple or boolean?\n>")
    if qType:
        qType = '&type=' + qType

    print(f"{baseUrl}{numQuestions}{category}{difficulty}{qType}")

if __name__ == "__main__":
    main()
