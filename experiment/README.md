# Experiment

## Structure

 **.**
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

--reset to reset counts

We have adapted the *neuropsydia* module from *https://github.com/neuropsychology/Neuropsydia.py*.

https://neuropsydia.readthedocs.io/en/latest/ can be referred to.

Modified ask.py, core.py and scale.py files.

36 stimuli in total for each run of the experiment

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

The generated image is of size 300 x 80 pixels, and the text is centered within the given space. The text is generated in *yellow* (#ffff00) on a *blue* (#496d89) background for good contrast and visibility. We chose *Gargi* font for the Devanagiri script for easy readability.