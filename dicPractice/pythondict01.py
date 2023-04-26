#!/usr/bin/env python3

def main():
    """runtime function"""

    ## create a dictionary w/4 key: value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    # display the entire dictionary
    print(switch)

    # proove that switch is a dictionary
    print(type(switch))

    # display parts of the dictionary

    print(switch["hostname"])
    print(switch["ip"])

    # request a 'fake' key
    print("First test - .get()")
    print(switch.get("lynx")) 

    print("Second test - .get()")

    print(switch.get("lynx", "The key is in another castle!".upper()))

    print("Third test - .get()")
    print(switch.get("version"))

# call main
if __name__ == "__main__":
    main()
