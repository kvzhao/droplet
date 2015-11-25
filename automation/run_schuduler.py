#! /usr/bin/python
import subprocess, sys
import os
import math

# ============================== #
task_name = 'regular'
# ====  Phsical Parameters ===== #
# Initala velocity list
V = [3.3e-3, 4.1e-3]
# Diameter list
D = [3.59]
# terminate time
T = 0.01
# ============================== #

# Grid resolution
level = 3
ncores = 8

for d0 in D:
    for v0 in V:
        case = task_name + '-' + '_'.join(['v'+str(v0),'d'+str(d0)])
        results_dir = 'results/' + case
        numerics_dir = 'numerics/' + case
        if not os.path.exists(results_dir):
            os.mkdir(results_dir)
        if not os.path.exists(numerics_dir):
            os.mkdir(numerics_dir)

        PARAM = ' -D'.join(['', 'V0='+str(v0), 'D0='+str(d0), 'LEVEL='+str(level),'CASE='+case, 'DURATION='+str(T)])
        TASK = task_name + '.gfs'
        SIMULATOR = 'gerris2D'
        cmd = ' '.join([SIMULATOR, PARAM, TASK])
        print cmd
        print '--- Launch Gerris on case ' + case + ' ---'

        # split the domain, twice
        cmd = ' '.join([SIMULATOR, PARAM, '-s', '2', TASK, '>', 'parallel-s.gfs'])
        print cmd
        retcode = subprocess.call(cmd, shell=True)

        p = str(int(math.log(ncores, 2)))
        cmd = ' '.join([SIMULATOR, '-p', p, 'parallel-s.gfs', '>', 'parallel-p.gfs'])
        print cmd
        retcode = subprocess.call(cmd, shell=True)

        # run the mpi simulation
        cmd = ' '.join(['mpirun', '-np', str(ncores), SIMULATOR, 'parallel-p.gfs'])
        print cmd
        retcode = subprocess.call(cmd, shell=True)
        if retcode != 0: sys.exit(retcode)
