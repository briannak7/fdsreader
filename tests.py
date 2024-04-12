if __name__ == '__main__':
    import numpy as np
    from fdsreader import simulation

    # read in simulation
    sim = simulation.Simulation(
        r"/Users/bd/Desktop/bandy-circles/new_FDS/1_mesh/out_0_cat.smv")

    print(sim)

    boundary = sim.meshes[0].get_boundary_data("TOTAL HEAT FLUX")
    print(f'n_t: {boundary.n_t()}')

    # fdsreader returns data in (time, x, y) (this makes array operations difficult)
    data = boundary.data[boundary.orientations[0]].data

    # Make the data (time, y, x) so that array operations make sense
    data = np.swapaxes(data, 1, 2)

    times = boundary.times
    coords = boundary.data[boundary.orientations[0]].get_coordinates()

    print(f'Boundary data shape: {data.shape}')
