#!/usr/bin/env python3

def main():
    # create the string hostname
    hostname = input("What value should we set for the hostname?")
    # test logic with the `if` statement
    # what to do if this statement is found to be true
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    print("Exiting the script")

if __name__ == "__main__":
    main()
