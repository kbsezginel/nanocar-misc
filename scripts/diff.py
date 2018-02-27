"""
Nanocar result analysis
"""
import numpy as np
from angstrom import Trajectory
from msdtools import read_msd_data, read_lammps_msd_data, plot_msd


start_frame = 101   # Start reading from
dt = 0.5            # femtoseconds
time_unit = 'ns'    # time to convert
sim_box = [39.08, 41.4506, 50]

# Calculate MSD
msd_data = read_msd_data('traj.xyz', sim_box, start_frame=start_frame, dt=dt, time_unit=time_unit)
print(msd_data['d0'])

# Read Lammps MSD
lammps_data = read_lammps_msd_data('msd1.csv', dt=dt, time_unit=time_unit)
print(lammps_data['d0'])

# Save MSD vs time figure
plot_msd(msd_data, save='msd-time-ang.png')
plot_msd(lammps_data, save='msd-time-lammps.png')
