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
  data-href='/mol/Pd110_DC.xyz'
  data-style='stick'>
</div>
