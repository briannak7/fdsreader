if __name__ == '__main__':
    import numpy as np
    from fdsreader import simulation

    # # read in simulation
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


    import matplotlib.pyplot as plt

    plt.imshow(data[0])
    plt.colorbar()
    plt.show()


    # sim = simulation.Simulation(
    # r"/Users/bd/Desktop/bandy-circles/example_simulation_w_slcf_data/out_0_cat.smv")
    # print(sim.meshes)

    # boundary = sim.meshes[0].get_boundary_data("TOTAL HEAT FLUX")
    # print(f'n_t: {boundary.n_t()}')

    # # fdsreader returns data in (time, x, y) (this makes array operations difficult)
    # data = boundary.data[boundary.orientations[0]].data

    # # Make the data (time, y, x) so that array operations make sense
    # data = np.swapaxes(data, 1, 2)

    # times = boundary.times
    # coords = boundary.data[boundary.orientations[0]].get_coordinates()

    # print(f'Boundary data shape: {data.shape}')

    # plt.imshow(data[900])
    # plt.colorbar()
    # plt.show()



    # /Users/bd/desktop/bandy-circles/2_patches

    # print('-------------------')
    # sim = simulation.Simulation(
    # r"/Users/bd/desktop/bandy-circles/2_patches/NIST_Methanol_1m_pan_4cm_grid_predicted.smv")
    # print('\n-------------------\n')
    # Location of file: 30205694 End of file: 30236970
    # Location of file: 30205694 End of file: 30236970
    # Location of file: 30205694 End of file: 30236970

    # print(sim.meshes)

    # print()

    # boundary = sim.meshes[0].get_boundary_data("GAUGE HEAT FLUX")
    # boundary = sim.meshes[1].get_boundary_data("GAUGE HEAT FLUX")
    # boundary = sim.meshes[2].get_boundary_data("GAUGE HEAT FLUX")
    # boundary = sim.meshes[3].get_boundary_data("GAUGE HEAT FLUX")
    # boundary = sim.meshes[4].get_boundary_data("GAUGE HEAT FLUX")
    # boundary = sim.meshes[0].get_boundary_data("TOTAL HEAT FLUX")

    # print(f'n_t: {boundary.n_t()}')

    # # fdsreader returns data in (time, x, y) (this makes array operations difficult)
    # data = boundary.data[boundary.orientations[0]].data

    # # Make the data (time, y, x) so that array operations make sense
    # data = np.swapaxes(data, 1, 2)

    # times = boundary.times
    # coords = boundary.data[boundary.orientations[0]].get_coordinates()

    # print(f'Boundary data shape: {data.shape}')

    # plt.imshow(data[900])
    # plt.colorbar()
    # plt.show()


