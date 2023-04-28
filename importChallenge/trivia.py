#!/usr/bin/env python3

import html
import random

def main():

    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

    print(trivia["question"])

    answers = trivia["incorrect_answers"]
    answers.append(trivia["correct_answer"])
    random.shuffle(answers)
    
    key = {}
    index = "A"
    for answer in answers:
        print(f"{index}. {html.unescape(answer)}")
        key[index.lower()] = answer
        index = chr(ord(index) + 1)

    guess = input("Guess your answer:\n>")
    if key[guess.lower()] == trivia["correct_answer"]:
        print("Correct!")
    else:
        print("Incorrect.")

if __name__ == "__main__":
    main()

