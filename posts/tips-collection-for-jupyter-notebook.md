<!--
.. title: Tips Collection for Jupyter Notebook
.. slug: tips-collection-for-jupyter-notebook
.. date: 2019-04-14 13:26:32 UTC-08:00
.. tags: 
.. category: Python
.. link: 
.. description: 
.. type: text
.. status: draft
-->



## Automatic ipykernel installation

When you do not see a installed ipython kernel, it would be better to install `nb_conda_kernels` so that this will automatically register it as jupyter kernel and show up in the list of kernels.  

 `conda install nb_conda_kernels`



I used to install and name each kernel manually by this command:

```
source activate myenv
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

However,  `nb_conda_kernels` can more easily organize your kernel with consistent naminng convension.  



reference: <https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook>