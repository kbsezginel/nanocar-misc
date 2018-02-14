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

Mean Squared Displacement Calculation
-------------------------------------

<p class="collapse">
  <details>
    <summary><b>Click here for calculation details</b></summary>
    <p>MSD is calculated using the <code>compute msd</code> command in Lammps and also using the <a href="https://github.com/kbsezginel/angstrom" target="_blank">Ångström</a> Python package. In Lammps, MSD calculations were done both with and without the center of mass option. You can see the differences in the <a href="/decacylene-si" target="_blank">Supplementary Information</a>. Here, MSD results without using the center of mass option are shown.</p>

    <h3>Lammps MSD vs Calculated MSD</h3>
    <h4>Single Atom vs Grouped Atoms (HtBDC - UFF (FF3) - 5ε)</h4>
    <p>In Lammps you can group atoms and then use the <code>compute msd</code> command to calculate MSD of this group of atoms.
    As a result, Lammps returns a 4 element array of MSD values for x, y, z directions and overall.
    Then, you can also tell at which interval you want to print these MSD values.
    Here, I am showing results for MSD values printed each 1000 timesteps where <code>dt = 0.5 fs</code>.
    The simulations are 2 million timesteps long corresponding to 1 ps.
    Using <a href="https://github.com/kbsezginel/angstrom" target="_blank">Ångström</a> I first convert trajctory coordinates to
    non-periodic coordinates and then calculate MSD for a single atom using the MD trajectory.
    Here is the comparison between Lammps MSD and calculated (Ångström) MSD results.</p>

    <p><img src="assets/img/msd/msd-calc-group.png" alt="msd-calc-group"></p>

    <p>Alternatively, you can also calculate the MSD for a single atom in Lammps.
    Theoretically, as the molecule is relatively small and all atoms are bonded together their MSD should not be too different.
    Here are the resultsd comparing single atom MSD in Lammps and calculated single atom MSD.</p>

    <p><img src="assets/img/msd/msd-calc-single-atom.png" alt="msd-calc-single-atom"></p>

    <p>As seen in figures, the single atom MSD results are more comparable to calculated MSD results, however
    there are still differences. Overall, the curves follow the same trends but the calculated MSD curve
    is much more smooth compared to Lammps results. I am still investigating where this difference is coming from.</p>

    <h4>DC - UFF (FF3) MSD Comparison</h4>
    <p><img src="assets/img/msd/dc-ff3-msd-lammps-vs-calc.png" alt="dc-ff3-msd-lammps-vs-calc"></p>
    <h4>HtBDC - UFF (FF3) MSD Comparison</h4>
    <p><img src="assets/img/msd/htbdc-ff3-msd-lammps-vs-calc.png" alt="htbdc-ff3-msd-lammps-vs-calc"></p>
  </details>
</p>

Experimental Comparison
=======================

<p class="collapse">
  <details>
    <summary><b>Click here for details</b></summary>
    <p><b>Decacylene - UFF (FF3) - Increased Epsilon</b><img src="assets/img/msd/dc-ff3-msd.png" alt="lammps-msd-eqeq"></p>
  </details>
</p>

Diffusivity
===========

<p class="collapse">
  <details>
    <summary><b>Click here for calculation details</b></summary>

    <h3>Linear fitting to MSD vs Time (LAMMPS)</h3>

    <p><img src="assets/img/msd/DC-ff3-lammps-msd-fit.png" alt="DC-ff3-lammps-msd-fit.png"></p>

    <p><img src="assets/img/msd/HtBDC-ff3-lammps-msd-fit.png" alt="HtBDC-ff3-lammps-msd-fit"></p>

    <h3>Linear fitting to MSD vs Time (Angstrom)</h3>

    <p><img src="assets/img/msd/DC-ff3-calc-msd-fit.png" alt="DC-ff3-calc-msd-fit"></p>

    <p><img src="assets/img/msd/HtBDC-ff3-calc-msd-fit.png" alt="HtBDC-ff3-calc-msd-fit"></p>

    <h3>Plotting the slopes (y-axis)</h3>

    <table>
      <tr>
        <th>LAMMPS</th>
        <th>Calculated</th>
      </tr>
      <tr>
        <th><img src="assets/img/msd/ff3-lammps-msd-diffusivity.png" alt="ff3-lammps-msd-diffusivity"></th>
        <th><img src="assets/img/msd/ff3-calc-msd-diffusivity.png" alt="ff3-calc-msd-diffusivity"></th>
      </tr>
    </table>

  </details>
</p>
