---
numbering: false
---

# Speeding up package installation

As your environment gets bigger, you might notice that attempting to install new packages becomes very sluggish, and involves long wait times. This is because managing dependencies becomes exponentially more complex the more packages there are. Thus, computing solutions that work for all packages takes longer and longer.

The python community has proposed custom solutions to this. 

## First thing to try

The first thing to do is to update the conda backend solver to '`libmamba`': this can be done with the following `conda` command:

```bash
conda config --set solver libmamba
```

Check is this has made a notable improvement.

## Second thing to try

If this doesn't notably speed up your installs, the second thing is to manually install the drop-in replacement for `conda`, called `mamba` (this continues the ongoing snake theme of many Python tools...).

Install `mamba` in your `base` environment using the following command:

```bash
conda install -c conda-forge -n base mamba 
```
From this point, you should be able to replace the word `conda` in any instruction with the word `mamba`. This should work across environments. For instance:

```bash
mamba activate gsc
mamba install -c conda-forge numpy
```

This should dramatically improve the time taken to solve dependencies.