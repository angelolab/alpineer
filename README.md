# tmi

Toolbox for Multiplexed Imaging. Contains scripts and little tools which are used throughout [ark-analysis](https://github.com/angelolab/ark-analysis), [mibi-bin-tools](https://github.com/angelolab/mibi-bin-tools), and [toffy](https://github.com/angelolab/toffy)

## Requirements

Latest version of conda (miniconda prefered)

## Setup

Clone the repo

```
git clone https://github.com/angelolab/tmi.git
```

Move into directory and build environment

```
cd tmi
conda env create -f environment.yml
```

## Usage

Activate the environment

```
conda activate tmi_env
```

## Updating

Run the command

```
git pull
```

> The following step will probably be changed in the future

You may have to rebuild the environment which can be done via:

```
conda remove --name tmi_env --all
conda env create -f environment.yml
```

## Questions?

Feel free to open an issue on our [GitHub page](https://github.com/angelolab/tmi/issues)
