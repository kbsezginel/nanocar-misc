# Pyrene on rigid wall
Pyrene motion on rigid wall with Lennard-Jones parameters.

## Setup
The simulation box is by default a cube centered on `0, 0, 0` with `2 nm` sides. Periodic boundary conditions are applied in each direction.

The pyrene and wall are both are on the `xy` plane. Wall is at the bottom edge of the simulation box acting as a floor. Pyrene is at the middle of the simulation box at `z = 0`.

#### Box size
 The box size is changed between `1.5 - 5 nm`.

#### Wall force field parameters
Defaults force field parameters for wall are:

`epsilon: 0.0005 ADD_UNITS sigma: 4.0 Å cutoff: 10 Å`

#### Pyrene wall distance
The distance between pyrene and wall in `z` axis are changes between `5 - 60 Å`.
