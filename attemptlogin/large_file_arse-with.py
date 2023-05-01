#!/usr/bin/env python3

from re import search

def main():
    # parse keystone.common.wsgi and return # of failed login attempts w/ip
    loginfail = 0 #counter for fials

    failedIps = {}

    # open filf or reading
    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r") as keystone_file:

        for line in keystone_file:

            if "- - - - -] Authorization failed" in line:
                loginfail += 1
                ip_address = search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line).group()
                if ip_address in failedIps:
                    failedIps[ip_address] += 1
                else:
                    failedIps[ip_address] = 1


    print("The number of failed log in attmepts is", loginfail)
    for key, value in failedIps.items():
        print(f"There were {value} failed log in attempts from {key}")

if __name__ == "__main__":
    main()
