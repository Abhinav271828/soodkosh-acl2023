from numpy import argmin
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        changes = [1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
                changes.append(0)
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
                changes.append(1)
        distances = distances_
    return distances[-1]

#pws = \
["ना:",
"कुुय",
"कव",
"फ़िल्र",
"तॉल",
"पेन्श",
"स्घोट",
"भीर्ड",
"जुल्क",
"अन्टा",
"जांख",
"विका",
"हनड़",
"हफ़ल",
"आल्गा",
"अज़्ज़म",
"नायू",
"नूला",
"ग्यान्त",
"रेम्ना",
"अक्सित",
"ओंटना",
"रिहाक",
"बुगज़ू",
"हन्गा",
"गायून",
"तमघ",
"सलन्क",
"फुस्से",
"फैखी",
"सिफूत",
"मसरह",
"लालीस",
"युतको",
"ताजपुन",
"ननदान्स",
"तजरील",
"इलाहना",
"अबख़दा",
"अनातक",
"लिठाई",
"काराईट",
"वाविमा",
"उटकाना",
"जफजा",
"सफेरी",
"उन्जुका",
"पनिवैश",
"अनाकषत",
"इन्स्टारा",
"बेशिध्र",
"यर्धबाद",
"ज़सूची",
"मुनमूल्य",
"अपरचन",
"परीथाम",
"दुमार्डा",
"पताग्ना",
"शीस्करण",
"धुरन्वै",
"बेन्सीना",
"किरनोवक",
"किन्हूता",
"वीशकाला",
"बामल्लें",
"धोगिमन",
"केलिफोन",
"नसविष्का",
"आत्मखाई",
"परिमयता",
"बिशुभावल",
"शद्रगानी",
"औरावस्था",
"हरखिनित्व",
"देहमूनिका",
"असनस्पेतक",
"रुदनीवाला",
"पदन्शानिया",
"तामबूलियों",
"श्रिहागनतन",
"साथ्यदारी",
"मायामामन्द",
"मुर्तववादी",
"गुठ्रानेबाद",
"क्राब्लोनेविक",
"उल्गारेषियों",
"दुस्सवपार्शिक",
"राइकरषिक्ता",
"प्रात्रिषक्षत",
"कोरुपाशवादी"
]

pws = \
["nɑɑ",
"kʊj",
"kəʋ",
"fɪlɾ",
"Tɔɔl",
"peenʃ",
"sɡʱɔɔʈ",
"bʱiiɾɖ",
"Jʊlk",
"ənʈɑɑ",
"Jɑɑ̃kʰ",
"ʋɪkɑɑ",
"ɦənəɽ",
"ɦəfəl",
"ɑɑlɡɑɑ",
"əzzəm",
"nɑɑjuu",
"nuulɑɑ",
"ɡjɑɑnT",
"ɾəmnɑɑ",
"əksɪT",
"oõʈnɑɑ",
"ɾɪɦɑɑk",
"bʊɡzuu",
"ɦəŋɡɑɑ",
"ɡɑɑjuun",
"Təməɡʱ",
"sələŋk",
"pʰʊssee",
"pʰɛɛkʰii",
"sɪfuuT",
"məsɾəɦ",
"lɑɑliis",
"jʊTkoo",
"TɑɑJpʊn",
"nənDɑɑns",
"TəJɾiil",
"ɪlɑɑɦnɑɑ",
"əbəxDɑɑ",
"ənɑɑTək",
"lɪTʰɑɑii",
"kɑɑɾɑɑɪʈ",
"ʋɑɑʋɪmɑɑ",
"ʊʈkɑɑnɑɑ",
"JəpʰJɑɑ",
"səpʰeeɾii",
"ʊnJʊkɑɑ",
"pənɪʋeeʃ",
"ənɑɑkʂəT",
"ɪnsʈɑɑɾɑɑ",
"beeʃɪDʱɾə",
"jəɾDʱbɑɑD",
"zəsuuCii",
"mʊnmuuljə",
"əpəɾCən",
"pəɾɪTʰɑɑm",
"Dʊmɑɑɾɖɑɑ",
"pəTɑɑɡnɑɑ",
"ʃiiskəɾəɳ",
"Dʱʊɾənʋee",
"beensiinɑɑ",
"kɪɾnooʋək",
"kɪnɦuuTɑɑ",
"ʋiiʃkɑɑlɑɑ",
"bɑɑməlleẽ",
"Dʱooɡɪmən",
"keelɪpʰoon",
"nəsʋɪʂkɑɑ",
"ɑɑTməkʰɑɑii",
"pəɾɪməjTɑɑ",
"bɪʃʊbʱɑɑʋəl",
"ʃəDɾəɡɑɑnii",
"ɔɔɾɑɑʋəsTʰɑɑ",
"ɦəɾkʰɪnɪTʋə",
"Deeɦmuunɪkɑɑ",
"əsənspeeTək",
"ɾʊDniiʋɑɑlɑɑ",
"pəDnʃɑɑɳɪjɑɑ",
"Tɑɑmbuulɪjoõ",
"ʃɾɪɦɑɑɡənTən",
"sɑɑTʰjəDɑɑɾii",
"mɑɑjɑɑmɑɑmənD",
"muuɾTəʋʋɑɑDii",
"ɡʊʈʰɾɑɑneebɑɑD",
"kɾɑɑblooneeʋɪk",
"ʊlɡəɾeeʂɪjõ̃",
"Dʊssəʋpɑɑɾʃɪk",
"ɾɑɑɪkəɾʂɪkTɑɑ",
"pɾɑɑTɾɪʂəkʂəT",
"kooɾʊpɑɑʃʋɑɑDii"
]

def clean_word(w):
    w = w.replace(' ', '').replace('.', '').replace('ˈ', '')
    w = w.replace('d͡ʒ', 'J').replace('t͡ʃ', 'C')
    w = w.replace('t̪', 'T').replace('d̪', 'D')
    w = w.replace('ᵊ', 'ə')
    for i, c in enumerate(w):
        if (c == 'ː'):
            if (w[i-1] == '̃'):
                w = w[:i-1] + w[i-2] + w[i-1] + w[i+1:]
            else:
                w = w[:i] + w[i-1] + w[i+1:]
    return w

print("Getting vocab")
f = open('ipa_lexicon.txt', 'r')
lex = []
from tqdm import tqdm
for line in tqdm(f):
    lex.append(clean_word(line[:-1]))
f.close()

closest = []
for w in tqdm(pws, desc="Finding closest words"):
    closest.append(min(lex, key=lambda x: levenshteinDistance(x, w)))

distances = []
for w in tqdm(pws, desc="Finding distances"):
    distances.append(min(map(lambda x: levenshteinDistance(x, w), lex)))

g = open('closest.txt', 'w')
g.write('\n'.join(map(lambda w: w[0]+'\t'+str(w[1]),zip(closest, distances))))
g.close()

characters = {'m', 'i', 'z', 'ɽ', 'ŋ', 'T', 'b', 'j', 'l', 'e', 'ɑ', 'ʃ', 'D', 'ɦ', 'ʈ', 'n', 'ʊ', 'ɾ', 'a', '‿', 'ʰ', 'ɖ', 'x', 'ɛ', 'k', '̃', 'ɣ', 'p', 'ə', 'ɡ', 'ɔ', 'o', 'ʱ', 'u', '̯', 'ʒ', 'f', 'C', 'J', 'æ', 'ɪ', 's', 'ɳ', 'ʋ', 'q', 'ʂ', 'ɲ'}
consonants = {'m', 'z', 'ɽ', 'ŋ', 'T', 'b', 'j', 'l', 'ʃ', 'D', 'ɦ', 'ʈ', 'n', 'ɾ', 'ʰ', 'ɖ', 'x', 'k', 'ɣ', 'p', 'ɡ', 'ɔ', 'ʱ', 'ʒ', 'f', 'C', 'J', 's', 'ɳ', 'ʋ', 'q', 'ʂ', 'ɲ'}
vowels = {'ɑ', 'e', '̃', 'u', 'ɪ', '̯', 'a', 'o', 'ʊ', 'æ', 'i', 'ə', 'ɛ'}

f = open('ipa_lexicon.txt', 'r')
lex = []
from tqdm import tqdm
for line in tqdm(f):
    lex.append(clean_word(line[:-1]))
f.close()

def get_x_plus(w, s):
    clusters = []
    i = 0
    while i < len(w):
        if w[i] in s:
            cluster = w[i]
            i += 1
            while i < len(w) and w[i] in s:
                cluster += w[i]
                i += 1
            clusters.append(cluster)
            i -= 1
        i += 1
    return clusters

c_clusters = []
for w in lex: c_clusters += get_x_plus(w, consonants)
c_clusters = set(c_clusters)

for w in pws:
    c = get_x_plus(w, consonants)
    wrong = [x for x in c if x not in c_clusters]
    #if sum([(x not in c_clusters) for x in c]): print(0)
    #else: print(1)
    if wrong == []: print(0)
    else: print(str(len(wrong)) + '\t' + str(wrong))

print('\n\n')
v_clusters = []
for w in lex: v_clusters += get_x_plus(w, vowels)
v_clusters = set(v_clusters)

for w in pws:
    c = get_x_plus(w, vowels)
    wrong = [x for x in c if x not in v_clusters]
    #if any([(x not in v_clusters) for x in c]): print(0)
    #else: print(1)
    if wrong == []: print(0)
    else: print(str(len(wrong)) + '\t' + str(wrong))

print('\n\n')
def get_cvc_plus(w):
    clusters = []
    i = 0
    while i < len(w)-1:
        if w[i] in consonants and w[i+1] in vowels:
            cluster = w[i]
            i += 1
            while i < len(w) and w[i] in vowels:
                cluster += w[i]
                i += 1
            if i < len(w) and w[i] in consonants:
                cluster += w[i]
                clusters.append(cluster)
                i -= 1
        i += 1
    return clusters

cvc_clusters = []
for w in lex: cvc_clusters += get_cvc_plus(w)
cvc_clusters = set(cvc_clusters)

for w in pws:
    c = get_cvc_plus(w)
    wrong = [x for x in c if x not in cvc_clusters]
    #if any([(x not in cvc_clusters) for x in c]): print(0)
    #else: print(1)
    if wrong == []: print(0)
    else: print(str(len(wrong)) + '\t' + str(wrong))

def get_cpvpcp(w):
  clusters = []
  i = 0
  while i < len(w):
    if w[i] in consonants:
      j = i + 1
      cluster = [w[i]]
      while j < len(w) and w[j] in consonants:
        cluster.append(w[j])
        j += 1
      if j < len(w) and w[j] in vowels:
        while j < len(w) and w[j] in vowels:
          cluster.append(w[j])
          j += 1
        if j < len(w) and w[j] in consonants:
          c = j
          while j < len(w) and w[j] in consonants:
            cluster.append(w[j])
            j += 1
          clusters.append(''.join(cluster))
          i = c
        else:
          i += 1
          continue
      else:
        i += 1
        continue
    else:
      i += 1
  return clusters

cpvpcp_clusters = []
for w in lex: cpvpcp_clusters += get_cpvpcp(w)
cpvpcp_clusters = set(cpvpcp_clusters)

for w in pws:
    c = get_cpvpcp(w)
    wrong = [x for x in c if x not in cpvpcp_clusters]
    #if any([(x not in cvc_clusters) for x in c]): print(0)
    #else: print(1)
    if wrong == []: print(0)
    else: print(str(len(wrong)) + '\t' + str(wrong))

matras = ['ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'े', 'ै', 'ो', 'ौ', 'ं', 'ः', 'ँ', 'ॅ', 'ॉ', 'ॆ', 'ॊ']

f = open('dev_stats.tsv', 'w')
for w in pws:
    l = len(w)
    m = len([c for c in w if c in matras])
    h = w.count('्')
    n = w.count('़')
    a = l - m - n - (1.5 * h)
    f.write(w + '\t' + str(l) + '\t' + str(m) + '\t' + str(a) + '\n')
f.close()

f = open('ipa_pseudowords.txt', 'r')
ipa = []
for line in f:
    ipa.append(line[:-1])
f.close()

f = open('ipa_stats.tsv', 'w')
for w in ipa:
    s = w.count('.') + 1
    p = w.count(' ') + 1 - (s - 1)
    f.write(w + '\t' + str(s) + '\t' + str(p) + '\n')
f.close()
