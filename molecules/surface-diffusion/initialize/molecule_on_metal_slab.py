"""
Place given molecules on a metal slab parallel to xy-plane.
Molecule information is read from molecules.yaml and surface nformation is read from surfaces.yaml.
- A metal slab is generated parallel to xy-plane acoording to info given in surfaces.yaml.
- The molecule is aligned to xy-plane by two given vectors.
- The vectors are determined from two given atoms for each vector to be aligned to x and y axes.
- The molecule is placed <distance_from_surface> A above the metal slab.
- xyz, cif, and Lammps files are generated.
"""
import os
import ase
import yaml
from ase.build import fcc110
from moleidoscope.linker import Linker
from moleidoscope.geo.vector import align
from xyz2cif import write_cif
from thermof import Simulation
from thermof import Parameters


####################################################################################################
metal = 'Cu'                  # Metal atom
z_box = 50                    # Length of simulation box in z-direction (A)
distance_from_surface = 5     # Distance btw molecule and surface (A)
force_field = 'UFF'           # Force field for Lammps
mol_dir = '/home/kutay/Documents/git/Nanocar/molecules/surface-diffusion/opt'
save_dir = '/home/kutay/Documents/git/Nanocar/molecules/surface-diffusion/initialize/lammps'
####################################################################################################


def ase_to_linker(ase_atoms):
    """ Convert ASE atoms object to Moleidoscope linker object """
    mol = Linker()
    mol.atom_names = list(ase_atoms.get_chemical_symbols())
    mol.atom_coors = list(ase_atoms.get_positions())
    return mol


def read_yaml(yaml_file):
    with open(yaml_file, 'r') as yf:
        data = yaml.load(yf)
    return data


molecules_info = read_yaml('molecules.yaml')
surfaces_info = read_yaml('surfaces.yaml')

surf = surfaces_info[metal]
for molecule in molecules_info.keys():
    mol = molecules_info[molecule]

    # Create metal slab
    ase_slab = fcc110(metal, a=surf['a'], size=surf['size'], vacuum=surf['vacuum'])
    l_slab = ase_to_linker(ase_slab)
    print(ase_slab.cell)
    print(len(ase_slab.get_chemical_symbols()), 'atoms')

    # Align molecule to xyz plane
    l_mol = Linker(read=os.path.join(mol_dir, '%s.xyz' % molecule))
    l_mol.vector = l_mol.get_vector(mol['x'][0], mol['x'][1])
    l_mol = l_mol.align([1, 0, 0])
    l_mol.center([0, 0, 0])
    l_mol.vector = l_mol.get_vector(mol['y'][0], mol['y'][1])
    l_mol = l_mol.align([0, 1, 0])
    l_mol.center([0, 0, 0])

    # Place molecule on slab
    # The min z coordinate of molecule, used to make sure molecule is 5 A away from surface
    mol_z_dist = min([i[2] for i in l_mol.atom_coors])
    slab_center = l_slab.get_center()
    l_mol.center(slab_center)
    l_mol.translate([0, 0, distance_from_surface + ase_slab.cell[2][2] / 2 - mol_z_dist])
    mol_slab = l_slab.join(l_mol)

    # Save xyz file
    mol_slab.name = '%s_%s110' % (molecule, metal)
    mol_slab.save(file_format='xyz', save_dir=save_dir)

    # Save cif file
    sim_box = [ase_slab.cell[0][0], ase_slab.cell[1][1], z_box, 90, 90, 90]
    cif_file = os.path.join(save_dir, '%s_%s.cif') % (mol_slab.name, force_field)
    write_cif(cif_file, mol_slab.atom_names, mol_slab.atom_coors, header=cif_file, cell=sim_box, fractional=True)

    # Write Lammps files
    simpar = Parameters()
    sim = Simulation(mof=cif_file, parameters=simpar)
    mof_name = os.path.splitext(os.path.basename(cif_file))[0]
    sim.simdir = os.path.join(os.path.dirname(cif_file), mof_name)

    sim.parameters.lammps['force_field'] = force_field
    sim.parameters.lammps['mol_ff'] = force_field
    sim.parameters.thermof['fix'] = ['NVT', 'NVE']
    sim.parameters.thermof['temperature'] = 200
    sim.parameters.thermof['thermo_style'] = ['step', 'temp', 'press', 'pe', 'etotal', 'epair', 'emol', 'evdwl']
    sim.parameters.job['scheduler'] = 'slurm'
    sim.parameters.job['cluster'] = 'smp'
    sim.parameters.job['nodes'] = 1
    sim.parameters.job['ppn'] = 24

    sim.initialize()
