#!/usr/bin/python3

# documentation for this API is at
# https://anapioficeandfire.com/Documentation


import requests

asoif_characters = "https://anapioficeandfire.com/api/characters/"



condition = True


names = []

url = asoif_characters
for i in range(1996,2139):
 #   print(i)
#    url = f"{url}{i}"
    
#    print(url)
    response = requests.get(f"{url}{i}")
#    print(response)
    data = response.json()
#    print(data)
    if str(response) == "<Response [404]>":
        print(response)
    else:
#        for character in data:
        if data["name"]:
            names.append(data["name"])
        elif data['aliases']:
            names.append(data['aliases'])
        else:
            names.append(data['url'])
    with open('names2.txt', 'a') as file:
        file.write(str(names[i-1996]) + '\n')
    

with open('names.txt', 'w') as output:
    for element in names:
        output.write(str(element) + '\n')
