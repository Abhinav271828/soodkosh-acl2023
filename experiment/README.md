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

https://neuropsydia.readthedocs.io/en/latest/ can be referred to.

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

| Label |        Type        |
| :---: | :----------------: |
|   7   | Short pseudo-words |
|   8   | Long pseudo-words |

This file also lists the counts of all pseudo words.

## Run the experiment

Use the *--reset* parameter if the counts of all pseudowords used in past runs need to be reset for starting afresh.

```powershell
python run.py --reset
```

### Experiment Details
The experiment requires participants to rate stimuli (words, non-words, pseudowords) according to familiarity and wordlikeness. The scale of rating familiarity and wordlikeness for a given stimulus is from 1 to 7. The motivation and reasoning behind all the following details of the experiment are provided in the paper. The experiment starts upon pressing Enter, following which the stimuli appear after 1000ms, immediately after which the familiarity scale appears. Participants are given 6000ms to rate the familiarity of stimuli. The familiarity scale disappears either after the participant has finished rating or after the time is up (whichever is the minimum of the two). This is to ensure that the participants do not change their responses for the familiarity scale. There is a gap of 500ms between the familiarity and wordlikeness scales. Participants are given 5000ms to rate the wordlikeness of stimuli. For both familiarity and wordlikeness, in case the participants fail to rate the stimuli within the stipulated amount of time, the rating is recorded as -1.

The first part of the experiment is a warm-up test consisting of 5 randomised word stimuli (some of which are code-mixed, and some are low frequency). The Enter button required to start the warm-up test appears after 2000 ms. Upon the completion of the warm-up test, 10000ms are given to the participants before the appearance of the Enter button for starting the main experiment. This time is provided to the participants to relax before the main experiment and is also used to instruct them with regard to their responses in the warmup test. The main experiment consists of 36 stimuli in total, 12 words, 12 non-words, and 12 pseudowords. The stimuli in the main experiment are pseudo-randomised such that their occurrence is balanced across word types and lengths. 

### Element specific details

The following parameters can be changed by going to the respective codes.

In the experiment, the positioning of the elements on the screen with respect to the central horizontal line (-10<=y<=10) is as follows: the familiarity scale is placed above the central horizontal line (y=3.3), the wordiness scale is placed below the central horizontal line (y=-2.3), and the stimuli are placed above the familiarity scale (y=7). 

## Creation of Stimuli

Stimuli2img.ipynb (run on Google Colab) is used to generate the image form of the given Unicode string (word, pseudoword, or nonword) i.e the stimuli. The generated image is of size 300 x 80 pixels, and the text is centred within the given space. The text is generated in yellow (#ffff00) on a blue (#496d89) background for good contrast and visibility. The font **Gargi** was chosen for the Devanagiri script for easy readability.