#!/usr/bin/env python

import os
import subprocess
import glob

#Takes the .bos files and filters them for the banks that you need.
#output to after -o

file = glob.glob('run_437*_pass*')

command = '/group/clas12/packages/bos/bosutility -filter -b "HEADHEVTEVNTTAGRECPBCCPBSCPBLCPB" -o ' \
          '/work/clas12/viducic/bosfiltered/'

for f in file:
        cmd_exec = command + f + '.filtered  ' + f
        print(cmd_exec)
        os.system(cmd_exec)