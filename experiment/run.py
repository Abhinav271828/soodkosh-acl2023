# import time
import neuropsydia as n
import pandas as pd
import os
import random
import sys

if len(sys.argv)==2 and sys.argv[1]=="--reset":
    ps = pd.read_csv("./data/pseudo.csv", index_col=False)
    for i in range(ps.count()[0]):
        ps.at[i, 'Count']=0
    ps.to_csv("./data/pseudo.csv", index=False)

n.start()

warmup_wordiness = []
warmup_familiarity = []
warmup_wordiness_time = []
warmup_familiarity_time = []

main_wordiness = []
main_familiarity = []
main_wordiness_time = []
main_familiarity_time = []

#Roll Number
n.newpage()
roll_number = n.ask(text = "Enter your roll number:",
                    style = "body",
                    x = -3,
                    y = 1.5,
                    size = 2,
                    color = "blue",
                    detach_question=True,
                    question_style="body",
                    question_x = 0,
                    question_y = 3,
                    question_size = 2
                    )
print(roll_number)

# Warmup Test
n.newpage()
n.write(text="WARMUP",
        x = 0,
        y = 2,
        size = 2
        )
n.write(text="TEST",
        x = 0,
        y = 0,
        size = 2
        )
n.refresh()
n.time.wait(2000)
press_enter = n.ask(text = "Press ENTER",
                    style = "body",
                    x = -10,
                    y = -10,
                    size = 2,
                    detach_question=True,
                    question_style="body",
                    question_x = 0,
                    question_y = -5,
                    question_size = 1,
                    question_color="green"
                    )

for i in os.listdir("./images/warmup/"):
    n.newpage()
    n.time.wait(1000)
    n.image("./images/warmup/" + i, size=3, y=7)
    answer1 = -1
    rt1 = -1
    answer1, rt1 = n.scale(y = 3.3,
                           anchors=["Not familiar", "Familiar"],
                           style = "blue",
                           analog=False,
                           edges = [1, 7],
                           labels = ["1", "2", "3", "4", "5", "6", "7"],
                           validation = False,
                           time_max=6000,
                           get_RT=True
                           )
    if rt1>6000:
            answer1 = -1
    n.newpage()
    n.image("./images/warmup/" + i, size=3, y=7)
    n.refresh()
    n.time.wait(500)
    n.newpage()
    n.image("./images/warmup/" + i, size=3, y=7)
    answer2 = -1
    rt2 = -1
    answer2, rt2 = n.scale(y = -2.3,
                           anchors=["Cannot be a word", "Could be a word"],
                           style = "blue",
                           analog=False,
                           edges = [1, 7],
                           labels = ["1", "2", "3", "4", "5", "6", "7"],
                           validation = False,
                           time_max=5000,
                           get_RT=True
                           )
    if rt2>5000:
            answer2 = -1
    warmup_familiarity.append(round(answer1))
    warmup_familiarity_time.append(rt1)
    warmup_wordiness.append(round(answer2))
    warmup_wordiness_time.append(rt2)

warmup = ["जनप्रतिनिधियों", "स्मित", "ओवरब्रिजों", "गढ़खेड़ा", "फीजियोथेरेपिस्ट"]

A = "265847367851"
B = "367851265847"
seeds = [A+A+A, B+B+B, B+A+A, B+B+A]

nonpseudo = pd.read_csv("./data/nonpseudo.csv", index_col=False)

indices = []

for i in range(6):
    curr = list(nonpseudo[nonpseudo['Label']==i+1].index.values.astype(int))
    random.shuffle(curr)
    indices.append(curr)

pseudo = pd.read_csv("./data/pseudo.csv", index_col=False)

k = 6

for i in range(2):
    curr = pseudo[pseudo['Label']==i+7].sample(frac=1).sort_values(by = 'Count')
    curr = curr[:k]
    indices.append(list(curr.index.values.astype(int)))

final_indices = []

for i in indices:
    final_indices.append([])
    for j in i:
        final_indices[-1].append(j)

loc = []
words = []

random.shuffle(seeds)

for i in seeds[0]:
    curr = int(i)
    if curr<7:
        loc.append("./images/nonpseudo/" + str(indices[curr-1][-1]) + ".png")
        words.append(nonpseudo._get_value(indices[curr-1][-1], 'String'))
        indices[curr-1].pop()
    else:
        loc.append("./images/pseudo/" + str(indices[curr-1][-1]) + ".png")
        words.append(pseudo._get_value(indices[curr-1][-1], 'String'))
        indices[curr-1].pop()

# Main Test
n.newpage()
n.write(text="MAIN",
        x = 0,
        y = 2,
        size = 2
        )
n.write(text="EXPERIMENT",
        x = 0,
        y = 0,
        size = 2
        )
n.refresh()
n.time.wait(10000)
press_enter = n.ask(text = "Press ENTER",
                    style = "body",
                    x = -10,
                    y = -10,
                    size = 2,
                    detach_question=True,
                    question_style="body",
                    question_x = 0,
                    question_y = -5,
                    question_size = 1,
                    question_color="green"
                    )

for i in range(len(loc)):
    n.newpage()
    n.time.wait(1000)
    n.image(loc[i], size=3, y=7)
    answer1 = -1
    rt1 = -1
    answer1, rt1 = n.scale(y = 3.3,
                           anchors=["Not familiar", "Familiar"],
                           style = "blue",
                           analog=False,
                           edges = [1, 7],
                           labels = ["1", "2", "3", "4", "5", "6", "7"],
                           validation = False,
                           time_max=6000,
                           get_RT=True
                           )
    if rt1>6000:
            answer1 = -1
    n.newpage()
    n.image(loc[i], size=3, y=7)
    n.refresh()
    n.time.wait(500)
    n.newpage()
    n.image(loc[i], size=3, y=7)
    answer2 = -1
    rt2 = -1
    answer2, rt2 = n.scale(y = -2.3,
                           anchors=["Cannot be a word", "Could be a word"],
                           style = "blue",
                           analog=False,
                           edges = [1, 7],
                           labels = ["1", "2", "3", "4", "5", "6", "7"],
                           validation = False,
                           time_max=5000,
                           get_RT=True
                           )
    if rt2>5000:
            answer2 = -1
    main_familiarity.append(round(answer1))
    main_familiarity_time.append(rt1)
    main_wordiness.append(round(answer2))
    main_wordiness_time.append(rt2)

# print(warmup_familiarity, warmup_familiarity_time, warmup_wordiness, warmup_wordiness_time)
# print(main_familiarity, main_familiarity_time, main_wordiness, main_wordiness_time)

words = warmup + words
familiarity = warmup_familiarity + main_familiarity
familiarity_time = warmup_familiarity_time + main_familiarity_time
wordiness = warmup_wordiness + main_wordiness
wordiness_time = warmup_wordiness_time + main_wordiness_time

out = pd.DataFrame(list(zip(words, familiarity, familiarity_time, wordiness, wordiness_time)), columns = ["word", "familiarity", "familiarity_time", "wordiness", "wordiness_time"])
out.to_csv("./results/"+roll_number + ".csv", index=False)

for i in final_indices[6:]:
    for j in i:
        pseudo.at[j, 'Count'] = pseudo.iloc[j]['Count'] + 1

pseudo.to_csv("./data/pseudo.csv", index=False)