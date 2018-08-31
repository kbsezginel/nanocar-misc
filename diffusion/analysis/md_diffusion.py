"""
Reads MD position data.
"""
import os
import yaml
import numpy as np
from thermof.read import read_log, read_thermo


def read_position_data(scandir, t_skip=0, dt=1, time_unit='ns', log=None):
    """
    Reads LAMMPS output (log file) to collect molecule position data.

    Parameters
    ----------
    scandir : str
        Molecule scan directory.
    t_skip : int
        Skips the first t_skip ps of simulation data.
    dt : int
        Time step in femtoseconds
    time_unit : str
        Unit of time (fs | ps | [ns] | us | ms | s)
    log : str or None
        Logfile name. If not given basename of scandir is taken -> (log.scanname).

    Returns
    -------
    dict
        Position data.
        - x : list -> All x positions for all simulations
        - y : list -> All y positions for all simulations
        - z : list -> All z positions for all simulations
        - time : list -> Time for all simulations in nanoseconds

    """
    thermo_headers = 'Step Temp Press TotEng E_pair E_mol Fmax Fnorm c_C1[1] c_C1[2] c_C1[3]'
    thermo_keys = ['step', 'temp', 'press', 'etotal', 'epair', 'emol', 'fmax', 'fnorm', 'x', 'y', 'z']

    time_conv = {'fs': 1e0, 'ps': 1e3, 'ns': 1e6, 'us': 1e9, 'ms': 1e12, 's': 1e15}
    time_constant = dt / time_conv[time_unit]

    if log is None:
        log = os.path.basename(scandir)
    scanlist = [os.path.join(scandir, i) for i in os.listdir(scandir)]
    ALL_DATA = {}
    for simdir in scanlist:
        logfile = os.path.join(simdir, '%s' % log)
        thermo_data = read_log(logfile, headers=thermo_headers)
        thermo = read_thermo(thermo_data, headers=thermo_keys)[0]
        time = np.array(thermo['step']) * time_constant
        pos_data = {'x': thermo['x'][t_skip:], 'y': thermo['y'][t_skip:],
                    'z': thermo['z'][t_skip:], 'time': time}
        ALL_DATA[os.path.basename(simdir)] = pos_data
    return ALL_DATA


def save_np_array(simdir, npdir, t_skip=0, log=None):
    """
    Reads position data for a simulation with multiple runs and saves position data as a numpy array.

    Parameters
    ----------
    simdir : str
        Simulation directory with subdirectories as different runs (seeds) of the same simulation.
    npdir : str
        Directory to save numpy arrays.
    t_skip : int
        Skips the first t_skip ps of simulation data.
    log : str or None
        Logfile name. If not given basename of scandir is taken -> (log.scanname).

    Returns
    -------
    None
        Saves numpy array.
    """
    sim_name = os.path.basename(simdir)
    sim_data = read_position_data(simdir, t_skip=t_skip, log=log)
    # Create 3D numpy array with positions for each frame and for each run

    # Sort all run folders numerically and create ids for each run from 0 -> n_runs
    # This step is done to make sure numpy array index is the same as run index for cases
    # where run ids don't start from 0. For examples 1 - 5 becomes 0 - 4.
    run_idx = {}
    for idx, run in enumerate(sorted([int(i) for i in list(sim_data.keys())])):
        run_idx[str(run)] = idx
    print('Run ids: ', run_idx)

    n_frames = len(sim_data[list(sim_data.keys())[0]]['x'])  # Really don't like this but whatever
    n_runs = len(sim_data.keys())
    pos_array = np.zeros((n_frames, n_runs, 3))

    for frame in range(n_frames):
        for run in sim_data:
            pos_array[frame][run_idx[run]] = [sim_data[run]['x'][frame], sim_data[run]['y'][frame], sim_data[run]['z'][frame]]

    if not os.path.exists(npdir):
        os.makedirs(npdir)
        print('Creating directory -> %s' % npdir)
    np_array_filename = os.path.join(npdir, '%s-pos' % sim_name)
    np.save(np_array_filename, pos_array)
    print('%s | Shape: (%i, %i, %i) | Saved: %s' % (sim_name, *pos_array.shape, np_array_filename))


def read_diff_data(filename):
    """Read MSD code output."""
    with open(filename, 'r') as f:
        lines = f.readlines()
    diff_data = {}
    for line in lines:
        if 'SIM:' in line:
            sim = line.split()[1].split('-pos')[0]
        if 'cm^2 / s' in line:
            diff = float(line.split()[2])
            diff_data[sim] = diff
    return diff_data


def collect_diff_data(sim_dir):
    diff_data = {}
    for sim in os.listdir(sim_dir):
        if os.path.isdir(os.path.join(sim_dir, sim)):
            with open(os.path.join(sim_dir, sim, 'fit_results.yaml'), 'r') as f:
                sim_diff = yaml.load(f)
            diff_data[sim.split('-')[0]] = sim_diff
    return diff_data
