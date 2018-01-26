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
# MD simulation setup (LAMMPS) for diffusion

# Decacylene on Cu (110)

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

<table>
  <tr>{% for head in page.box_size.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.box_size.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

# Decacylene on Pd (110)

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
