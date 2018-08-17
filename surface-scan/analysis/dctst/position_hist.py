import os
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab
from thermof.read import read_log, read_thermo


surfatoms1 = [[21.582, 22.8912], [25.179, 22.8912], [21.582, 25.4346], [25.179, 25.4346]]
surfatoms2 = [23.3805, 24.1629]


def read_position_data(scandir, T_SKIP=0):
    """
    Reads LAMMPS output (log file) to collect molecule position data.

    Parameters
    ----------
    scandir : str
        Molecule scan directory.
    T_SKIP : int
        Skips the first T_SKIP ps of simulation data.
    Returns
    -------
    dict
        Position data.
        - allx : list -> All x positions for all simulations
        - ally : list -> All y positions for all simulations
        - histx : dict -> x positions separated by x starting points of all simulations
        - histy : dict -> y positions separated by y starting points of all simulations

    """
    thermo_headers = 'Step Temp Press TotEng E_pair E_mol Fmax Fnorm c_C1[1] c_C1[2] c_C1[3]'
    thermo_keys = ['step', 'temp', 'press', 'etotal', 'epair', 'emol', 'fmax', 'fnorm', 'x', 'y', 'z']

    pos_data = {'allx': [], 'ally': [], 'histx': {}, 'histy': {}}
    SCAN = os.path.basename(scandir)
    scanlist = [os.path.join(scandir, i) for i in os.listdir(scandir)]
    for simdir in scanlist:
        logfile = os.path.join(simdir, 'log.%s' % SCAN)
        xi, yi = [int(i) for i in os.path.basename(simdir).split('-')]
        thermo_data = read_log(logfile, headers=thermo_headers)
        thermo = read_thermo(thermo_data, headers=thermo_keys)[0]

        # Combine all x and y positions into single lists
        pos_data['allx'] += thermo['x'][T_SKIP:]
        pos_data['ally'] += thermo['y'][T_SKIP:]

        # x positions separated for each x starting point (join all y starts)
        if '%s' % xi in pos_data['histx']:
            pos_data['histx']['%s' % xi] += thermo['x'][T_SKIP:]
        else:
            pos_data['histx']['%s' % xi] = thermo['x'][T_SKIP:]

        # y positions separated for each y starting point (join all x starts)
        if '%s' % yi in pos_data['histy']:
            pos_data['histy']['%s' % yi] += thermo['y'][T_SKIP:]
        else:
            pos_data['histy']['%s' % yi] = thermo['y'][T_SKIP:]
    return pos_data


def plot_hist(data, bins=50, color='xkcd:crimson', linestyle='k', alpha=0.25, lw=1.5, xlabel='', ylabel='Frequency'):
    """
    Plot position histogram.
    """
    (mu, sigma) = norm.fit(data)
    # the histogram of the data
    n, bins, patches = plt.hist(data, bins, normed=1, facecolor=color, alpha=alpha)
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, linestyle, linewidth=lw)
    plt.scatter(data[0], max(y), c='k')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def plot_surface_hist(xdata, ydata, cmap='GnBu_r', xlim=(21, 25.8), ylim=(22.3, 26.0), bin_size=(0.1, 0.1), figsize=(5, 4), dpi=200, save=None):
    """
    Plot 2D histogram of molecule position.
    """
    fig = plt.figure(figsize=figsize, dpi=dpi)
    bins = (abs(xlim[1] - xlim[0]) / bin_size[0], abs(ylim[1] - ylim[0]) / bin_size[1])
    print('Bins || x: %.2f Å (%.2f) | y: %.2f Å (%.2f)' % (bin_size[0], bins[0], bin_size[1], bins[1]))
    plt.hist2d(xdata, ydata, bins=bins, cmap=cmap)
    plt.colorbar()
    plt.scatter([i[0] for i in surfatoms1], [i[1] for i in surfatoms1], c='k', alpha=0.7, s=200, edgecolors='w', lw=2)
    plt.scatter(surfatoms2[0], surfatoms2[1], c='k', alpha=0.5, s=200, edgecolors='k', lw=2)
    plt.xlim(xlim)
    plt.ylim(ylim)
    if save is not None:
        plt.savefig(save, dpi=dpi, transparent=True, bbox_inches='tight')
