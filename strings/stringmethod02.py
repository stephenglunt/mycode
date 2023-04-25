#!/usr/bin/env python3

"""Alta3 Research"""

def main():
    """ Run-time code """

    #create a small string
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(' ') # this returns a list
    print(newlist)

    # create a list of strings
    myIpList = ["192", '168', '0', '12']

    singleIp = ".".join(myIpList)

    print(singleIp)

main()
