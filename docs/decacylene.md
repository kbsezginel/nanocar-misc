---
ff_comparison:
  headers: ['FF1', 'FF2 (EQeq)', 'FF3 (5ε)']
  links:
    - assets/img/msd/traj-ff1.gif
    - assets/img/msd/traj-eqeq.gif
    - assets/img/msd/ff3-5eps.gif
ff3:
  headers: ['2ε', '3ε', '4ε', '5ε', '7.5ε', '10ε']
  links:
    - assets/img/msd/ff3-2eps.gif
    - assets/img/msd/ff3-3eps.gif
    - assets/img/msd/ff3-4eps.gif
    - assets/img/msd/ff3-5eps.gif
    - assets/img/msd/ff3-7.5eps.gif
    - assets/img/msd/ff3-10eps.gif
---
<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>

MD simulations (LAMMPS) of Decacylene and Hexa-*tert*-butyl-Decacylene
======================================================================
<p class="collapse">
  <details open>
    <summary><strong>Show molecules</strong></summary>
    <table>
      <tr>
        <th>DC</th>
        <th>HtBDC</th>
      </tr>
      <tr>
        <th>
          <div style="height: 300px; width: 300px;"
            class='viewer_3Dmoljs' data-datatype='xyz'
            data-backgroundcolor='0xffffff'
            data-href='assets/mol/DC-single.xyz'
            data-style='stick'>
          </div>
        </th>
        <th>
          <div style="height: 300px; width: 300px;"
            class='viewer_3Dmoljs' data-datatype='xyz'
            data-backgroundcolor='0xffffff'
            data-href='assets/mol/HtBDC-single.xyz'
            data-style='stick'>
          </div>
        </th>
      </tr>
    </table>
  </details>
</p>

Structure generation
====================

The molecules are placed on a Cu(110) slab. The metal slab is generated using a replication of `10 x 15 x 5` parallel to *xy-plane*.
The molecules are then aligned to *xy-plane* and placed `5 Å` above the slab in the *z-direction*.
Fixing *z-length* of the box at `50 Å`, the simulation boxes have a size of `39.08 Å x 41.45 Å x 50.0 Å`.

<p class="collapse">
  <details>
    <summary>
      <strong>Click here for interactive structures</strong>
    </summary>
    <table>
      <tr>
        <th>DC</th>
        <th>HtBDC</th>
      </tr>
      <tr>
        <th>
          <div style="height: 300px; width: 300px;"
            class='viewer_3Dmoljs' data-datatype='xyz'
            data-backgroundcolor='0xffffff'
            data-href='assets/mol/DC_Cu110.xyz'
            data-style='stick'>
          </div>
        </th>
        <th>
          <div style="height: 300px; width: 300px;"
            class='viewer_3Dmoljs' data-datatype='xyz'
            data-backgroundcolor='0xffffff'
            data-href='assets/mol/HtBDC_Cu110.xyz'
            data-style='stick'>
          </div>
        </th>
      </tr>
    </table>
  </details>
</p>

Simulation setup
================

The motion of the molecules on Cu(110) surface is investigated by Molecular Dynamcis simulations using LAMMPS.
Initially effect of force field is investigated.

<h2>Universal Force Field</h2>

Different configurations are tested using the universal force field:
-   <b>FF1:</b> UFF with no-charges
-   <b>FF2:</b> UFF with EQeq partial charges
-   <b>FF3:</b> UFF with no-charges but increased pairwise interactions

<h3>Force field comparison</h3>

  <table>
    <tr>{% for head in page.ff_comparison.headers %}<th>{{ head }}</th>{% endfor %}</tr>
    <tr>
      {% for link in page.ff_comparison.links %}
        <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
      {% endfor %}
    </tr>
  </table>

<p class="collapse">
  <details><summary><b>More information</b></summary>
  <h3>EQeq</h3>
  <p>Charge assignment is done using the EQeq code with the above configuration (DC .5 nm above Cu110 slab).</p>

  <b>Cu110 Charge Distribution</b>
  <p><img src="assets/img/msd/Cu110-charge.png" alt="Cu110-charge"></p>

  <b>DC Charge Distribution</b>
  <p><img src="assets/img/msd/DC-charge.png" alt="Cu110-charge"></p>

  <p>As seen above the surface and DC are assigned positive and negative overall charges. Moreover, the charge distribution of the surface is localized to molecule's initial configuration. These cause the molecule to strongly <i>stick</i> on the surface and not diffuse.</p>

  <p>The partial charges can be calculated separately for the surface and the molecule to avoid localized charge distribution. Moreover, a polarizable force field could be used to approximate local charge
  deviations of the surface atoms.</p>

  <h3>FF3</h3>
  <p>In <b>FF3</b> the pairwise interaction parameters between <i>Decacylene</i> and <i>Cu110</i> surface are varied. Here is how a change in <i>ε</i> parameter of the <i>Lennard-Jones</i> potential effects pairwise energy during simulation.</p>

  <p><img src="assets/img/msd/ff3-vdw.png" alt="Cu110-charge"></p>

  <p>With increasing <i>ε</i> for <i>Cu-C</i> and <i>Cu-H</i> interactions the total Van der Waals energy is decreased resulting in increased attractive forces between <i>Decacylene</i> and <i>Cu110</i>.</p>
  <p>Here are the MD trajectories with increasing epsilon:</p>
  <table>
    <tr>{% for head in page.ff3.headers %}<th>{{ head }}</th>{% endfor %}</tr>
    <tr>
      {% for link in page.ff3.links %}
        <th><a href="{{ link }}"><img src="{{ link }}"></a></th>
      {% endfor %}
    </tr>
  </table>
  </details>
</p>

<h2>UFF4MOF</h2>

Mean Squared Displacement (MSD)
===============================

### Lammps MSD
MSD is calculated using `compute msd` command in Lammps and also using []() library. In Lammps both 
The dark red data is generated using `com yes` option to use center of mass for decacylene. The light red data is without using the center of mass but averaging each atom in decacylene.

**Without charges - FF1**
<p><img src="assets/img/msd/lammps-msd.png" alt="lammps-msd"></p>

**With EQeq charges - FF2**
<p><img src="assets/img/msd/lammps-msd-eqeq.png" alt="lammps-msd-eqeq"></p>

**Increased Epsilon - FF3**
<p><img src="assets/img/msd/dc-ff3-msd.png" alt="lammps-msd-eqeq"></p>




Mean Squared Displacement Calculation
-------------------------------------

<p><img src="assets/img/msd/msd-calc-single-atom.png" alt="msd-calc-single-atom"></p>

<p><img src="assets/img/msd/msd-calc-group.png" alt="msd-calc-group"></p>

### LAMMPS MSD ve Calculated (Angstrom)

#### DC
<p><img src="assets/img/msd/dc-ff3-msd-lammps-vs-calc.png" alt="dc-ff3-msd-lammps-vs-calc"></p>

#### HtBDC
<p><img src="assets/img/msd/htbdc-ff3-msd-lammps-vs-calc.png" alt="htbdc-ff3-msd-lammps-vs-calc"></p>

Diffusivity
-----------

### Linear fitting to MSD vs Time (LAMMPS)

<p><img src="assets/img/msd/DC-ff3-lammps-msd-fit.png" alt="DC-ff3-lammps-msd-fit.png"></p>

<p><img src="assets/img/msd/HtBDC-ff3-lammps-msd-fit.png" alt="HtBDC-ff3-lammps-msd-fit"></p>

### Linear fitting to MSD vs Time (Angstrom)

<p><img src="assets/img/msd/DC-ff3-calc-msd-fit.png" alt="DC-ff3-calc-msd-fit"></p>

<p><img src="assets/img/msd/HtBDC-ff3-calc-msd-fit.png" alt="HtBDC-ff3-calc-msd-fit"></p>

### Plotting the slopes (y-axis)

<table>
<tr>
<th>LAMMPS</th>
<th>Calculated</th>
</tr>
<tr>
<th><img src="assets/img/msd/ff3-lammps-msd-diffusivity.png" alt="ff3-lammps-msd-diffusivity">
</th>
<th><img src="assets/img/msd/ff3-calc-msd-diffusivity.png" alt="ff3-calc-msd-diffusivity">
</th>
</tr>
</table>
