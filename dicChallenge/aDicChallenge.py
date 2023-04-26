#!/usr/bin/env python3

def main():

    luke_skywalker = {
    'Title': ['Jedi Knight', 'Jedi Master', 'Red Five', 'Rogue Leader'
              ],
    'Occupation': ['Apprentice', 'Moisture Farmer', 'Pilot', 'Jedi'],
    'Affiliation': [
        'Skywalker family',
        'Rebel Alliance',
        'Rogue Squadron',
        'Jedi',
        'New Republic',
        'New Jedi Order',
        'Resistance',
        'Galactic Alliance',
        'Jedi Council',
        ],
    'Family': ['Padm\xc3\xa9 Amidala (mother)',
               'Anakin Skywalker (father)', 'Leia Organa (twin sister)'
               , 'Owen Lars (paternal step-uncle)',
               'Beru Lars (paternal step-aunt)'],
    }

    # print(luke_skywalker.keys())
    keys = {}
    for i in range(len(list(luke_skywalker.keys()))):
        print(f"{i}: {list(luke_skywalker.keys())[i]}")
        keys[i] = list(luke_skywalker.keys())[i]

    choice = input("Select one of the keys listed: \n> ")

    print(luke_skywalker.get(choice, "Invalid Key"))


main()
