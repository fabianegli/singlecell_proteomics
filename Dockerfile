FROM docker.io/continuumio/miniconda3@sha256:10b38c9a8a51692838ce4517e8c74515499b68d58c8a2000d8a9df7f0f08fc5e

COPY reproduce-single-cell-proteomics.yaml reproduce-single-cell-proteomics.yaml
RUN conda env update --name base --file reproduce-single-cell-proteomics.yaml
CMD jupyter lab --allow-root --ip 0.0.0.0 --no-browser
