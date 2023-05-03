#!/usr/bin/python3

# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    pprint.pprint(got_dj)

    ## display only the keys within
    ## the dictionary by using dict.keys()
    ## great for seeing what keys are available for lookup
    pprint.pprint(got_dj.keys())


if __name__ == "__main__":
    main()
