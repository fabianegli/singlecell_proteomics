**NB: This is repository aims to provide everything needed to rerun the original Jupyter notebook. I am not connected to the [Theis Lab](https://github.com/theislab) and work on this repository in my free time. There is not guarantee - implied or expressed - that this repository will allow a perfect reproduction of the results.**

# Single-cell proteomics analysis in Python

The analyses were performed in Python and heavily use [scanpy](https://scanpy.readthedocs.io/en/stable/) and [anndata](https://anndata.readthedocs.io/en/latest/) functionality. Both Python packages were originally created for single cell transcriptomics analyses, but can to a large part also directly be applied to protein data and thus help kick off this exciting new field! Especially scanpy enables easy data visualizations like PCA plots or UMAPs and provides some ready to use analysis methods like assigning cell cycle stage scores to single cells given some cell cycle markers.

## Reproducing the results

### Requirements

The only requirements for the reproduciton are a conda installation and this repository.

### Step by Step instructions for `conda`

1. Get a copy of this repository and open a shell in it.
2. Set up the conda environment using the conda environment definition in `reproduce-single-cell-proteomics.yaml`.
   This will create an environment named `scprep`.
3. Activate the new conda environment
4. Start JupyterLab
5. Open `TSP_cell_cycle_analysis.ipynb` in JupyterLab
6. Run the code.

For convenience step 1.-4. as shell commands:

```shell
# Step 1. Copy the repo
git clone https://github.com/fabianegli/singlecell_proteomics
# Step 1. Navigate in a terminal into the repo
cd singlecell_proteomics
# Step 2.
conda env create --file reproduce-single-cell-proteomics.yaml
# Step 3.
conda activate scprep
# Step 4.
jupyter lab
```

## Step by Step instructions for Containers

### Interactive

For this to work Podman needs to be installed on the system.

The `Dockerfile` in this repository can be used as follows to run the notebook: 

- Build the Podman image with `podman build .`
- Run the Podman image with `podman run -it -p 8888:8888 -v "${PWD}":"/tscp/" tscp`
- Point the browser to link in shown in the terminal starting with `http://127.0.0.1:8888/`
- Open the tscp folder in the Jupyter lab navigation, it contians the notebook.
- Open and run the notebook.

While it has been tested with Podman, it may also work with Docker. To run it with Docker simply change the `podman` with `docker`.

### Non-interactive
For a non-interactive reproduction one can use the following command:

```
podman run -it -v "${PWD}":"/tscp/" tscp \
  bash -c \
    "sed -i 's/conda-env-tissue-py/python/' /tscp/TSP_cell_cycle_analysis.ipynb; \
      python -m nbconvert \
      --execute \
      --to notebook /tscp/TSP_cell_cycle_analysis.ipynb \
      --output=/tscp/TSP_cell_cycle_analysis-reproduced.ipynb"
```

## The budled data in `data.tar.gz`

Much care has been given to the bundling of all data required for successful reproduction.
The following sources were used:

From PRIDE project [PXD024043] the files `20210919_DIANN_SingleCellOutput.pg_matrix_cellcyclepred.tsv` and `20210919_DIANN_SingleCellOutput.pg_matrix_notnormalized.tsv` in the
https://ftp.pride.ebi.ac.uk/pride/data/archive/2022/02/PXD024043/DIANN1.8_SingleCells_CellCycle.7z archive licensed under the [Creative Commons Public Domain (CC0)](https://creativecommons.org/share-your-work/public-domain/cc0/).

All other files in `data.tar.gz` originate from [Gene Expression Omnibus (GEO)](https://www.ncbi.nlm.nih.gov/gds/) as downloaded in January 2023.
The directories `GSE129447_RAW` and `GSE142277_RAW` with their respective contents were downloaded from https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE129447&format=file and https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE142277&format=file respectively as compressed folders and their contents subsequently extracted.
The files `GSM4226257_out_gene_exon_tagged.dge_exonsds_046.txt` and `GSM4226257_out_gene_exon_tagged.dge_intronsds_046.txt` in `GSM4226257_RAW` were individually downloaded and extracted from https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM4226257&format=file&file=GSM4226257%5Fout%5Fgene%5Fexon%5Ftagged%2Edge%5Fexonsds%5F046%2Etxt%2Egz and https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSM4226257&format=file&file=GSM4226257%5Fout%5Fgene%5Fexon%5Ftagged%2Edge%5Fintronsds%5F046%2Etxt%2Egz respectively.

The contents of `data.tar.gz`

```
data
├── 20210919_DIANN_SingleCellOutput.pg_matrix_cellcyclepred.tsv
├── 20210919_DIANN_SingleCellOutput.pg_matrix_notnormalized.tsv
├── GSE129447_RAW
│   ├── GSM3713084_HeLa_1.txt
│   ├── GSM3713085_HeLa_2.txt
│   └── GSM3713086_HeLa_3.txt
├── GSE142277_RAW
│   ├── GSM4224315_out_gene_exon_tagged.dge_exonssf002_WT.txt
│   ├── GSM4224315_out_gene_exon_tagged.dge_intronssf002_WT.txt
│   ├── GSM4224316_out_gene_exon_tagged.dge_exonssf002_KO.txt
│   └── GSM4224316_out_gene_exon_tagged.dge_intronssf002_KO.txt
└── GSM4226257_RAW
    ├── GSM4226257_out_gene_exon_tagged.dge_exonsds_046.txt
    └── GSM4226257_out_gene_exon_tagged.dge_intronsds_046.txt
```

## Reference

This repository contains analyses done for [Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation](https://doi.org/10.15252/msb.202110798), A Brunner, ..., M Mann, Molecular Systems Biology (2022).

## License

This repository is licensed under the BSD-3 clause license.

The licenses of the bundled data is noted in the "The budled data in `data.tar.gz`" section above.

## Comments

The effort to make this repository's code reproducible was carried out on MacOS 11.7.2. It has yet to be tested on other platforms.
`conda-env-for-reproduction-on-MacOS1172.yaml` contains the exported conda environment - this file can be used to set up the environment exactly the same, but it will most probably not work if you use another OS than what generated it.

While this repository holds all the information to reproduce the plots, there might still be subtle differences that escaped or that are outside my purview to change.
