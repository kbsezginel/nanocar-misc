---
ff_comparison:
  headers: ['FF1', 'FF2 (EQeq)', 'FF3 (5ε)']
  links:
    - assets/img/msd/traj-ff1.gif
    - assets/img/msd/traj-eqeq.gif
    - assets/img/msd/ff3-5eps.gif
ff3_eps:
  headers: ['1σ', '2σ', '4ε', '10ε']
  links:
    - assets/img/msd/traj-ff1.gif
    - assets/img/msd/ff3-2eps.gif
    - assets/img/msd/ff3-4eps.gif
    - assets/img/msd/ff3-10eps.gif
ff3:
  headers: ['2ε', '3ε', '4ε', '5ε', '7.5ε', '10ε']
  links:
    - assets/img/msd/ff3-2eps.gif
    - assets/img/msd/ff3-3eps.gif
    - assets/img/msd/ff3-4eps.gif
    - assets/img/msd/ff3-5eps.gif
    - assets/img/msd/ff3-7.5eps.gif
    - assets/img/msd/ff3-10eps.gif
ff3_sig:
  headers: ['2σ', '2ε2σ']
  links:
    - assets/img/msd/ff3-2sig.gif
    - assets/img/msd/ff3-2eps2sig.gif
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
-   **FF1:** UFF with no-charges
-   **FF2:** UFF with EQeq
-   **FF3:** UFF with no-charges but increased pairwise interactions

###  Force field comparison

<table>
  <tr>{% for head in page.ff_comparison.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.ff_comparison.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

### EQeq
Charge assignment is done using the EQeq code with the above configuration (DC .5 nm above Cu110 slab).

**Cu110 Charge Distribution**
<p><img src="assets/img/msd/Cu110-charge.png" alt="Cu110-charge"></p>

**DC Charge Distribution**
<p><img src="assets/img/msd/DC-charge.png" alt="Cu110-charge"></p>

### FF3
In **FF3** the pairwise interaction parameters between *Decacylene* and *Cu110* surface are varied. Here is how a change in *ε* parameter of the *Lennard-Jones*
potential effects pairwise energy during simulation.

<p><img src="assets/img/msd/ff3-vdw.png" alt="Cu110-charge"></p>

With increasing *ε* for *Cu-C* and *Cu-H* interactions the total Van der Waals energy is decreased resulting in increased attractive forces between *Decacylene* and *Cu110*.

Mean Squared Displacement (MSD)
-------------------------------

### Lammps MSD
MSD is calculated using `compute msd` command in Lammps.
The dark red data is generated using `com yes` option to use center of mass for decacylene. The light red data is without using the center of mass but averaging each atom in decacylene.

**Without charges - FF1**
<p><img src="assets/img/msd/lammps-msd.png" alt="lammps-msd"></p>


**With EQeq charges - FF2**
<p><img src="assets/img/msd/lammps-msd-eqeq.png" alt="lammps-msd-eqeq"></p>

**Increased Epsilon - FF3**
<p><img src="assets/img/msd/dc-ff3-msd.png" alt="lammps-msd-eqeq"></p>


### Green-Kubo
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

### FF3 - Effect of Epsilon

<table>
  <tr>{% for head in page.ff3_eps.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.ff3_eps.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>

**Decacylene:**

<p><img src="assets/img/msd/htbdc-ff3-msd.png" alt="lammps-msd-eqeq"></p>

### FF3 - Effect of Sigma

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

### All Epsilon

<table>
  <tr>{% for head in page.ff3.headers %}<th>{{ head }}</th>{% endfor %}</tr>
  <tr>
    {% for link in page.ff3.links %}
      <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
    {% endfor %}
  </tr>
</table>


### Molecule comparison

#### x
<p><img src="assets/img/msd/ff3-msd-both-x.png" alt="ff3-msd-both-x"></p>

#### y
<p><img src="assets/img/msd/ff3-msd-both-y.png" alt="ff3-msd-both-y"></p>

#### z
<p><img src="assets/img/msd/ff3-msd-both-z.png" alt="ff3-msd-both-z"></p>

#### all
<p><img src="assets/img/msd/ff3-msd-both-all.png" alt="ff3-msd-both-all"></p>
