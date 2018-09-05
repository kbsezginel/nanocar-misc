#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def autocorrFFT(x, N):
    N=len(x)
    F = np.fft.fft(x, n=2*N)  #2*N because of zero-padding
    PSD = F * F.conjugate()
    res = np.fft.ifft(PSD)
    res= (res[:N]).real   #now we have the autocorrelation in convention B
    n=N*np.ones(N)-np.arange(0,N) #divide res(m) by (N-m)
    return res/n #this is the autocorrelation in convention A


def msd_fft(r, N):
    N=len(r)
    D=np.square(r).sum(axis=1)
    D=np.append(D,0)
    S2=sum([autocorrFFT(r[:, i], N) for i in range(r.shape[1])])
    Q=2*D.sum()
    S1=np.zeros(N)
    for m in range(N):
        Q=Q-D[m-1]-D[N-m]
        S1[m]=Q/(N-m)
        # if m % 10000 == 0:
        #     print(m)
    return S1-2*S2


def calculate_diffusion_coefficient(data, average_frames=1, fs_per_frame=1000, plot=False):
    """
    Calculate diffusion coefficient.

    Parameters
    ----------
    data : ndarray
        3D numpy array -> row:molecule:x,y,z
    average_frames : int
        Average n frames together
    fs_per_frame : int
        Femtoseconds per timestep
    plt : bool
        Plot MSD data
    """
    num_frames, num_molecules, num_dimensions = data.shape
    # Slice the position data so that we have the first n frames we want
    reduced_frames = num_frames // average_frames
    num_frames = reduced_frames * average_frames
    data = data[0:num_frames, :, :]

    # Time in nanoseconds
    simple_t = np.arange(0, num_frames / fs_per_frame, average_frames / fs_per_frame)

    ### per molecule data and plots
    all_results = np.zeros(reduced_frames)
    simple_results = np.zeros((num_molecules, reduced_frames))
    for m in range(num_molecules):
        # Molecule position data
        results = msd_fft(data[:num_frames, m, :], num_frames)
        simple_results[m, :] = np.mean(results.reshape(-1, average_frames), axis=1)

    simple_results /= (2 * num_dimensions)
    all_results = np.mean(simple_results, axis=0)

    # attempt fits across different ranges
    # generally for all fits, first 10% and last 50% are thrown away
    # different ranges from 0.1-0.5 are tried, and fit with lowest error is selected as the
    # "correct" fit and reported as the diffusivity
    lin_fit_pairs = [(0.0, 1.0), (0.10, 0.50), (0.10, 0.45), (0.10, 0.40), (0.10, 0.35), (0.30, 0.50),
                     (0.25, 0.50), (0.20, 0.50), (0.15, 0.50), (0.20, 0.40), (0.15, 0.40), (0.20, 0.45)]
    fit_results = []
    highest_r2 = None
    highest_r2_pair = None
    for pair in lin_fit_pairs:
        # y = at + b
        p1 = int(pair[0] * (reduced_frames - 1))
        p2 = int(pair[1] * (reduced_frames - 1))
        slope, intercept, r_value, _, _ = stats.linregress(simple_t[p1:p2], all_results[p1:p2])
        poly = (slope, intercept)
        r2 = r_value ** 2

        # pick best fit
        if not highest_r2 or r2 > highest_r2:
            highest_r2 = r2
            highest_r2_pair = (p1,p2)
        fit_results.append([(p1,p2), r2, poly])

    # plot combined data and fits
    if plot:
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('$tau (ns)$')
        ax.set_ylabel('$MSD (Å^2)$')
        ax.grid(linestyle='-', color='0.7', zorder=0)
        ax.plot(simple_t, all_results, zorder=10)

    fit_data = {}
    for r in fit_results:
        p, r2, poly = r
        d_cm2s = poly[0] * 1e-16 / 1e-9  # diffusivity in cm2 / s
        zorder = 2

        if p == highest_r2_pair:
            print("Best fit: (%.2f - %.2f ns; $R^2$ = %.3f):" % (simple_t[p[0]], simple_t[p[1]], r2))
            print("D = %2.3E $cm^2 / s$" % d_cm2s)
            d_cm2s = poly[0] * 1e-16 / 1e-9
            fit_data['best'] = {'cm2/s': poly[0] * 1e-16/1e-9, 'r2': r2, 't': '%.2f-%.2f' % (simple_t[p[0]], simple_t[p[1]])}
            zorder = 20

        fit_data['%.2f-%.2f' % (simple_t[p[0]], simple_t[p[1]])] = {'cm2/s': d_cm2s, 'r2': r2}

        if plot:
            ax.plot(simple_t[p[0]:p[1]], np.polyval(poly, simple_t[p[0]:p[1]]), zorder=zorder,
                    label="(%.2f - %.2f ns; $R^2$ = %0.3f) D: %.3e $cm^2/s$" % (simple_t[p[0]], simple_t[p[1]], r2, d_cm2s))
    if plot:
        ax.legend()
        fig.savefig("msd_fft_all_plot.png", dpi=288)

    return fit_data
