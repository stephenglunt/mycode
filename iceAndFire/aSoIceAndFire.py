#!/usr/bin/python3

# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import json
import requests

asoif_characters = "https://anapioficeandfire.com/api/characters?"

page = input("Enter start page:\n>")

pageSize = input("Enter page size:\n>")

asoif_characters += f"page={page}&pageSize={pageSize}"

headers = {'last': { 'url': 'text/html'} }

condition = True

#response = requests.get(asoif_characters)
#headers = response.links
#response = response.json()

names = []

url = asoif_characters
while condition:
    response = requests.get(url)
    headers = response.links
    data = response.json()
    for character in data:
        if character["name"]:
            names.append(character["name"])
        elif character['aliases']:
            names.append(character['aliases'])
        else:
            names.append(character['url'])
    condition = url != headers['last']['url']
    if condition:
        url = headers['next']['url']

with open('test.txt', 'w') as output:
    for element in names:
        output.write(str(element) + '\n')
print(headers)
print(headers['last']['url'])

#for i in range(len(names)):
 #   print(i, names[i])
 
