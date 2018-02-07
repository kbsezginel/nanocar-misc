---
box_periodicity:
  headers: ['ppp', 'ppf']
  links:
  - assets/img/DC_Cu110/DC_Cu110_ppp.gif
  - assets/img/DC_Cu110/DC_Cu110_ppf.gif
temperature:
  headers: ['150 K', '175 K', '200 K', '225 K', '250 K']
  links:
  - assets/img/DC_Cu110/DC_Cu110_ppp_T150.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T175.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T200.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T225.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_T250.gif
box_size:
  headers: ['2 nm', '3 nm', '4 nm', '5 nm']
  links:
  - assets/img/DC_Cu110/DC_Cu110_ppp_z20.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_z30.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_z40.gif
  - assets/img/DC_Cu110/DC_Cu110_ppp_z50.gif
---
MD simulations (LAMMPS) for diffusion of Decacylene
===================================================

Decacylene (DC) on Cu (110)
----------------------

The metal slab is generated using a replication of `10 x 15 x 5` parallel to *xy-plane*.
The decacylene is then aligned to *xy-plane* and placed `5 Å` above the slab in *z-direction*.
Fixing *z-length* of the box at `50 Å`, the simulation box has a size of `39.08 Å x 41.45 Å x 50.0 Å`.

<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>

<div style="height: 400px; width: 600px;"
  class='viewer_3Dmoljs' data-datatype='xyz'
  data-backgroundcolor='0xffffff'
  data-href='assets/mol/DC_Cu110.xyz'
  data-style='stick'>
</div>

Force field
-----------
Different force fields are tested for the above setup.
1. UFF with no-charges
2. UFF with EQeq

### EQeq
Charge assignment is done using the EQeq code with the above configuration (DC .5 nm above Cu110 slab).

**Cu110 Charge Distribution**
<p><img src="assets/img/msd/Cu110-charge.png" alt="Cu110-charge"></p>

**DC Charge Distribution**
<p><img src="assets/img/msd/DC-charge.png" alt="Cu110-charge"></p>

Mean Squared Displacement (MSD)
-------------------------------

### Lammps MSD
MSD is calculated using `compute msd` command in Lammps.
The dark red data is generated using `com yes` option to use center of mass for decacylene. The light red data is without using the center of mass but averaging each atom in decacylene.

**Without charges - FF1**
<p><img src="assets/img/msd/lammps-msd.png" alt="lammps-msd"></p>


**With EQeq charges - FF2**
<p><img src="assets/img/msd/lammps-msd-eqeq.png" alt="lammps-msd-eqeq"></p>

### Green-Kubo
Here Green-Kubo approximation is used.

**Without charges - FF1**
<p><img src="assets/img/msd/green-kubo.png" alt="green-kubo"></p>


**With EQeq charges - FF2**
<p><img src="assets/img/msd/green-kubo-eqeq.png" alt="green-kubo-eqeq"></p>


### Tests
-   Periodic vs non-periodic *z-direction*
-   Temperature
-   Box size
-   Decacylene - slab distance

## Box Periodicity

<table><tr>{% for head in page.box_periodicity.headers %}<th>{{ head }}</th>{% endfor %}</tr>
<tr>{% for link in page.box_periodicity.links %}<th><a href="{{ link }}">
<img src="{{ link }}"></a></th>{% endfor %}</tr></table>

### Temperature

<table>
  <tr>{% for head in page.temperature.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.temperature.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

### Box size

#### *z-direction*

<table>
  <tr>{% for head in page.box_size.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.box_size.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

#### *xy-plane*

<table>
  <tr>{% for head in page.box_size.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.box_size.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>
