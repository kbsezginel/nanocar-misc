"""
WHAM analysis helper functions.
"""
import numpy as np
import subprocess


def run_wham(wham_args):
    wham_args = [str(i) for i in wham_args]
    subprocess.run(wham_args)
    return read_wham_out(wham_args[-1])


def read_wham_out(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = dict(coor=[], free=[], prob=[])
    for line in lines[1:]:
        ls = line.split()
        if ls[0] == '#Window':
            break
        else:
            data['coor'].append(float(ls[0]))
            data['free'].append(float(ls[1]))
            data['prob'].append(float(ls[3]))
    return data


def write_timeseries_file(filename, time, position):
    with open(filename, 'w') as f:
        for t, p in zip(time, position):
            f.write('%.2f  %.5f\n' % (t, p))


def timesteps_to_time(timesteps, dt=1, conversion=1e-3):
    """ Convert time steps to time """
    return np.array(timesteps) * dt * conversion


def write_data_file(filename, tsfile, minimum, spring):
    with open(filename, 'w') as f:
        for ts, m, k in zip(tsfile, minimum, spring):
            f.write('%s  %.5f  %.2f\n' % (ts, m, k))
