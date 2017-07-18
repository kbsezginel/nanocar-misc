# Pyrene on rigid wall
Pyrene motion on rigid wall with Lennard-Jones parameters.

## Setup
The simulation box is by default a cube centered on `0, 0, 0` with `2 nm` sides. Periodic boundary conditions are applied in each direction.

The pyrene and wall are both are on the `xy` plane. Wall is at the bottom edge of the simulation box acting as a floor. Pyrene is at the middle of the simulation box at `z = 0`.

### Box size
The box size is changed between `1.5 - 5 nm` in different dimensions as follows.

| Case | xlo         | xhi       | ylo         | yhi       | zlo         | zhi       |
|------|-------------|-----------|-------------|-----------|-------------|-----------|
| 1    | -7.5 to -25 | 7.5 to 25 | -7.5 to -25 | 7.5 to 25 | -7.5 to -25 | 7.5 to 25 |
| 2    | -10         | 5 to 40   | -10         | 5 to 40   | -10         | 5 to 40   |
| 3    | -10         | 10        | -10         | 10        | -7.5 to -25 | 7.5 to 25 |
| 4    | -10         | 10        | -10         | 10        | -10         | 5 to 40   |
| 5    | -7.5 to -25 | 7.5 to 25 | -7.5 to -25 | 7.5 to 25 | -10         | 10        |

### MSD
Using the output trajectories position of the pyrene center of mass is calculated for each frame. Then mean square displacement is calculated for each direction using the equation below:

<p align="center"> <img src="https://goo.gl/yJTrbK" width="40%"> </p>

where:
- *N* : number of frames
- *p(t<sub>i</sub>)* : position at i<sup>th</sup> frame
- *p(t<sub>i - 1</sub>)* : position at i - 1<sup>th</sup> frame

#### Case 1 (center)
In this case, pyrene is positioned in the middle of the box and box size is enlarged in 3 dimensions from 1.5 nm to 5 nm.
<p align="center"> <img src="https://goo.gl/Aty3fC" width="50%"> </p>

Mean squared displacement:

![alt_text][boxsize-center-MSD]

#### Case 2 (floor)
In this case, pyrene is positioned 1 nm above the floor (z-dimension) and box size is enlarged in 3 dimensions from 1.5 nm to 5 nm.
<p align="center"> <img src="https://goo.gl/4USDfS" width="50%"> </p>

Mean squared displacement is ca(blue data points represent runs where simulations were not completed):

![alt_text][boxsize-floor-MSD]

#### Case 3 (z-center)
<p align="center"> <img src="https://goo.gl/gtbnKe" width="50%"> </p>

**MSD**

![alt_text][boxsize-z-center-MSD]

#### Case 4 (z-floor)
<p align="center"> <img src="https://goo.gl/eqg8Hx" width="50%"> </p>

**MSD**

![alt_text][boxsize-z-floor-MSD]

#### Case 5 (xy-center)
<p align="center"> <img src="https://goo.gl/iK6ZkM" width="50%"> </p>

**MSD**

![alt_text][boxsize-xy-center-MSD]

### Wall force field parameters
Defaults force field parameters for wall are:

`epsilon: 0.0005 ADD_UNITS sigma: 4.0 Å cutoff: 10 Å`

#### Pyrene wall distance
The distance between pyrene and wall in `z` axis are changes between `5 - 60 Å`.

----------------------------------------------------------------------
[boxsize-center-MSD]: https://goo.gl/26ED6T
[boxsize-floor-MSD]: https://goo.gl/jde7SG
[boxsize-z-center-MSD]: https://goo.gl/rwWkNr
[boxsize-z-floor-MSD]: https://goo.gl/xikSNn
[boxsize-xy-center-MSD]: https://goo.gl/miwq7x
