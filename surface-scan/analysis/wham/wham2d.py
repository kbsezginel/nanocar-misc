"""
WHAM=2D analysis helper functions.
"""
import numpy as np
import subprocess


def run_wham(wham_args, verbose=False):
    wham_args = [str(i) for i in wham_args]
    wham_process = subprocess.run(wham_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if verbose:
        stdout, stderr = wham_process.stdout.decode(), wham_process.stderr.decode()
        print("Stdout:\n\n%s\nStderr:\n%s" % (stdout, stderr))
    return read_wham_out(wham_args[-2])


def read_wham_out(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = dict(x=[], y=[], free=[], prob=[])
    for line in lines[1:]:
        ls = line.split()
        if len(ls) > 0:
            data['x'].append(float(ls[0]))
            data['y'].append(float(ls[1]))
            data['free'].append(float(ls[2]))
            data['prob'].append(float(ls[3]))
    return data


def read_wham_out_list(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = []
    scan_data = dict(x=[], y=[], free=[], prob=[])
    for line in lines[1:]:
        ls = line.split()
        if len(ls) == 0:
            data.append(scan_data)
            scan_data = dict(x=[], y=[], free=[], prob=[])
        elif len(ls) > 0:
            scan_data['x'].append(float(ls[0]))
            scan_data['y'].append(float(ls[1]))
            scan_data['free'].append(float(ls[2]))
            scan_data['prob'].append(float(ls[3]))
    return data


def write_timeseries_file(filename, time, position_x, position_y):
    with open(filename, 'w') as f:
        for t, px, py in zip(time, position_x, position_y):
            f.write('%.2f  %.5f  %.5f\n' % (t, px, py))


def timesteps_to_time(timesteps, dt=1, conversion=1e-3, shift=0):
    """ Convert time steps to time """
    return ((np.array(timesteps) * dt * conversion) - shift)


def write_data_file(filename, tsfile, minimum_x, minimum_y, spring_x, spring_y):
    with open(filename, 'w') as f:
        for ts, mx, my, kx, ky in zip(tsfile, minimum_x, minimum_y, spring_x, spring_y):
            f.write('%s  %.5f  %.5f  %.2f  %.2f\n' % (ts, mx, my, kx, ky))
