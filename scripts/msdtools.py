"""
Functions to read and analyze MSD data.
"""
import os
import csv
import datetime
import subprocess
import numpy as np
from angstrom import Trajectory
import matplotlib
matplotlib.use('agg')              # So it works on H2P ($DISPLAY variable is not defined)
import matplotlib.pyplot as plt


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


msd_settings = {'directions': ['x', 'y', 'z'], 'time_unit': 'ns', 'figsize': (15, 2.5), 'dpi': 200,
                'subplots_adjust': (0.0, 0.25), 'suptitle': None, 'markersize': 30, 'linewidth': 2,
                'fontsize': {'label': 14, 'title': 16, 'text': 20, 'tick': 14, 'suptitle': 18, 'fit': 12},
                'color': {'x': '#c1ef1c', 'y': '#ff765e', 'z': '#c1ef1c', 'all': 'r', 'text': 'k', 'tick': 'k', 'fit': 'k'},
                'fit': {'text': '$D_0$: %.1E $cm^2/s$\n$R^2$: %.3f',
                'box': dict(boxstyle='round', facecolor='w', alpha=0.3, edgecolor='w'), 'loc': (0.5, 0.65)}}


def plot_msd(msd_data, settings=msd_settings, save=None):
    """ Plot MSD vs time plots for each direction """
    fig = plt.figure(figsize=settings['figsize'], dpi=settings['dpi'])
    fig.subplots_adjust(hspace=settings['subplots_adjust'][0], wspace=settings['subplots_adjust'][1])
    if settings['suptitle'] is not None:
        fig.suptitle(settings['suptitle'], fontsize=settings['fontsize']['suptitle'], y=1.05)
    for idx, axis in enumerate(settings['directions'], start=1):
        ax = fig.add_subplot(1, len(settings['directions']), idx)
        ax.scatter(msd_data['time'], msd_data[axis], s=settings['markersize'], alpha=0.6,
                   c=settings['color'][axis], edgecolor='k', linewidth=0.2)
        ax.tick_params(labelsize=settings['fontsize']['tick'], labelcolor=settings['color']['tick'])
        plt.title('MSD (%s)' % axis, fontsize=settings['fontsize']['title'])
        plt.xlabel('Time (%s)' % settings['time_unit'], fontsize=settings['fontsize']['label'])
        plt.xlim(-0.02, max(msd_data['time']) + 0.02)

        # Linear fitting
        if settings['fit'] is not None:
            msd_fit = [msd_data['a'][axis] * x + msd_data['b'][axis] for x in msd_data['time']]
            ax.plot(msd_data['time'], msd_fit, '%s--' % settings['color']['fit'], linewidth=2)
            diff_text = settings['fit']['text'] % (msd_data['d0'][axis], msd_data['r2'][axis])
            y_text = (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.1 + ax.get_ylim()[0]
            x_text = msd_data['time'][-1] * settings['fit']['loc'][0]
            plt.text(x_text, y_text, diff_text, color=settings['color']['fit'],
                     fontsize=settings['fontsize']['fit'], bbox=settings['fit']['box'])

    if save is not None:
        plt.savefig(save, dpi=settings['dpi'], transparent=True, bbox_inches='tight')
        print('Saved -> %s' % save)


"""
Markdown report template to be formatted. Add following sections (in order):
 - title,
"""

report_template = """
%s
=======

MSD Trajectory
--------------

![msd-traj](%s)

LAMMPS MSD vs time
------------------

![lammps-msd](%s)

Angstrom MSD vs time
------------------

![ang-msd](%s)

### Simulation details

-   Simulation directory: %s
-   Report date: %s

#### Simulation files

%s
"""


def get_file_table(sim_dir):
    """ Get list of files in the simulation directory and create a table. """
    file_list = os.listdir(sim_dir)
    rows = [['File', 'Date', 'Size']]
    for f in file_list:
        stats = os.stat(os.path.join(sim_dir, f))
        f_date = datetime.datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M")
        f_size = "%.1f kB" % (stats.st_size / 1024)  # In kilobytes
        rows.append([f, f_date, f_size])
    return html_table(rows)


def html_table(rows):
    """ Generate HTML table string using a list of rows (first one is headers) """
    text = '<table>\n'
    for i, row in enumerate(rows):
        text += '  <tr>\n'
        if i == 0:
            text += ''.join(['    <th>%s</th>\n' % col for col in row])
        else:
            text += ''.join(['    <td>%s</td>\n' % col for col in row])
        text += '  </tr>\n'
    text += '</table>\n'
    return text


"""
VMD movie generation
"""


def vmd_movie(sim_dir, report_dir, vis_state, movie_file='movie.gif'):
    """ Generate VMD movie """
    cmd = ['vmd', '-dispdev', 'text', '-eofexit']
    vmd_inp = open(vis_state, 'r')
    subprocess.call(cmd, stdin=vmd_inp, cwd=sim_dir)
    vmd_inp.close()
    # Consider adding this part to vis-state.vmd instead of doing the move here
    os.rename(os.path.join(sim_dir, movie_file), os.path.join(report_dir, movie_file))
