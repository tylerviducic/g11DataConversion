#!/usr/bin/env python

import os
import glob

#conver the bos file to hipo. duh.

file = glob.glob('run_43*')

command = '/home/gavalian/coatjava/bin/bos2hipo -lz4'

for f in file:
    cmd_exec = command + " " + f +".hipo " + f
    print(cmd_exec)
    os.system(cmd_exec)