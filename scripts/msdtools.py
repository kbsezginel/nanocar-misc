"""
Functions to read and analyze MSD data.
"""
import os
import csv
import numpy as np
from angstrom import Trajectory


def read_msd(msd_file, dt=0.5, time_unit='ns'):
    """ Read csv formatted msd file (dt in femtoseconds) """
    time_conv = {'fs': 1, 'ps': 0.001, 'ns': 0.000001}
    msd_data = {'step': [], 'x': [], 'y': [], 'z': [], 'all': [], 'time': []}
    with open(msd_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)  # Skip header
        for row in reader:
            msd_data['step'].append(int(row[0]))
            msd_data['time'].append(int(row[0]) * time_conv[time_unit] * dt)
            msd_data['x'].append(float(row[1]))
            msd_data['y'].append(float(row[2]))
            msd_data['z'].append(float(row[3]))
            msd_data['all'].append(float(row[4]))
    return msd_data


def read_lammps_msd_data(msd_file, dt=0.5, time_unit='ns'):
    """ Read Lammps MSD vs time data and calculate diffusion coefficient """
    msd_data = read_msd(msd_file, dt=dt, time_unit=time_unit)
    msd_data['d0'] = {'x': 0, 'y': 0, 'z': 0, 'all': 0}
    msd_data['r2'] = {'x': 0, 'y': 0, 'z': 0, 'all': 0}
    msd_data['a'] = {'x': 0, 'y': 0, 'z': 0, 'all': 0}
    msd_data['b'] = {'x': 0, 'y': 0, 'z': 0, 'all': 0}
    for axis in ['x', 'y', 'z', 'all']:
        diff = calculate_d0(msd_data['time'], msd_data[axis], time_unit=time_unit)
        msd_data['d0'][axis] = diff['d0']
        msd_data['r2'][axis] = diff['r2']
        msd_data['a'][axis] = diff['a']
        msd_data['b'][axis] = diff['b']
    return msd_data


"""
Diffusivity --------------------------------------------------------------------------------
"""


def calculate_d0(time, msd, time_unit='ns'):
    """ Calculate diffusion coefficient from A2/time_unit to in cm2/s and R2 from MSD vs time data """
    time, msd = np.array(time), np.array(msd)
    coeffs = np.polyfit(time, msd, 1)          # Linear fit coefficients
    f_fit = np.poly1d(coeffs)
    y_fit = f_fit(time)

    ybar = np.mean(msd)
    ss_tot = np.sum(np.power(msd - ybar, 2))
    ss_res = np.sum(np.power(msd - y_fit, 2))
    r2 = 1 - ss_res / ss_tot

    time_conv = {'fs': 15, 'ps': 12, 'ns': 9}     # From given unit to s
    dist_conv = {'nm2': 2, 'cm2': 16, 'm2': 20}   # From Angstrom2 to dist_unit
    dist_unit = 'cm2'
    d0 = coeffs[0] * (10 ** (time_conv[time_unit] - dist_conv[dist_unit]))
    return {'r2': r2, 'd0': d0, 'a': coeffs[0], 'b': coeffs[1]}


"""
MSD calculation ------------------------------------------------------------------------------------
"""


def calculate_msd(coordinates, reference=0):
    ref_coor = coordinates[reference]
    return np.average(np.power((coordinates - ref_coor), 2))


def get_msd_vs_time(np_coor, timesteps, dt=0.5, time_unit='ns'):
    time_conv = {'fs': 1, 'ps': 0.001, 'ns': 0.000001}
    msd_data = {'x': [], 'y': [], 'z': [], 'time': []}
    n_frames = len(np_coor)
    for frame in range(1, n_frames):
        xcoor, ycoor, zcoor = np_coor[:frame, 0, 0], np_coor[:frame, 0, 1], np_coor[:frame, 0, 2]
        msd_data['x'].append(calculate_msd(xcoor))
        msd_data['y'].append(calculate_msd(ycoor))
        msd_data['z'].append(calculate_msd(zcoor))
        msd_data['time'].append(timesteps[frame - 1] * time_conv[time_unit] * dt)
    return msd_data


def read_msd_data(traj_file, sim_box, start_frame=101, dt=0.5, time_unit='ns'):
    """ Read MSD and diffusivity from simulation using Angstrom """
    traj = Trajectory(read=traj_file)
    np_traj = traj.non_periodic([39.08, 41.4506, 50])

    np_coor = np_traj.coordinates[start_frame:, :, :]
    timesteps = [int(h.split('Timestep:')[1]) for h in traj.headers][start_frame:]

    msd_data = get_msd_vs_time(np_coor, timesteps, dt=dt, time_unit=time_unit)
    msd_data['d0'] = {'x': 0, 'y': 0, 'z': 0}
    msd_data['r2'] = {'x': 0, 'y': 0, 'z': 0}
    msd_data['a'] = {'x': 0, 'y': 0, 'z': 0}
    msd_data['b'] = {'x': 0, 'y': 0, 'z': 0}
    for axis in ['x', 'y', 'z']:
        diff = calculate_d0(msd_data['time'], msd_data[axis], time_unit=time_unit)
        msd_data['d0'][axis] = diff['d0']
        msd_data['r2'][axis] = diff['r2']
        msd_data['a'][axis] = diff['a']
        msd_data['b'][axis] = diff['b']
    return msd_data


"""
Plot MSD vs time -----------------------------------------------------------------------------------
"""


lammps_msd_settings = {'msd_file': 'msd1.csv', 'dt': 0.5, 'time_unit': 'ns', 'dpi': 200,
                       'directions': ['all', 'x', 'y', 'z'], 'suptitle': None,
                       'fit': {'text': '$D_0$: %.1E $cm^2/s$\n$R^2$: %.3f', 'box': dict(boxstyle='round', facecolor='w', alpha=0.3, edgecolor='w'), 'loc': (0.5, 0.65)},
                       'text': ['ε: 2', 'ε: 3', 'ε: 4', 'ε: 5', 'ε: 7.5', 'ε: 10'],
                       'figsize': None, 'subplots_adjust': (0.0, 0.25),
                       'text_box': dict(boxstyle='round', facecolor='xkcd:coral', alpha=0.3, edgecolor='white'),
                       'color': {'x': 'xkcd:coral', 'y': 'xkcd:crimson', 'z': 'xkcd:coral', 'all': 'xkcd:crimson', 'text': 'xkcd:crimson', 'tick': 'k', 'fit': 'k'},
                       'fontsize': {'label': 14, 'title': 16, 'text': 20, 'tick': 16, 'suptitle': 18, 'fit': 12}}


def plot_lammps_msd(sim_list, settings=lammps_msd_settings, save=None):
    """ Plot LAMMPS MSD vs time plots for a list of simulations """
    if settings['figsize'] is None:
        settings['figsize'] = (22, 2.2 * len(sim_list))
    fig = plt.figure(figsize=settings['figsize'], dpi=settings['dpi'])
    fig.subplots_adjust(hspace=settings['subplots_adjust'][0], wspace=settings['subplots_adjust'][1])
    if settings['suptitle'] is not None:
        fig.suptitle(settings['suptitle'], fontsize=settings['fontsize']['suptitle'], y=1.05)
    idx = 1
    for i, sim_dir in enumerate(sim_list, start=1):
        msd_file = os.path.join(sim_dir, settings['msd_file'])
        msd_data = read_msd(msd_file, dt=settings['dt'], time_unit=settings['time_unit'])
        for j, axis in enumerate(settings['directions'], start=1):
            ax = fig.add_subplot(len(sim_list), len(settings['directions']), idx)
            ax.scatter(msd_data['time'], msd_data[axis], s=10, alpha=0.5, c=settings['color'][axis])

            # Linear fitting
            if settings['fit'] is not None:
                diff = calculate_d0(msd_data['time'], msd_data[axis], time_unit=settings['time_unit'])
                msd_fit = [diff['a'] * x + diff['b'] for x in msd_data['time']]
                ax.plot(msd_data['time'], msd_fit, '%s--' % settings['color']['fit'])

            # Set yticks
            ymax = max(msd_data[axis])
            rounder = 10 ** (len(str(int(ymax))) - 1)
            ytick = int(ymax + (rounder - ymax % rounder))
            ax.tick_params(labelsize=settings['fontsize']['tick'], labelcolor=settings['color']['tick'])
            plt.yticks([0, ytick], ['', str(ytick)])

            if i == 1:
                plt.title('MSD (%s)' % axis, fontsize=settings['fontsize']['title'])
            if i == len(sim_list):
                plt.xlabel('Time (%s)' % settings['time_unit'], fontsize=settings['fontsize']['label'])
            else:
                plt.xticks([])
            if j == 1 and settings['text'] is not None:
                plt.text(msd_data['time'][-1] * 0.05, ytick * 0.7, settings['text'][i - 1],
                         fontsize=settings['fontsize']['text'], color=settings['color']['text'], bbox=settings['text_box'])
            if settings['fit'] is not None:
                diff_text = settings['fit']['text'] % (diff['d0'], diff['r2'])
                plt.text(msd_data['time'][-1] * settings['fit']['loc'][0], ytick * settings['fit']['loc'][1], diff_text,
                         color=settings['color']['fit'], fontsize=settings['fontsize']['fit'], bbox=settings['fit']['box'])

            idx += 1

    if save is not None:
        plt.savefig(save, dpi=settings['dpi'], transparent=True, bbox_inches='tight')
        print('Saved -> %s' % save)
