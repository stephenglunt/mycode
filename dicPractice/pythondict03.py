#!/usr/bin/env python3

"""Understanding dictionaries """

def main():
    """runtime function"""

    # create a dictionary w/4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    print(switch)

    print(type(switch))

    print(switch.get("lynx"))

    print("Forth test - .keys()")
    print(switch.keys())

    print("Fifth test - .values()")
    print(switch.values())


if __name__ == "__main__":
    main()
