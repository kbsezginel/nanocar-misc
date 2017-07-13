# Motion of molecules on surfaces

## Pyrene
Initial tests are performed using pyrene molecules since it's relatively small and rigid.

### Force field parameters
Force field parameters for pyrene were based on UFF.
Pyrene has a total of 26 atoms, 29 bonds, 48 angles, 76 dihedrals, 16 impropers. The interaction types used in Lammps, number of interactions and force field parameters for Lammps are given below:

|        | Pair | Bond     | Angle           | Dihedral | Improper |
|--------|------|----------|-----------------|----------|----------|
| Type   | lj   | harmonic | cosine/periodic | harmonic | fourier  |
| Number | 2    | 2        | 2               | 3        | 2        |


```
Pair Coeffs

1 0.105 3.431           # C_R
2 0.044 2.571           # H_b

Bond Coeffs

1 391.670  1.458        # C-C
2 357.440  1.081        # C-H

Angle Coeffs

1 101.627  -1  3        # C-C-C
2  76.818  -1  3        # C-C-H

Dihedral Coeffs

1 1.497  -1  2          # C-C-C-C
2 0.55   -1  2          # C-C-C-H
3 0.30   -1  2          # H-C-C-H

Improper Coeffs

1 2.0 1.0 -1.0 0.0  0   # C C C C
2 2.0 1.0 -1.0 0.0  0   # C C C H
```
