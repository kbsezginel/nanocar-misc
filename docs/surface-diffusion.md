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
  <tr>
    <td>Violet Lander</td>
    <td>Cu(1 1 0)</td>
    <td> - </td>
    <td> - </td>
    <td>(4.8 ± 0.5) x 10<sup>-17</sup></td>
    <th><a href="https://doi.org/10.1038/nmat1243">5</a></th>
  </tr>
</table>

Computational Diffusion Results
-------------------------------

> Table 2: Diffusion parameters (activation energy, hopping rate and diffusion coefficient) extracted from computational surface diffusion studies. See below for molecular structures.

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
    <td>Carborane</td>
    <td>Au(0 0 1)</td>
    <td> - </td>
    <td> - </td>
    <td> - </td>
    <th><a href="https://doi.org/10.1021/acs.jpcc.6b02201">C1</a></th>
  </tr>
  <tr>
    <td>Violet Lander</td>
    <td>Cu(1 1 0)</td>
    <td> - </td>
    <td> - </td>
    <td>5.6 x 10<sup>-4</sup></td>
    <th><a href="https://doi.org/10.1063/1.3512623">C2</a></th>
  </tr>
</table>

Molecules
---------

<p>
  <details>
    <summary>
      <b>1. Schnunack et al. Phys. Rev. Lett. 88, 156102 (2002)</b>
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
      <b>2. Weckesser et al. J. Chem. Phys., Vol. 110, No. 11, 15 (1999)</b>
    </summary>
    <h4>PVBA</h4>
    <iframe style="width: 500px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=balls&cid=12006311&bg=white">
    </iframe>
  </details>
</p>

<p>
  <details>
    <summary>
      <b>3. Weckesser et al. Phys. Rev. B 64, 161403 (2001)</b>
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
      <b>4. Sun et al. Appl. Phys. Lett. 103, 013103 (2013)</b>
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

<p>
  <details>
    <summary>
      <b>5. Otero et al. Nature Materials, 3, 779-782 (2004)</b>
    </summary>
    <h4>Violet Lander</h4>
    <p><img src="http://aip.scitation.org/na101/home/literatum/publisher/aip/journals/content/jcp/2010/jcp.2010.133.issue-22/1.3512623/production/images/medium/1.3512623.figures.f1.gif"></p>
  </details>
</p>

<p>
  <details>
    <summary>
      <b>C1. Lavasani et al. J. Phys. Chem. C, 120 (26), 14048–14058 (2016)</b>
    </summary>
    <h4>P-carborane</h4>
    <div style="height: 300px; width: 500px;"
      class='viewer_3Dmoljs' data-datatype='xyz'
      data-backgroundcolor='0xffffff'
      data-href='assets/mol/p-carborane.xyz'
      data-style='stick'>
    </div>
  </details>
</p>


Surfaces
--------

The metal surfaces considered here are constructured using [ASE](https://wiki.fysik.dtu.dk/ase/).
Take a look at the [Jupyter Notebook](https://github.comXu, Q., Feng, L., Sha, R., Seeman, N. C., & Chaikin, P. M. (2011). Subdiffusion of a sticky particle on a surface. Physical review letters, 106(22), 228102./kbsezginel/Nanocar/blob/master/molecules/surfaces/metal-surfaces.ipynb) for more info.

### Copper (110) | COD: 9011604

```
Space Group: 	F m -3 m | (a, b, c): 3.597 Å | (α, β, γ): 90°
```

### Palladium (110) | COD: 1011110

```
Space Group: 	F m -3 m | (a, b, c): 3.908 Å | (α, β, γ): 90°
```

Bibliography
------------

[Rosei, F., Schunack, M., Naitoh, Y., Jiang, P., Gourdon, A., Laegsgaard, E., ... & Besenbacher, F. (2003). **Properties of large organic molecules on metal surfaces.** *Progress in Surface Science*, 71(5-8), 95-146.](https://www.sciencedirect.com/science/article/pii/S0079681603000042)

[Rosei, F., Schunack, M., Jiang, P., Gourdon, A., Lægsgaard, E., Stensgaard, I., ... & Besenbacher, F. (2002). **Organic molecules acting as templates on metal surfaces.** *Science*, 296(5566), 328-331.](http://science.sciencemag.org/content/296/5566/328)

[Haq, S., Wit, B., Sang, H., Floris, A., Wang, Y., Wang, J., ... & Raval, R. (2015). **A small molecule walks along a surface between porphyrin fences that are assembled in situ.** *Angewandte Chemie International Edition*, 54(24), 7101-7105.](http://onlinelibrary.wiley.com/doi/10.1002/anie.201502153/full)

[Claytor, K., Khatua, S., Guerrero, J. M., Tcherniak, A., Tour, J. M., & Link, S. (2009). **Accurately determining single molecule trajectories of molecular motion on surfaces.** *The Journal of chemical physics*, 130(16), 04B624.](https://doi.org/10.1063/1.3118982)

[Khatua, S., Guerrero, J. M., Claytor, K., Vives, G., Kolomeisky, A. B., Tour, J. M., & Link, S. (2009). **Micrometer-scale translation and monitoring of individual nanocars on glass.** *ACS nano*, 3(2), 351-356.](https://pubs.acs.org/doi/full/10.1021/nn800798a)

[Chen, F., García-López, V., Jin, T., Neupane, B., Chu, P. L. E., Tour, J., & Wang, G. (2016). **Moving Kinetics of Nanocars with Hydrophobic Wheels on Solid Surfaces at Ambient Conditions.** *The Journal of Physical Chemistry C*, 120(20), 10887-10894.](https://pubs.acs.org/doi/full/10.1021/acs.jpcc.6b01249)

[Buchner, F., Xiao, J., Zillner, E., Chen, M., Röckert, M., Ditze, S., ... & Marbach, H. (2011). **Diffusion, rotation, and surface chemical bond of individual 2 H-tetraphenylporphyrin molecules on Cu (111).** *The Journal of Physical Chemistry C*, 115(49), 24172-24177.](https://pubs.acs.org/doi/full/10.1021/jp206675u)

[Wasio, N. A., Murphy, C. J., Patel, D. A., Wei, D., Sholl, D. S., & Sykes, E. C. H. (2017). **Towards the directional transport of molecules on surfaces.** *Tetrahedron*, 73(33), 4858-4863.](https://www.sciencedirect.com/science/article/pii/S0040402017306658)

[Xu, Q., Feng, L., Sha, R., Seeman, N. C., & Chaikin, P. M. (2011). **Subdiffusion of a sticky particle on a surface.** *Physical review letters*, 106(22), 228102.](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.106.228102)
