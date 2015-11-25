#! /usr/bin/python
import subprocess, sys
cmd = 'rm parallel* -rf results/* -rf numerics/*'
retcode = subprocess.call(cmd, shell=True)
if retcode != 0: sys.exit(retcode)
