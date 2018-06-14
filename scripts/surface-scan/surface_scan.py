"""
2D surface scan helper functions.
"""
import numpy as np


def read_datafile(datafile, skip_atoms=1400):
    with open(datafile, 'r') as f:
        datalines = f.readlines()
    atoms_start = datalines.index('Atoms\n') + 2 + skip_atoms
    atoms_end = datalines.index('Bonds\n') - 1
    masses_start = datalines.index('Masses\n') + 2
    masses_end = datalines.index('Bond Coeffs\n') - 1
    elements = {}
    for i, line in enumerate(datalines[masses_start:masses_end]):
        element = line.split()[3]
        if element[1] == '_':
            element = element[0]
        else:
            element = element[:2]
        elements[line.split()[0]] = element
    n_atoms = atoms_end - atoms_start
    atomids, atoms, coords = [], [], np.empty((n_atoms, 3))
    for i, line in enumerate(datalines[atoms_start:atoms_end]):
        coords[i] = np.array([float(i) for i in line.split()[4:7]])
        atoms.append(elements[line.split()[2]])
        atomids.append(line.split()[2])
    return atomids, atoms, coords


def get_lammps_data_lines(coordinates, atoms, startid=1401):
    dataformat = '    %4i      444        %s     0.00000   %3.5f   %3.5f   %3.5f\n'
    lines = []
    for idx, (atm, cor) in enumerate(zip(atoms, coordinates)):
        lines.append(dataformat % (startid + idx, atm, cor[0], cor[1], cor[2]))
    return lines


def change_coordinates(datafile, newfile, newlines, skip_atoms=1400):
    """ Change coordinates of the molecule in the data file. """
    with open(datafile, 'r') as f:
        datalines = f.readlines()
    mol_start = datalines.index('Atoms\n') + skip_atoms + 2
    for i, line in enumerate(newlines):
        datalines[mol_start + i] = line
    with open(newfile, 'w') as nf:
        for line in datalines:
            nf.write(line)


def write_job_file(jobfile, newjobfile, jobname, jobnameindex=2):
    with open(jobfile, 'r') as f:
        joblines = f.readlines()
    joblines[jobnameindex] = '#SBATCH --job-name=%s\n' % jobname
    with open(newjobfile, 'w') as nf:
        for line in joblines:
            nf.write(line)


def write_spring_input(inpfile, newinpfile, SPRING, springindex=48):
    spring_fix = 'fix             SPRNG mol spring tether %.2f %.4f %.4f %s %.2f\n'
    with open(inpfile, 'r') as f:
        lines = f.readlines()
    lines[springindex] = spring_fix % (SPRING['k'], SPRING['xeq'], SPRING['yeq'], SPRING['zeq'], SPRING['r0'])
    with open(newinpfile, 'w') as nf:
        for line in lines:
            nf.write(line)
