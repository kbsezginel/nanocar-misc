# MD simulation setup (LAMMPS) for diffusion

## Decacylene on Pd (110)

The metal slab is generated using a replication of `10 x 15 x 5` parallel to *xy-plane*.
The decacylene is then aligned to *xy-plane* and placed `5 Å` above the slab in *z-direction*.
Leaving additional `~5 Å` above decacylene the simulation box has a size of `35.97 Å x 38.152 Å x 20.087 Å`.

### Tests
-   Periodic vs non-periodic *z-direction*
-   Temperature
-   Box size
-   Decacylene - slab distance


<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>

<div style="height: 300px; width: 500px;"
  class='viewer_3Dmoljs' data-datatype='xyz'
  data-backgroundcolor='0xffffff'
  data-href='assets/mol/Pd110_DC.xyz'
  data-style='stick'>
</div>

### Box size

#### 2 nm
<p align="center"> <img src="assets/img/dc-pd110-z20.gif" width="100%"> </p>

#### 3 nm
<p align="center"> <img src="assets/img/dc-pd110-z30.gif" width="100%"> </p>

#### 4 nm
<p align="center"> <img src="assets/img/dc-pd110-z40.gif" width="100%"> </p>

#### 5 nm
<p align="center"> <img src="assets/img/dc-pd110-z50.gif" width="100%"> </p>

#### Displacement

<p align="center"> <img src="assets/img/dc-pd110-boxsize.png" width="100%"> </p>

# Decacylene on Cu (110)

## Periodic box

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp.gif" width="100%"> </p>

### Temperature

#### 150 K

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_T150.gif" width="100%"> </p>

#### 175 K

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_T175.gif" width="100%"> </p>

#### 200 K

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_T200.gif" width="100%"> </p>

#### 225 K

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_T225.gif" width="100%"> </p>

#### 250 K

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_T250.gif" width="100%"> </p>

### Box size

#### 2 nm

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_z20.gif" width="100%"> </p>

#### 3 nm

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_z30.gif" width="100%"> </p>

#### 4 nm

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_z40.gif" width="100%"> </p>

#### 5 nm

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppp_z50.gif" width="100%"> </p>

## Non-periodic box in z-direction

<p align="center"> <img src="assets/img/DC_Cu110/DC_Cu100_ppf.gif" width="100%"> </p>
