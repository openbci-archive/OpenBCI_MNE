# Using OpenBCI boards with MNE

This repo contains demos for integration of OpenBCI boards to MNE libraries.

This integration in done using [BrainFlow project](https://brainflow.readthedocs.io/en/stable/).

## MNE Python with BrainFlow's python binding

BrainFlow returns numpy arrays, all you need - convert numpy arrays to MNE objects.

[Example](./python/brainflow_to_mne.py)

## MNE R with BraiFlow's R binding

BrainFlow and MNE both use [reticulate](https://rstudio.github.io/reticulate/) package, which allows to call Python code from R, and provides seamless convertion between Python and R objects.

[Example](./r/brainflow_to_mne.R)

## License
MIT
