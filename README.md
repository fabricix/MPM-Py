# MPM-Py

A Material Point Method implementation using Python: MPM-Py. This program uses objected-oriented programming paradigm to represent and modeling the elements and its interaction in the material point method context.

## Installation

```git
git clone https://github.com/fabricix/MPM-Py.git
```

## Documentation

To create the documentation, install pdoc:

```bash
pip3 install pdoc3
```

And then run

```bash
pdoc --html -c latex_math=True modules/
```

To read the documentation, open the file `/html/modules/index.html` using a web browser.

Note that in Windows the module flag  `-m` must be used to correctly use `pdoc`:

```bash
python -m pdoc --html -c latex_math=True modules/
```
## Requirements

* Python 3.7.4 or superior

* Matplotlib 3.3.4 or superior

## Running tests and examples

In the folders `verification_problems` and `tests` there are examples showing and testing the functionalities of the program.

### Mesh test

#### All elements with particles

The file `tests/mesh-test.py` tests the mesh generations module by plotting the mesh and showing the number of elements, nodes and material points. 

Run this example as:

```bash
python mesh-test.py
```
![Alt text](tests/mesh_test.png?raw=true "All elements with particles")

#### Mesh with particles in some elements
In this case the particles are distributed in some elements.

Run this example as:

```bash
python mesh_elements_without_particles_test.py
```
![Alt text](tests/mesh_elements_without_particles_test.png?raw=true "Elements without particles")

### Interpolation function test

The file `tests/interpolation_functions_test.py` shows the interpolation functions and its derivates over an one 1D element.

In `test_interpolation_functions` function of the `shape` module, set `shape_type="linear"` for linear interpolation functions or `shape_type="cpGIMP"` for contiguous particle GIMP (generalized interpolation material point).

Run this example as:

```bash
python interpolation-functions-test.py
```
Linear interpolation functions:

![Alt text](tests/linear_interpolation_functions_test.png?raw=true "Linear interpolation functions")

cpGIMP interpolation functions:

![Alt text](tests/cpGIMP_interpolation_functions_test.png?raw=true "Linear interpolation functions")

### Single mass vibration problem

In this verification problem a single mass vibration is analyzed numerically and then the numerical solution is compared with the analytical one.

Run this example as:

```bash
python mpm-single-mass-bar-vibration.py
```
![Alt text](verification_problems/mpm_single_mass_vibration.png?raw=true "Single mass vibration problem")

## Parametric analysis over material density

```bash
python mpm-single-mass-bar-vibration_parametric_density.py
```
![Alt text](verification_problems/mpm_single_mass_vibration_parametric_density.png?raw=true "Single mass vibration problem: Parametric analysis over density")


### Continuum bar vibration problem

In this verification problem a continuum bar vibration is analyzed numerically and then the numerical solution is compared with the analytical one.

Run this example as:

```bash
python mpm-continuum-bar-vibration.py
```

![Alt text](verification_problems/mpm_continuum_bar_vibration.png?raw=true "Continuum bar vibration problem")

### Wave traveling in a pile

In this verification problem a wave traveling in a pile is analyzed numerically and then the numerical solution is compared with the analytical one.

Run this example as:

```bash
python mpm_wave_in_pile.py
```

![Alt text](verification_problems/mpm_wave_in_pile.png?raw=true "Wave in pile vibration problem")

## Parametric analysis over Young modulus

```bash
python mpm_wave_in_pile_parametric_young.py
```

![Alt text](verification_problems/mpm_wave_in_pile_parametric_young.png?raw=true "Wave in pile vibration problem with parametric analysis over Young modulus")

### Local damping

The local damping is a nodal force proportional to the unbalanced nodal total force, acting in opposite nodal velocity direction.

The local damping must be setting up using the `model_setup` class. For example:

```bash
msetup = setup.model_setup()
msetup.damping_local_alpha=0.1
```

![Alt text](tests/damped_continuum_bar_vibration.png?raw=true "Damped continuum bar vibration")

## Parametric analysis over damping factor

```bash
python mpm-continuum-bar-vibration_damping.py
```

![Alt text](verification_problems/mpm_continuum_bar_vibration_damping.png?raw=true "Continuum bar vibration problem with parametric analysis over damping factor")
