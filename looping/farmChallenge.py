#!/usr/bin/env python3


def main():
#    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
 #        {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
  #       {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


    animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]


    print("All the animals from the NE Farm:")
    for animal in farms[0]["agriculture"]:
        print(animal)

    print("Choose a farm:")
    for farm in farms:
        print(farm["name"])

    choice = input("> ")
    for farm in farms:
        if farm["name"] == choice:
            print(f"All the plants and  animals from the {choice}")
            for animal in farm["agriculture"]:
                print (animal)

    print("Choose a farm:")
    for farm in farms:
        print(farm["name"])

    choice = input("> ")
    for farm in farms:
        if farm["name"] == choice:
            print(f"All the animals from the {choice}")
            for animal in farm["agriculture"]:
                if animal in animals:
                    print (animal)


if __name__ == "__main__":
    main()
