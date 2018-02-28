"""
Nanocar LAMMPS simulation report.

Usage:
 >>> python sim_report.py /path/to/simulation /path/to/report
or you can also give a simulation title:
 >>> python sim_report.py /path/to/simulation /path/to/report sim-title

Using with a bash script:
reportdir='kutmatik/reports'
simdir='/sim/dir'
simtitle='kutmatik'
python sim_report.py $simdir $reportdir $simtitle
"""
import os
import sys
import datetime
import numpy as np
from angstrom import Trajectory
from msdtools import read_msd_data, read_lammps_msd_data, plot_msd
from msdtools import report_template, get_file_table, vmd_movie


start_frame = 101   # Start reading from
dt = 0.5            # femtoseconds
time_unit = 'ns'    # time to convert
sim_box = [39.08, 41.4506, 50]

# Directories #####################################################
sim_dir = os.path.abspath(sys.argv[1])
save_dir = os.path.abspath(sys.argv[2])
if len(sys.argv) > 3:
    sim_title = str(sys.argv[3])
else:
    sim_title = os.path.basename(sim_dir)
# Files ###########################################################
traj_file = os.path.join(sim_dir, 'traj.xyz')
csv_file = os.path.join(sim_dir, 'msd1.csv')
traj_movie = os.path.join(save_dir, 'movie.gif')
ang_plot = os.path.join(save_dir, 'msd-time-ang.png')
lammps_plot = os.path.join(save_dir, 'msd-time-lammps.png')
report_file = os.path.join(save_dir, 'report.md')
###################################################################

# Generate movie
vmd_movie(sim_dir, save_dir, 'vis-state.vmd')

# Calculate MSD
msd_data = read_msd_data(traj_file, sim_box, start_frame=start_frame, dt=dt, time_unit=time_unit)

# Read Lammps MSD
lammps_data = read_lammps_msd_data(csv_file, dt=dt, time_unit=time_unit)

# Save MSD vs time figure
plot_msd(msd_data, save=ang_plot)
plot_msd(lammps_data, save=lammps_plot)

# Create summary report
file_table = get_file_table(sim_dir)
report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
report = report_template % (sim_title, traj_movie, lammps_plot, ang_plot, sim_dir, report_date, file_table)
with open(report_file, 'w') as rep:
    rep.write(report)
