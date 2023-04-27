#!/usr/bin/env python3

import shutil
import os

def main():

    # Sets the execution directory
    os.chdir("/home/student/mycode/")

    # this copies the first file to the location in the second argument
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # this deletes the old copy of the backup
    os.system("rm -rf /home/student/mycode/5g_reasearch_backup/")
    # this will copy the entire directory structure of 5g_research/
    shutil.copytree("5g_research/", "5g_reasearch_backup/")


if __name__ == "__main__":
    main()
