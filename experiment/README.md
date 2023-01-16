# Experiment

## Structure

**experiment**
├── **data**
│   ├── *nonpseudo.csv*  : List of words and non-words
│   └── *pseudo.csv*  : List and counts of all pseudo-words
├── **images** : Images for all stimuli
│   ├── **nonpseudo**
│   ├── **pseudo**
│   └── **warmup**
├── **neuropsydia** : Modified *neuropsydia* python module
├── **results** : Stores the results of all runs of the experiment
├── *run.py* : Main experiment for the given stimuli
├── *requirements.txt* : List of requisite python modules
└── *stimuli2img.ipynb* : Generates image for given stimulus

## Prerequisites

Requires Python 3.7 or higher on a Windows system. Install all necessary packages using:

```powershell
pip install -r requirements.txt
```

We have adapted the *neuropsydia* module from [https://github.com/neuropsychology/Neuropsydia.py]() and modified the *ask.py*, *core.py* and *scale.py* files to better accommodate the experiment's requirements.

## Data

**nonpseudo.csv**

| Label |            Type            |
| :---: | :------------------------: |
|   1   | Short high-frequency words |
|   2   | Long high-frequency words |
|   3   | Short low-frequency words |
|   4   | Long high-frequency words |
|   5   |      Short non-words      |
|   6   |       Long non-words       |

**pseudo.csv**

| Label |            Type            |
| :---: | :------------------------: |
|   7   | Short pseudo-words |
|   8   | Long pseudo-words |

Words (12)

- 6 high freq
  - 3 short
  - 3 long
- 6 low freq
  - 3 short
  - 3 long

Non Words (12)

- 6 long
- 6 short

Pseudo Words (>12)

- half short
- half long

36 stimuli in total for each run of the experiment

## Run the experiment

Use the *--reset* parameter to reset the counts of all pseudowords used in past runs and start afresh.

```powershell
python experiment.py --reset
```

https://neuropsydia.readthedocs.io/en/latest/ can be referred to.

The generated image is of size 300 x 80 pixels, and the text is centered within the given space. The text is generated in *yellow* (#ffff00) on a *blue* (#496d89) background for good contrast and visibility. We chose *Gargi* font for the Devanagiri script for easy readability.
