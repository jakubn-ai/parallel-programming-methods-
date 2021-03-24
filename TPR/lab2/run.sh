for points in 1000 10000 100000 1000000 10000000; do
	mpiexec -machinefile ./allnodes_lab2 -np 1 ./pi.py $points
	for nodes in 1 2 3 4 5 6 7 8 9 10 11 12; do
		mpiexec -machinefile ./allnodes_lab2 -np $nodes ./pi_parall.py $points
		mpiexec -machinefile ./allnodes_lab2 -np $nodes ./pi_strong_stalled.py $points

	done
done
		
		