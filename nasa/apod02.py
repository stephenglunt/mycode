#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def returncreds():
    with open('/home/student/nasa.creds', 'r') as mycreds:
        nasacreds = mycreds.read()

    nasacreds = 'api_key=' + nasacreds.strip('\n')
    print(nasacreds)
    return nasacreds

def main():
    nasacreds = returncreds()

    apodresp = requests.get(NASAAPI + nasacreds)

    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
