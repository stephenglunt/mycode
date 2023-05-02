#!/usr/bin/python3

import json

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galaxyguide.json", 'w') as zfile:
        json.dump(hitchhikers, zfile)


if __name__ == "__main__":
    main()
