"""
Dynamically Corrected Transition State Theory (dctst) tools.
"""

import numpy as np


def calculate_rate(fq_star, fq_area, mw, temperature=200, kappa=1.0):
    """
    Calculate rate (k_ab).

    Parameters
    ----------
    fq_star : float
        Activation energy (kcal / mol)
    fq_area : float
        Integral of free energy barrier (kcal / mol)
    mw : float
        Molecular weight (g / mol)
    temperature: float
        System temperature in K
    kappa : float
        Some constant (default: 1.0)

    Returns
    -------
    float
        Transition rate (1 / s)
    """
    # kab_hand = np.sqrt(4.184e6 * 0.001987 * 200 / (2 * np.pi * 787.17)) * np.exp(-beta * 13) / (INTEGRAL)
    k_ab = kappa * 36.377 * np.sqrt(temperature / mw) * fq_star / fq_area
    return k_ab


def calculate_diffusion(rate, lamda=1, nn=2.765, n=1):
    """
    Calculate Ds.

    Parameters
    ----------
    rate : float
        Transition rate (1/s)
    n : int
        Dimensionality
    lamda : float
        Jump length (A)
    nn : float
        Nearest neighbour distance (default: 2.765 A for Cu(110))

    Returns
    -------
    float
        Diffusion coefficient (cm2 / s)
    """
    D_s = 1 / 2 * rate * ((lamda * nn * 1e-8) ** 2)   # cm2 / s
    return D_s


def calculate_boltzmann_average(energy, temperature, kb=0.0019872041):
    """
    Calculates average energy for a given list of energy values according to a Boltzmann distribution.

    Parameters
    ----------
    energy : list
        List of energy values
    temperature : float
        System temperature (K)
    kb : float
        Boltzmann constant (default: 0.0019872041 kcal / mol.K)

    Returns
    -------
    float
        Boltzmann average of energy
    """
    beta = 1 / (kb * temperature)
    F = np.array(energy)
    Ptot = np.exp(-F * beta)
    P = Ptot / Ptot.sum()
    F_avg = (P * F).sum()
    return F_avg


def fit_gaussian(position, energy, dx=0.005, a=2, b=1.5, db=0.01, tolerance=0.05, max_iterations=1000):
    """
    Fits a gaussian curve as an energy barrier.
    The gaussian has the form: F = exp(-a * (dx/2 - x))^2 + b
    The b constant is iteratively modified to change the peak of the gaussian curve.
    The peak value is optimized to be as close to the activation energy as possible.

    Parameters
    ----------
    position : list
        Position values for the energy barrier (x-axis).
    energy: list
        Free energy values (y-axis).
    dx : float
        Gaussian position values step size.
    a : float
        Gaussian constant -> a (see equation above).
        This can be modified to change the area under the curve without modifying the peak value.
    b : float
        Gaussian constant -> b (see equation above).
        This is iteratively changed to find the peak value of the gaussian.
    db : float
        Step size for changing the b constant in each iteration.
    tolerance : float
        Stopping criteria for the b constant search.
        If difference between the peak value of the gaussian and acivation energy is smaller
        than this value search is finished. If not the value that gives the smallest energy
        difference is used.
    max_iterations : int
        Maximum number of iterations for the b constant search.

    Returns
    -------
    tuple
        Gaussian x-axis (position) and y-axis (free energy).
    """
    min_energy, max_energy = min(energy), max(energy)
    x_start, x_range = min(position), max(position) - min(position)
    x_gauss = np.arange(0, x_range, dx)
    f_gauss = np.exp(-a * (x_range / 2 - x_gauss) ** 2 + b)
    delta_energy = abs(max(f_gauss) - max_energy)
    b_direction = np.sign(max_energy - max(f_gauss))
    print('E_WHAM: %.3f | E_GAUSS: %.3f | b_direction: %i' % (max_energy, max(f_gauss), b_direction))
    for i in range(max_iterations):
        b = b + b_direction * db
        f_gauss_trial = np.exp(-a * (x_range / 2 - x_gauss) ** 2 + b)
        delta_energy_trial = abs(max(f_gauss_trial) - max_energy)
        if delta_energy_trial < tolerance:
            f_gauss = f_gauss_trial
            print('Found b value: %.2f with dE: %.3f within tolerance in %i iterations' % (b, delta_energy, i))
            break
        elif delta_energy_trial < delta_energy:
            f_gauss = f_gauss_trial
            delta_energy = delta_energy_trial
    print('Finished fitting. %i iterations | dE: %.3f | b_final: %.2f' % (i, delta_energy, b))
    return (x_gauss + x_start, f_gauss)
