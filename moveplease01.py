#!/usr/bin/env python3

import shutil
import os


def main():
    os.chdir('/home/student/mycode/')
    
    # moves file. Will overwrite files at destination!
    shutil.move('raynor.obj', 'ceph_storage/')

    # gets new name for kerrigan.obj
    xname = input('What is the new name for the kerrigan.obj?')

    # renames kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()
