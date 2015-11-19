#! /usr/bin/python
import subprocess, sys
cmd = 'rm *.vtk splash*.gfs t k'
retcode = subprocess.call(cmd, shell=True)
if retcode != 0: sys.exit(retcode)
