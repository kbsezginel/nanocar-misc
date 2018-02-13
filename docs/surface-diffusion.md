<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>

Calculating molecular diffusion on a surface
============================================

Before studying motion of nanocars on surfaces it's a good idea to start with simpler molecules and
try replicating experimental results. There aren't many studies measuring single molecule diffusion
of *larger* molecules, however, I was able to identify the following three studies which I will
use as anchor points for the computational setup.

Experimental Diffusion Results
------------------------------

> Table 1: Diffusion parameters (activation energy, hopping rate and diffusion coefficient) extracted from experimental surface diffusion studies. See below for molecular structures.

<table>
  <tr>
    <th>Molecule</th>
    <th>Surface</th>
    <th><i>E<sub>d</sub></i> (eV)</th>
    <th><i>h<sub>0</sub></i> (s<sup>-1</sup>)</th>
    <th><i>D<sub>0</sub></i> (cm<sup>2</sup>/s)</th>
    <th>Ref</th>
  </tr>
  <tr>
    <td>DC</td>
    <td>Cu(1 1 0)</td>
    <td>0.74 ± 0.03 (hop)</td>
    <td>10<sup>13.9 ± 0.7</sup></td>
    <td>10<sup>-1.0 ± 1.0</sup></td>
    <th><a href="https://doi.org/10.1103/PhysRevLett.88.156102">1</a></th>
  </tr>
  <tr>
    <td>HtBDC</td>
    <td>Cu(1 1 0)</td>
    <td>0.57 ± 0.02 (hop)</td>
    <td>10<sup>13.5 ± 0.4</sup></td>
    <td>10<sup>0.9 ± 1.0</sup></td>
    <th><a href="https://doi.org/10.1103/PhysRevLett.88.156102">1</a></th>
  </tr>
  <tr>
    <td>PVBA</td>
    <td>Pd(1 1 0)</td>
    <td>0.83 ± 0.03 </td>
    <td>10<sup>10.3 ± 0.4</sup></td>
    <td> - </td>
    <th><a href="https://doi.org/10.1063/1.478430">2</a></th>
  </tr>
  <tr>
    <td>C<sub>60</sub></td>
    <td>Pd(1 1 0)</td>
    <td>1.40 ± 0.20</td>
    <td>10<sup>14.4 ± 0.4</sup></td>
    <td> - </td>
    <th><a href="https://doi.org/10.1103/PhysRevB.64.161403">3</a></th>
  </tr>
  <tr>
    <td>DNHD</td>
    <td>Cu(1 1 0)</td>
    <td>0.195</td>
    <td> - </td>
    <td> - </td>
    <th><a href="https://doi.org/10.1063/1.4811353">4</a></th>
  </tr>
  <tr>
    <td>TPEE</td>
    <td>Cu(1 1 0)</td>
    <td>0.175</td>
    <td> - </td>
    <td> - </td>
    <th><a href="https://doi.org/10.1063/1.4811353">4</a></th>
  </tr>
  <tr>
    <td>BtPHD</td>
    <td>Cu(1 1 0)</td>
    <td>0.325</td>
    <td> - </td>
    <td> - </td>
    <th><a href="https://doi.org/10.1063/1.4811353">4</a></th>
  </tr>
</table>

Molecules
---------

<p>
  <details>
    <summary>
      <strong>1. Schnunack et al. Phys. Rev. Lett. 88, 156102 (2002)</strong>
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

<p>
  <details>
    <summary>
      <strong>2. Weckesser et al. J. Chem. Phys., Vol. 110, No. 11, 15 (1999)</strong>
    </summary>
    <h4>PVBA</h4>
    <iframe style="width: 500px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=balls&cid=12006311&bg=white">
    </iframe>
  </details>
</p>

<p>
  <details>
    <summary>
      <strong>3. Weckesser et al. Phys. Rev. B 64, 161403 (2001)</strong>
    </summary>
    <h4>C60</h4>
    <div style="height: 300px; width: 500px;"
      class='viewer_3Dmoljs' data-datatype='xyz'
      data-backgroundcolor='0xffffff'
      data-href='assets/mol/C60-Ih.xyz'
      data-style='stick'>
    </div>
  </details>
</p>

<p>
  <details>
    <summary>
      <strong>4. Sun et al. Appl. Phys. Lett. 103, 013103 (2013)</strong>
    </summary>
    <table>
      <tr>
        <th>DNHD</th>
        <th>TPEE</th>
        <th>BtPHD</th>
      </tr>
      <tr>
        <th>
          <iframe style="width: 200px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=balls&cid=102492682&bg=white">
          </iframe>
        </th>
        <th>
          <iframe style="width: 200px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=balls&smiles=C12C=C(C%23C/C(/C%23CC3=CC4C=CC=CC=4C=C3)=C(/C%23CC3=CC=C4C=CC=CC4=C3)\C%23CC3=CC4C=CC=CC=4C=C3)C=CC=1C=CC=C2&bg=white">
          </iframe>
        </th>
        <th>
          <iframe style="width: 200px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=balls&cid=102418850&bg=white">
          </iframe>
        </th>
      </tr>
    </table>
  </details>
</p>

Surfaces
--------

The metal surfaces considered here are constructured using [ASE](https://wiki.fysik.dtu.dk/ase/).
Take a look at the [Jupyter Notebook](https://github.com/kbsezginel/Nanocar/blob/master/molecules/surfaces/metal-surfaces.ipynb) for more info.

### Copper (110) | COD: 9011604

```
Space Group: 	F m -3 m | (a, b, c): 3.597 Å | (α, β, γ): 90°
```

### Palladium (110) | COD: 1011110

```
Space Group: 	F m -3 m | (a, b, c): 3.908 Å | (α, β, γ): 90°
```
