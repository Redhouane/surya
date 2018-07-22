#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-

import pytextrank as ptr


# Stage 1

path_stage0 = "../Tests/pytextrank_dat/mih.json"
path_stage1 = "../Tests/pytextrank_dat/o1.json"

with open(path_stage1, 'w') as f:
    for graf in ptr.parse_doc(ptr.json_iter(path_stage0)):
        f.write("%s\n" % ptr.pretty_print(graf._asdict()))


# Stage 2
path_stage2 = "../Tests/pytextrank_dat/o2.json"

graph, ranks = ptr.text_rank(path_stage1)
ptr.render_ranks(graph, ranks)

with open(path_stage2, 'w') as f:
    for rl in ptr.normalize_key_phrases(path_stage1, ranks):
        f.write("%s\n" % ptr.pretty_print(rl._asdict()))


# Stage 3
import networkx as nx
import pylab as plt

nx.draw(graph, with_labels=True)
plt.show()

path_stage3 = "../Tests/pytextrank_dat/o3.json"
path_stage2 = "../Tests/pytextrank_dat/o2.json"

kernel = ptr.rank_kernel(path_stage2)

with open(path_stage3, 'w') as f:
    for s in ptr.top_sentences(kernel, path_stage1):
        f.write(ptr.pretty_print(s._asdict()))
        f.write("\n")

# Stage 4
phrases = ", ".join(set([p for p in ptr.limit_keyphrases(path_stage2, phrase_limit=12)]))
sent_iter = sorted(ptr.limit_sentences(path_stage3, word_limit=150), key=lambda x: x[1])
s = []

for sent_text, idx in sent_iter:
    s.append(ptr.make_sentence(sent_text))

graf_text = " ".join(s)
print("**excerpts:** %s\n\n**keywords:** %s" % (graf_text, phrases,))
