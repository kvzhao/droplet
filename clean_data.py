#! /usr/bin/python
import subprocess, sys
cmd = 'rm *.vtk res*.gfs *.dat t k parallel*'
retcode = subprocess.call(cmd, shell=True)
if retcode != 0: sys.exit(retcode)
