#!/usr/bin/env python
from mpi4py import MPI
import numpy as np
import sys
import pickle
import math
import random

points = long(sys.argv[1])
#points = 1000000
radius = 1
points_in_circle = 0
start = MPI.Wtime()

for i in xrange(points):
	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)

	if math.sqrt(x**2 + y**2) <= radius:
		points_in_circle += 1

area = points_in_circle * 1.0 / points * 4
pi = area / radius**2
time =  MPI.Wtime() - start
with open('xyz.txt', 'a') as file:
    file.write('{},{}\n'.format(time, points))
print("PI, points: {}, time: {}, pi: {}".format(points, time, pi))
MPI.Finalize()

