#! /usr/bin/python
import subprocess, sys
cmd = 'rm *.vtk t parallel* results/*'
retcode = subprocess.call(cmd, shell=True)
if retcode != 0: sys.exit(retcode)
