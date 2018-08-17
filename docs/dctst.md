## Dynamically Corrected Transition State Theory (dcTST)

In order to estimate diffusion transition state theory could be used with umbrella sampling.
For the unit cell of a Cu(110) surface we can divide the surface into grid points and
constrain our molecule to the grid point using a spring.
Then using Weighted Histogram Analysis Method (WHAM) we can calculate the free energy barrier
for diffusion in each direction.

<p align="center"><img src="assets/img/dctst/umbrella-sampling-energy-barrier.png" width="600"></p>

Above, on the left the grid points on the Cu(110) surface is shown.
For each point an MD simulation is performed.
Then 2D WHAM analysis is used to calculate free energy barriers for moving between these points.

### Calculating Overall Activation Energy
The overall activation energy for diffusion in a given direction can be calculated by averaging
different energy profiles (parallel) in that direction. Assuming Boltzmann distribution, we can calculate
probabilities for each energy profile. The probability of taking each pathway is related to it's
activation energy exponentially. Therefore we first take the activation energy for each pathway and
calculate probability for that pathway as follows:

<p align="center"><img src="assets/img/dctst/eqn_state_probability.png" width="250"></p>

After calculating probabilities for each pathway in the desired direction we can then multiply the
activation energies with the probabilities to get the average activation energy as follows:

<p align="center"><img src="assets/img/dctst/eqn_average_energy.png" width="250"></p>

## Free Energy Barriers

### Linear Energy Barriers (y) - 2D WHAM

<p>
    <details>
      <summary><b>DC</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/DC_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>HtBDC</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/HtBDC_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>C60</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/C60_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>PCARBORANE</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/PCARBORANE_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>BtPHD</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/BtPHD_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>DNHD</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/DNHD_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>PVBA</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/PVBA_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>TPEE</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/TPEE_Cu110-barriers.png">
    </details>
</p>

<p>
    <details>
      <summary><b>VL</b></summary>
        <img src="assets/img/dctst/2D-wham-barrier-y/VL_Cu110-barriers.png">
    </details>
</p>

### 3D Energy Surfaces

## Position Histograms

### WHAM 2D x and y histograms

<p>
    <details>
      <summary><b>DC</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/DC_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>HtBDC</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/HtBDC_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>C60</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/C60_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>PCARBORANE</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/PCARBORANE_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>BtPHD</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/BtPHD_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>DNHD</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/DNHD_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>PVBA</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/PVBA_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>TPEE</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/TPEE_Cu110-xy-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>VL</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/VL_Cu110-xy-hist.png">
    </details>
</p>


### 2D position histograms

<p>
    <details>
      <summary><b>DC</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/DC_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>HtBDC</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/HtBDC_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>C60</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/C60_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>PCARBORANE</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/PCARBORANE_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>BtPHD</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/BtPHD_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>DNHD</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/DNHD_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>PVBA</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/PVBA_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>TPEE</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/TPEE_Cu110-surf-hist.png">
    </details>
</p>


<p>
    <details>
      <summary><b>VL</b></summary>
        <img src="assets/img/dctst/2D-pos-hist/VL_Cu110-surf-hist.png">
    </details>
</p>


## 3D Surface Energy

### [1D WHAM Energy Profiles](htbdc_cu110_free_energy_1d)

### [2D WHAM Energy Profile](htbdc_cu110_free_energy_2d)
