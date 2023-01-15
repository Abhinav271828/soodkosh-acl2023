import wikipron
from tqdm import tqdm

f = open('../devanagari_lexicon.txt', 'w')
config = wikipron.Config(key="hin")  # French, with default options.
for word, pron in tqdm(wikipron.scrape(config)):
    f.write(word + '\t' + pron + '\n')
