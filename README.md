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

## Requirements

* Python 3.7.4 or superior

* Matplotlib 3.3.4 or superior

## Running tests and examples

In the folders `verification_problems` and `tests` there are examples showing and testing the functionalities of the program.

### Mesh test

The file `tests/mesh-test.py` tests the mesh generations module by plotting the mesh and showing the number of elements, nodes and material points. 

Run this example as:

```bash
python mesh-test.py
```

### Interpolation function test

The file `tests/interpolation_functions_test.py` shows the interpolation functions and its derivates over an one 1D element.

Run this example as:
```bash
python interpolation-functions-test.py
```

### Single mass vibration problem

In this verification problem a single mass vibration is analyzed numerically and then the numerical solution is compared with the analytical one.

Run this example as:
```bash
python mpm-single-mass-bar-vibration.py
```

### Continuum bar vibration problem

In this verification problem a continuum bar vibration is analyzed numerically and then the numerical solution is compared with the analytical one.

Run this example as:
```bash
python mpm-continuum-bar-vibration.py
```