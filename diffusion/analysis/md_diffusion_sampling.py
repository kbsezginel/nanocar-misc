"""
Reads MD position data.
"""
import os
import yaml
import numpy as np
from thermof.read import read_log, read_thermo


def read_lammps_out(simlist, var=['x', 'y', 'z', 'temp'], time_unit='ns', t_skip=0, dt_step=1, dt_frame=1000, log='lammps_out.txt'):
    """
    Reads LAMMPS output (log file) for multiple runs.

    Parameters
    ----------
    simlist : list
        List of simulation directories.
    var : list
        List of variables to return.
    time_unit : str
        Unit of time (fs | ps | [ns] | us | ms | s).
    t_skip : int
        Skips the first [time_unit] seconds of simulation data.
    dt_step : int
        Time step in femtoseconds (default: 1 fs).
    dt_frame : int
        Femtoseconds per frame (print interval) (default: 1000 fs = 1 ps).
    log : str or None
        Logfile name. If not given basename of scandir is taken -> (log.scanname).

    Returns
    -------
    dict
        Log data.

    """
    thermo_headers = 'Step Temp Press TotEng E_pair E_mol Fmax Fnorm c_C1[1] c_C1[2] c_C1[3]'
    thermo_keys = ['step', 'temp', 'press', 'etotal', 'epair', 'emol', 'fmax', 'fnorm', 'x', 'y', 'z']

    time_conv = {'fs': 1e0, 'ps': 1e3, 'ns': 1e6, 'us': 1e9, 'ms': 1e12, 's': 1e15}
    time_constant = dt_step / time_conv[time_unit]
    # Number of rows to skip
    t_skip = int(t_skip / dt_frame / dt_step * time_conv[time_unit])

    ALL_DATA = {}
    for simdir in simlist:
        logfile = os.path.join(simdir, '%s' % log)
        thermo_data = read_log(logfile, headers=thermo_headers)
        thermo = read_thermo(thermo_data, headers=thermo_keys)[0]
        data = {'time': np.array(thermo['step'][t_skip:]) * time_constant}
        for v in var:
            data[v] = np.array(thermo[v][t_skip:])
        ALL_DATA[os.path.basename(simdir)] = data
    return ALL_DATA


def read_position_array(simlist, directions=['x', 'y', 'z'], t_skip=0, log=None, save=None):
    """
    Reads position data for a simulation with multiple runs and arranges position data as a numpy array.

    Parameters
    ----------
    simlist : list
        List of simulation directories as different runs (seeds) of the same simulation.
    directions : list
        List of position directions.
    t_skip : int
        Skips the first t_skip ps of simulation data.
    log : str or None
        Logfile name. If not given basename of scandir is taken -> (log.scanname).
    save : str or None
        File name to save numpy array.

    Returns
    -------
    None
        Saves numpy array.
    """
    sim_name = os.path.basename(os.path.split(simlist[0])[0])
    sim_data = read_lammps_out(simlist, var=directions, t_skip=t_skip, log=log)
    # Create 3D numpy array with positions for each frame and for each run

    # Sort all run folders numerically and create ids for each run from 0 -> n_runs
    # This step is done to make sure numpy array index is the same as run index for cases
    # where run ids don't start from 0. For examples 1 - 5 becomes 0 - 4.
    run_idx = {}
    for idx, run in enumerate(sorted([int(i) for i in list(sim_data.keys())])):
        run_idx[str(run)] = idx
    print('%i runs:' % len(simlist))
    print('Run ids: ', run_idx)

    n_frames = len(sim_data[list(sim_data.keys())[0]][directions[0]])  # Really don't like this but whatever
    n_runs = len(sim_data.keys())
    n_dimensions = len(directions)
    pos_array = np.zeros((n_frames, n_runs, n_dimensions))

    for frame in range(n_frames):
        for run in sim_data:
            for didx, drx in enumerate(directions):
                # pos_array[frame][run_idx[run]][didx] = [sim_data[run]['x'][frame], sim_data[run]['y'][frame], sim_data[run]['z'][frame]]
                pos_array[frame][run_idx[run]][didx] = sim_data[run][drx][frame]

    if save is not None:
        np.save(save, pos_array)
    print('%s | Shape: (%i frames, %i runs, %i dimensions) | Saved: %s' % (sim_name, *pos_array.shape, save))
    return pos_array
