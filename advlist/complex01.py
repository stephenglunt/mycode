#!/usr/bin/env python3

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # displaylist1
    print(list1)

    # display list1[1]
    print(list1[1])

    list2 = ["juniper"]

    list1.extend(list2)

    #display list1, which now contains juniper
    print(list1)
    
    #create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #use the append operation to append list1 by list3
    list1.append(list3)

    print(list1)

    # display the list of IP addresses
    print(list1[4])

    # display the first item in the list - first IP address
    print(list1[4][0])

main()
