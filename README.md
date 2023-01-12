**NB: This is repository aims to provide everything needed to rerun the original Jupyter notebook. I am not connected to the [Theis Lab](https://github.com/theislab) and work on this repository in my free time.**

# Single-cell proteomics analysis in Python

## Reproducing the results

### Requirements

The only requirements for the reproduciton are a conda installation and this repository.

Note of caution: while this repository holds all the information to reproduce the plots, there might still be subtle differences that escaped me.

### Step by Step instructions

1. Get a copy of this repository and open a shell in it.

   e.g. with

   ```shell
   git clone https://github.com/fabianegli/singlecell_proteomics
   cd singlecell_proteomics
   ```

2. Set up the conda environment for the reproduction (the following command will create an environment named `scprep`)

   `conda env create --file reproduce-single-cell-proteomics.yaml`

3. Activate the new conda environment

   `conda activate scprep`

4. Start JupyterLab

   `jupyter lab`

5. Open `TSP_cell_cycle_analysis.ipynb` in JupyterLab
6. Run the code.

For convenience step 1.-4. all in one:

```shell
git clone https://github.com/fabianegli/singlecell_proteomics
cd singlecell_proteomics
conda env create --file reproduce-single-cell-proteomics.yaml
conda activate scprep
jupyter lab
```

## Reference

This repository contains analyses done for [Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation](https://doi.org/10.15252/msb.202110798), A Brunner, ..., M Mann, Molecular Systems Biology (2022).

The analyses were performed in Python and heavily use [scanpy](https://scanpy.readthedocs.io/en/stable/) and [anndata](https://anndata.readthedocs.io/en/latest/) functionality. Both Python packages were originally created for single cell transcriptomics analyses, but can to a large part also directly be applied to protein data and thus help kick off this exciting new field! Especially scanpy enables easy data visualizations like PCA plots or UMAPs and provides some ready to use analysis methods like assigning cell cycle stage scores to single cells given some cell cycle markers.

## License

This repository is licensed under the BSD-3 clause license.
The license for my contributinos resides in `LICENSE-fabianegli` while the original code's license is in `LICENSE`.

## Comments

The effort to make this repository's code reproducible was carried out on MacOS 11.7.2. It has yet to be tested on other platforms.
`conda-env-for-reproduction-on-MacOS1172.yaml` contains the exported conda environment - this file can be used to set up the environment exactly the same, but it will most probably not work if you use another OS than what generated it.
