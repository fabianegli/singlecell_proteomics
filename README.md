**NB: This is repository aims to provide everything needed to rerun the original Jupyter notebook. I am not connected to the [Theis Lab](https://github.com/theislab) and work on this repository in my free time.**

# Single-cell proteomics analysis in Python

## Reference

This repository contains analyses done for [Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation](https://doi.org/10.15252/msb.202110798), A Brunner, ..., M Mann, Molecular Systems Biology (2022).

The analyses were performed in Python and heavily use [scanpy](https://scanpy.readthedocs.io/en/stable/) and [anndata](https://anndata.readthedocs.io/en/latest/) functionality. Both Python packages were originally created for single cell transcriptomics analyses, but can to a large part also directly be applied to protein data and thus help kick off this exciting new field! Especially scanpy enables easy data visualizations like PCA plots or UMAPs and provides some ready to use analysis methods like assigning cell cycle stage scores to single cells given some cell cycle markers.

## License

This repository is licensed under the BSD-3 clause license.
The license for my contributinos resides in `LICENSE-fabianegli` while the original code's license is in `LICENSE`.
