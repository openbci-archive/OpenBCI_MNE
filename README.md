# Using OpenBCI boards with MNE

This repo contains demos for integration of OpenBCI boards to MNE libraries.

This integration in done using [BrainFlow project](https://brainflow.readthedocs.io/en/stable/).

## [MNE Scan](https://www.mne-cpp.org/index.php/category/development/mne-scan/)

MNE Scan is a part of [MNE-CPP project](https://github.com/mne-tools/mne-cpp). It's an application to visualize offline and online data. There is BrainFlow plugin which allows users to acquire data from all BrainFlow supported devices.

[Instructions to build BrainFlow plugin](https://mne-cpp.github.io/pages/development/brainflow.html)

![MNE-Scan](https://live.staticflickr.com/65535/49535986728_70c0e09497_b.jpg)

## MNE Python with BrainFlow's python binding

BrainFlow returns numpy arrays, all you need - convert numpy arrays to MNE objects.

[Example](./python/brainflow_to_mne.py)

## MNE R with BraiFlow's R binding

BrainFlow and MNE both use [reticulate](https://rstudio.github.io/reticulate/) package, which allows to call Python code from R, and provides seamless convertion between Python and R objects.

[Example](./r/brainflow_to_mne.R)

## License
MIT
