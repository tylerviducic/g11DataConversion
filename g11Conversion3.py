#!/usr/bin/env python

import os
import glob

#I used this to remove the files from my work directory when I was done but you dont NEED this step

file = glob.glob('run_43*')

command = 'rm /work/clas12/viducic/'

for f in file:
        newf = f.replace('.filtered', '')
        cmd_exec = command + newf
        print(cmd_exec)
        os.system(cmd_exec)