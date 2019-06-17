#!/usr/bin/env python

import os
import subprocess
import glob

#The first step is to cache the files you plan on converiting/skimming and then linking them.
#I don't really understand this step

file = glob.glob('/cache/mss/clas/g11a/production/pass0/v0/data/run*')

command = 'ln -s  '

for f in file:
    cmd_exec = command + f 
    print(cmd_exec)
    os.system(cmd_exec)


