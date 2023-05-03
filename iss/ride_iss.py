#!/usr/binpython3

"""Astros on the ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    #call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()

    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    print(type(helmet))

    print(type(helmetson))

    print(helmetson["people"])

    print(helmetson["people"][0])

    print(helmetson["people"][1])

    # list the LAST astro in the list
    print(helmetson["people"][-1])

    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(astro)

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])

if __name__ == "__main__":
    main()
