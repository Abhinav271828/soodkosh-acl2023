# PseudRNN

This repository hosts the generation pipeline (with model), evaluation experiment, and the dataset presented by the PseudRNN work.

## Getting Started

- Python: >= 3.10
- Run the following command to install dependencies: `pip install -r requirements.txt`

# Soodkosh

soodkosh.csv contains a dataset of 90 pseudowords in Hindi. Each pseudoword has the following features listed out:

* `WRmean`: Wordlikeness Gradient Acceptability Mean over 44 native Hindi participants ratings (1-7)
* `FRmean`: Familiarity (of the pseudoword) Mean over 44 native Hindi participants ratings (1-7)
* `WTmean`: Time taken to rate Wordlikeness Gradient Acceptability (in ms)
* `FTmean`: Time taken to rate Familiarity (in ms)
* `comp`: Is the pseudoword a compound of two real words? (1 for yes, 0 for no)
* `poly`: Does the pseudoword have a real root and real affixes? (1 for yes, 0 for no)
* `npoly`: Does the pseudoword have a made-up root and real affixes? (1 for yes, 0 for no)
* `half`: Is the pseudoword a made of a real word and a made up word? (1 for yes, 0 for no)
* `1-C`: Is the pseudoword 1 character away from a made up word? (1 for yes, 0 for no)
* `C+`: Count of consonant sequences in the pseuoword do not appear in the Hindi wiktionary
* `V+`: Count of vowel sequences in the pseuoword do not appear in the Hindi wiktionary
* `CV+C`: Count of CV+C sequences in the pseuoword do not appear in the Hindi wiktionary
* `C+V+C+`: Are there C+V+C+ sequences in the pseuoword that do not appear in the Hindi wiktionary? (1 for yes, 0 for no)
* `C+V+C+#`: Count of C+V+C+ sequences in the pseuoword do not appear in the Hindi wiktionary
* `Dist_IPA`: Distance of the closest word in Hindi lexicon according to the IPA representations
* `Dist_Dev`: Distance of the closest word in Hindi lexicon according to the Devanagari representations
* `Orth_Len`: Orthographic Length of the pseudoword (an aggreagte of Matras and Aksharas)
* `Matras`: Count of Matras in the pseudoword
* `Aksharas`: Count of Aksharas in the pseudoword
* `Syllables`: Count of Syllables in the pseudoword
* `Phonemes`: Count of Phonemes in the pseudoword

Please refer to Jemma König's [work]{https://academic.oup.com/applij/article-abstract/41/6/878/5580557} for a detailed definition of `comp`, `poly`, `npoly`, `1-C`, and `C+`, `V+`, `CV+C`

Please refer to Ark Verma's [work]{https://link.springer.com/article/10.3758/s13428-021-01625-2} for a detailed definition of `Orth_len`, `Matras`, `Aksharas`, `Syllables`, and `Phonemes`.

## Descriptive Metrics for Soodkosh
To generate metrics for the pseudowords, run the following command from the root directory:
```
$ python3 metrics/edit_dist.py
```

Its outputs are as follows:

* `closest.tsv`: For each pseudoword, the closest word to it in the lexicon, followed by the Levenshtein distance of the pair. Note that if line 20 is commented in and line 113 out, then line 220 should use `devanagari_lexicon.txt`, and otherwise `ipa_lexicon.txt`.
* `dev_stats.tsv`: For each pseudoword, its length, the number of matras in it, and the number of aksharas in it (tab-separated).
* `ipa_stats.tsv`': For each pseudoword, the number of syllables in it, and the number of phonemes in it (tab-separated).
* CLI output: The first 90 lines contain, for each pseudoword, the number of C+ clusters not found in the lexicon. This is followed by three newlines, and 90 lines with the number of unseen V+ clusters. The next set contains the number of unseen CV+C clusters, and the next contains the number of C+V+C+ clusters.
