"""
WHAM plotting functions.
"""
import matplotlib.pyplot as plt
import numpy as np


def subplot(plot_fun, plot_args, nrow=1, width=3, height=3, dpi=200, save=None):
    n_plots = len(plot_args)
    ncol = np.ceil(n_plots / nrow)
    figsize = (ncol * width, nrow * height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.subplots_adjust(hspace=.5, wspace=.25)
    for idx, args in enumerate(plot_args, start=1):
        args['ax'] = fig.add_subplot(nrow, ncol, idx)
        plot_fun(**args)
    if save is not None:
        plt.savefig(save, dpi=dpi, transparent=True, bbox_inches='tight')


def wham_plot(x, y, ax, xlabel, ylabel, title, xlim, plot_atom_pos=True):
    ax.plot(x, y, '-o', c='xkcd:crimson', lw=2, markersize=6)
    plt.xlim(xlim)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # Draws a line to the surface atom positions on y-axis
    if plot_atom_pos:
        ylims = list(ax.get_ylim())
        ax.plot([22.8912, 22.8912], ylims, c='k')
        ax.plot([25.4346, 25.4346], ylims, c='k')
        ax.plot([24.1629, 24.1629], ylims, 'k--', alpha=0.7)
