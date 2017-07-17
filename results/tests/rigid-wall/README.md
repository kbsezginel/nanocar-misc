# Pyrene on rigid wall
Pyrene motion on rigid wall with Lennard-Jones parameters.

## Setup
The simulation box is by default a cube centered on `0, 0, 0` with `2 nm` sides. Periodic boundary conditions are applied in each direction.

The pyrene and wall are both are on the `xy` plane. Wall is at the bottom edge of the simulation box acting as a floor. Pyrene is at the middle of the simulation box at `z = 0`.

### Box size
The box size is changed between `1.5 - 5 nm`.

#### Case 1 (center)
In this case, pyrene is positioned in the middle of the box and box size is enlarged in 3 dimensions from 1.5 nm to 5 nm.

![alt_text][boxsize-center]

Mean squared displacement:

![alt_text][boxsize-center-MSD]

#### Case 2 (floor)
In this case, pyrene is positioned 1 nm above the floor (z-dimension) and box size is enlarged in 3 dimensions from 1.5 nm to 5 nm.

![alt_text][boxsize-floor]

Mean squared displacement:

![alt_text][boxsize-floor-MSD]

### Wall force field parameters
Defaults force field parameters for wall are:

`epsilon: 0.0005 ADD_UNITS sigma: 4.0 Å cutoff: 10 Å`

#### Pyrene wall distance
The distance between pyrene and wall in `z` axis are changes between `5 - 60 Å`.

----------------------------------------------------------------------
[boxsize-floor]: https://goo.gl/4USDfS
[boxsize-center]: https://goo.gl/Aty3fC
[boxsize-center-MSD]: https://goo.gl/jCLo2P
[boxsize-floor-MSD]: https://goo.gl/Kh8DTf
