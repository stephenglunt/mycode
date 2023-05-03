#!/usr/bin/python3

import urllib.request
import json


NSAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Define creds
    with open('/home/student/nasa.creds') as mycreds:
        nsacreds = mycreds.read()

    nsacreds = "api_key=" + nsacreds.strip('\n')

    # Call the webservice with out key
    apodurlobj = urllib.request.urlopen(NSAAPI + nsacreds)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data struct
    apod = json.loads(apodread.decode("utf-8"))

    ## display our data
    print('\n\nConverted Python data')
    print(apod)

    print()

    print(apod['title'] + '\n')

    print(apod['date'] + '\n')

    print(apod['explanation'] + '\n')

    print(apod['url'])


if __name__ == "__main__":
    main()

