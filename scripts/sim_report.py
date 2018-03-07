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
 >>> python sim_report.py $simdir $reportdir $simtitle
"""
import os
import glob
import sys
import datetime
import numpy as np
from angstrom import Trajectory
from msdtools import read_msd_data, read_lammps_msd_data, plot_msd
from msdtools import report_template, get_file_table, vmd_movie, add_report_info
from msdtools import html_table, read_lammps_box, read_lammps_variables

"""
TO DO:
- Start frame as system argument??
"""

start_frame = 0     # Start reading from
time_unit = 'ns'    # time to convert
report_ts = str(datetime.datetime.now().timestamp())

# Directories #####################################################
sim_dir = os.path.abspath(sys.argv[1])
save_dir = os.path.abspath(sys.argv[2])
if len(sys.argv) > 3:
    sim_title = str(sys.argv[3])
else:
    sim_title = os.path.basename(sim_dir)
img_dir = os.path.join(save_dir, 'assets', 'reports', report_ts)
os.makedirs(img_dir, exist_ok=True)
# Files ###########################################################
traj_file = os.path.join(sim_dir, 'traj.xyz')
csv_file = os.path.join(sim_dir, 'msd1.csv')
traj_movie = os.path.join(img_dir, 'movie.gif')
ang_plot = os.path.join(img_dir, 'msd-time-ang.png')
lammps_plot = os.path.join(img_dir, 'msd-time-lammps.png')
report_file = os.path.join(save_dir, '%s.md' % report_ts)
index_md = os.path.join(save_dir, 'index.md')
vis_state = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'vis-state.vmd')
###################################################################

# Generate movie
vmd_movie(sim_dir, img_dir, vis_state)

# Read Lammps data and input
sim_box = read_lammps_box(glob.glob(os.path.join(sim_dir, 'data.*'))[0])
lammpsvar = read_lammps_variables(glob.glob(os.path.join(sim_dir, 'in.*'))[0])
dt = float(lammpsvar['dt'])

# Calculate MSD
msd_data = read_msd_data(traj_file, sim_box, start_frame=start_frame, dt=dt, time_unit=time_unit)

# Read Lammps MSD
lammps_data = read_lammps_msd_data(csv_file, dt=dt, time_unit=time_unit)

# Save MSD vs time figure
plot_msd(msd_data, save=ang_plot)
plot_msd(lammps_data, save=lammps_plot)

# Create summary report
vartable = html_table(list(lammpsvar.items()), header=False)
file_table = get_file_table(sim_dir)
report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
report = report_template % (sim_title, traj_movie, lammps_plot, ang_plot, sim_dir, report_date, vartable, file_table)
with open(report_file, 'w') as rep:
    rep.write(report)
add_report_info(index_md, report_ts, sim_title, report_date)
