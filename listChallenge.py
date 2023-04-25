#!/usr/bin/env python3

import random

def main():
    # this is a wordbank
    wordbank= ["indentation", "spaces"]

    wordbank.append(4)

    # list of TLG students
    tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]

    num = int(input("Give me a number between 0 and 11:\n> "))

    student_name = tlgstudents[num]

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    
    num = random.randint(0, 11)
    student_name = tlgstudents[num]

    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()
