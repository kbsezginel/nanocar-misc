# Calculating molecular diffusion on a surface

Before studying motion of nanocars on surfaces it's a good idea to start with simpler molecules and
try replicating experimental results. There aren't many studies measuring single molecule diffusion
of *larger* molecules, however, I was able to identify the following three studies which I will
use as anchor points for the computational setup.

## Comparative diffusion of DC and HtBDC on Cu(1 1 0)

Mean-squared displacement and hopping rate relation:

> <i> <(Δx<sup>2</sup>)> = λht </i>

HtBDC differs from DC solely by having six additional
tert-butyl spacer groups which raise the aromatic plane
of HtBDC away from the surface. As will be shown be-
low this leads to a 4 orders of magnitude higher diffusion
constant for HtBDC compared to DC in the investigated
temperature range.

<table>
<tr>
  <th>DC</th>
  <th>HtBDC</th>
</tr>
  <tr>
  <th><iframe style="width: 500px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=wireframe&cid=67448&bg=white"></iframe></th>
  <th><iframe style="width: 500px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=wireframe&cid=15467576&bg=white"></iframe></th>
</tr>
</table>


## Diffusion of PVBA on Pd(1 1 0)

## Diffusion of C60 on Pd(1 1 0)

> Table 1: Diffusion parameters (activation energy and attempt frequency) extracted from experimental surface diffusion studies of a few selected molecules (DC, HtBDC, C60, PVBA) on two metal surfaces (Cu(1 1 0) and Pd(1 1 0)).

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
</table>
