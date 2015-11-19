#! /usr/bin/python
import subprocess, sys

task_name = 'regular.gfs'
# split the domain twice to get enough boxes to redistribute
cmd = 'gerris2D -s 2 ' + task_name + ' > parallel-s2.gfs'
retcode = subprocess.call(cmd, shell=True)

# create the initial partition into 2^2=4 subdomains
cmd = 'gerris2D -p 3 parallel-s2.gfs > parallel-p8.gfs'
retcode = subprocess.call(cmd, shell=True)

# run the parallel simulation on 4 processors, pipe the output to
cmd = 'mpirun -np 8 gerris2D parallel-p8.gfs'
retcode = subprocess.call(cmd, shell=True)

if retcode != 0: sys.exit(retcode)
