# Sample-MPI-in-python

## Requirements
- Matplotlib ``pip install matplotlib``
- NumPy ``pip install numpy``
- Mpi4py ``pip install mpi4py``
- SciPy ``pip install scipy``

**NB:** Ensure You have installed mpi on your laptop. For Windows Users use [this](https://www.microsoft.com/en-us/download/confirmation.aspx?id=57467&6B49FDFB-8E5B-4B07-BC31-15695C5A2143=1) link to download its setup.

## How to Run
Run the [area_under_a_curve.ipynb](https://github.com/dopesky/Sample-MPI-in-python/blob/main/area_under_a_curve.ipynb) file in jupyter notebook. It has comments explaining what is happening. 

Alternatively, you can use the cmd to run each of the ``.py`` files with the following codes:
````
$ python area_under_a_curve.py

$ mpiexec -n 4 python -m mpi4py area_under_a_curve_mpi.py

$ mpiexec -n 4 python -m mpi4py mpi_processing_sample.py
````

### Note:

``area_under_a_curve.py`` contains code to find the area under the curve in without using MPI. It uses ``matplotlib`` to draw the curve.

``mpi_processing_sample.py`` contains code to simulate a sample parallel proccessing and communication in mpi using mpi4py.

``area_under_a_curve_mpi.py`` contains code to find the area under the curve using parallel processing in mpi using mpi4py.
