#!/usr/bin/env python

import os
import glob

#merge all the files for each run into one file for the run

file = glob.glob('run_43824*')

command = '/home/gavalian/coatjava/bin/hipo-utils -merge -o /work/clas12/viducic/43824_full.hipo '

for f in file:
    command+= f + ' '
cmd_exec = command + " " + f
print(cmd_exec)
os.system(cmd_exec)