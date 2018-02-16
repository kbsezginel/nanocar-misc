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
Force field parameters
----------------------

<table>
  <tr>
    <th>Force Field</th>
    <th colspan="2" style="text-align:center">Cu</th>
    <th colspan="2" style="text-align:center">C</th>
    <th colspan="2" style="text-align:center">H</th>
  </tr>
  <tr>
    <th>LJ</th>
    <th>ε (kcal/mol)</th>
    <th>σ (Å)</th>
    <th>ε (kcal/mol)</th>
    <th>σ (Å)</th>
    <th>ε (kcal/mol)</th>
    <th>σ (Å)</th>
  </tr>
  <tr>
    <th>UFF</th>
    <td>0.005000</td>
    <td>3.113691</td>
    <td>0.105000</td>
    <td>3.430851</td>
    <td>0.044000</td>
    <td>2.571134</td>
  </tr>
  <tr>
    <th>DRE</th>
    <td>0.055000</td>
    <td>4.044680</td>
    <td>0.095100</td>
    <td>3.472990</td>
    <td>0.015200</td>
    <td>2.846421</td>
  </tr>
</table>

Decacylene - UFF
----------------
<p><img src="assets/img/decacylene/DC-UFF-MSD-vs-time.png" alt="dc-uff-msd"></p>

<p><b>Diffusion Coefficient</b><img src="assets/img/decacylene/DC-UFF-D0-vs-eps.png" alt="dc-uff-d0"></p>

Decacylene - DRE
----------------
<p><img src="assets/img/decacylene/DC-DRE-MSD-vs-time.png" alt="dc-dre-msd"></p>

<p><b>Diffusion Coefficient</b><img src="assets/img/decacylene/DC-DRE-D0-vs-eps.png" alt="dc-dre-d0"></p>

HtBDC - UFF
-----------
<p><img src="assets/img/decacylene/HtBDC-UFF-MSD-vs-time.png" alt="htbdc-uff-msd"></p>

<p><b>Diffusion Coefficient</b><img src="assets/img/decacylene/HtBDC-UFF-D0-vs-eps.png" alt="htbdc-uff-d0"></p>

HtBDC - DRE
-----------
<p><img src="assets/img/decacylene/HtBDC-DRE-MSD-vs-time.png" alt="htbdc-dre-msd"></p>

<p><b>Diffusion Coefficient</b><img src="assets/img/decacylene/HtBDC-DRE-D0-vs-eps.png" alt="htbdc-dre-d0"></p>


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

### DC - UFF - Green-Kubo
Here Green-Kubo approximation is used.

**Without charges - FF1**
<p><img src="assets/img/msd/green-kubo.png" alt="green-kubo"></p>


**With EQeq charges - FF2**
<p><img src="assets/img/msd/green-kubo-eqeq.png" alt="green-kubo-eqeq"></p>

**Increased Epsilon - FF3**
<p><img src="assets/img/msd/gk-ff3-2eps.png" alt="lammps-msd-eqeq"></p>
<p><img src="assets/img/msd/gk-ff3-3eps.png" alt="lammps-msd-eqeq"></p>
<p><img src="assets/img/msd/gk-ff3-4eps.png" alt="lammps-msd-eqeq"></p>
<p><img src="assets/img/msd/gk-ff3-5eps.png" alt="lammps-msd-eqeq"></p>
<p><img src="assets/img/msd/gk-ff3-7.5eps.png" alt="lammps-msd-eqeq"></p>
<p><img src="assets/img/msd/gk-ff3-10eps.png" alt="lammps-msd-eqeq"></p>

<p><img src="assets/img/msd/gk-ff3-all.png" alt="lammps-msd-eqeq"></p>

### DC - UFF (FF3) - Effect of Sigma

<p><img src="assets/img/msd/ff3-2sig.png" alt="lammps-msd-eqeq"></p>
<p><img src="assets/img/msd/ff3-2eps2sig.png" alt="lammps-msd-eqeq"></p>

<table>
  <tr>{% for head in page.ff3_sig.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.ff3_sig.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

### DC vs HtBDC - UFF (FF3) - MSD Comparison by direction

<p><b>x</b><img src="assets/img/msd/ff3-msd-both-x.png" alt="ff3-msd-both-x"></p>
<p><b>y</b><img src="assets/img/msd/ff3-msd-both-y.png" alt="ff3-msd-both-y"></p>
<p><b>z</b><img src="assets/img/msd/ff3-msd-both-z.png" alt="ff3-msd-both-z"></p>
<p><b>all</b><img src="assets/img/msd/ff3-msd-both-all.png" alt="ff3-msd-both-all"></p>

### DC - UFF - LAMMPS MSD CoM vs No CoM

The dark red data is generated using `com yes` option to use center of mass for decacylene. The light red data is without using the center of mass but averaging each atom in decacylene.

**Without charges - FF1**
<p><img src="assets/img/msd/lammps-msd.png" alt="lammps-msd"></p>

**With EQeq charges - FF2**
<p><img src="assets/img/msd/lammps-msd-eqeq.png" alt="lammps-msd-eqeq"></p>

**Increased Epsilon - FF3**
<p><img src="assets/img/msd/dc-ff3-msd.png" alt="lammps-msd-eqeq"></p>
