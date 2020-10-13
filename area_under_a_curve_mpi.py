from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_p = comm.Get_size()

if rank == 1:
    comm.send(2/2, dest = 0)
elif rank == 2:
    comm.send(4 + 5, dest = 0)
elif rank == 3:
    comm.send(2 * (6 + 6 + 4 + 4), dest = 0)
else:
    from_1 = int(comm.recv(source = 1))
    print("Value from Process 1: ", from_1)

    from_2 = int(comm.recv(source=2))
    print("Value from Process 2: ", from_2)

    from_3 = int(comm.recv(source = 3))
    print("Value from Process 3: ", from_3)

    area = from_1 * (from_2 + from_3)
    print("Area Under the Curve Via Trapezium Rule is ", area, "Units Squared")