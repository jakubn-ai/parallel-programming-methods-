#!/usr/bin/env python
from mpi4py import MPI
import numpy as np
import sys
import pickle
import math
import random
import time

comm = MPI.COMM_WORLD
num_of_proc = comm.Get_size()
rank = comm.Get_rank()

random.seed(time.time() + rank)
all_points = long(sys.argv[1])
points = all_points / num_of_proc
radius = 1
points_in_circle = 0

comm.Barrier()
start = MPI.Wtime()

for i in xrange(points):
	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)
	if math.sqrt(x**2 + y**2) <= radius:
		points_in_circle += 1

my_list = comm.gather(points_in_circle, root=0)
if rank == 0:
	all_points_in_circle = reduce(lambda x, y: x + y, my_list, 0)
	area = 4.0 * all_points_in_circle / all_points
	pi = area / radius**2

comm.Barrier()
time = MPI.Wtime() - start
with open('zyx.txt', 'a') as file:
    file.write('{},{},{}\n'.format(time, points, num_of_proc))



if rank == 0:
	print("PI_PARALL, all_points: {}, num_of_proc: {}, time: {}, pi: {}".format(all_points, num_of_proc, time, pi))

MPI.Finalize()