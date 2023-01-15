# PseudRNN

This repository hosts the generation pipeline & model, evaluation experiment, and dataset presented by the PseudRNN work.

## Getting Started

- Python: >= 3.10
- Run the following command to install dependencies: `pip install -r requirements.txt`

## Evaluation
To evaluate the pseudowords, run the following command from the root directory:
```
$ python3 metrics/edit_dist.py
```

Its outputs are as follows:

* `closest.tsv`: For each pseudoword, the closest word to it in the lexicon, followed by the Levenshtein distance of the pair. Note that if line 20 is commented in and line 113 out, then line 220 should use `devanagari_lexicon.txt`, and otherwise `ipa_lexicon.txt`.
* `dev_stats.tsv`: For each pseudoword, its length, the number of matras in it, and the number of aksharas in it (tab-separated).
* `ipa_stats.tsv`': For each pseudoword, the number of syllables in it, and the number of phonemes in it (tab-separated).
* CLI output: The first 90 lines contain, for each pseudoword, the number of C+ clusters not found in the lexicon. This is followed by three newlines, and 90 lines with the number of unseen V+ clusters. The next set contains the number of unseen CV+C clusters, and the next contains the number of C+V+C+ clusters.