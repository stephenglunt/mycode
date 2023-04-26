#!/usr/bin/env python3

def main():
    #ipchk = "192.168.0.1"
    ipchk = input("Apply an IP address:\n> ")

    

    if ipchk:
        print("Looks like the IP address was set: " + ipchk)
    else: 
        print("You did not provide input.")

if __name__ == "__main__":
    main()
