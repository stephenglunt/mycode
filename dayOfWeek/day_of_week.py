#!/usr/bin/env python3

"""This function will ask the user's name and what day of the week it is. Then it will print out a greeting."""

def main():
    user = input("What is your name? ")
    day_of_week = input("What day of the week is it? ")

    user = user.strip()
    day_of_week = day_of_week.strip()

    print(f'Hello, {user}! Happy {day_of_week}!')

main()
