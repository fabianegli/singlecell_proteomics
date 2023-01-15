#!/usr/bin/env pytohn3

# © 2023 Fabian Egli
# BSD-3 Clause license


import tarfile
from pathlib import Path

bundled_data_file = "data.tar.gz"

if Path("data").exists():
    print("A 'data' directory is already present. Skipping the unpacking.")
    exit()

print(f"Extracting the dtata from {bundled_data_file} ... ", end="", flush=True)
with tarfile.open(bundled_data_file, "r:gz") as tar:
    tar.extractall()
print("done.")
