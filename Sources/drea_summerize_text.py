#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


# Stage 1
import pytextrank
import sys


path_stage0 = "../Tests/pytextrank_dat/mih.json"
path_stage1 = "../Tests/pytextrank_dat/o1.json"

with open(path_stage1, 'w') as f:
   for graf in pytextrank.parse_doc(pytextrank.json_iter(path_stage0)):
       f.write("%s\n" % pytextrank.pretty_print(graf._asdict()))
       print(pytextrank.pretty_print(graf))


# Stage 2
path_stage2 = "../Tests/pytextrank_dat/o2.json"

graph, ranks = pytextrank.text_rank(path_stage1)
pytextrank.render_ranks(graph, ranks)

with open(path_stage2, 'w') as f:
   for rl in pytextrank.normalize_key_phrases(path_stage1, ranks):
       f.write("%s\n" % pytextrank.pretty_print(rl._asdict()))
       # to view output in this notebook
       print(pytextrank.pretty_print(rl))


# Stage 3
import networkx as nx
import pylab as plt

nx.draw(graph, with_labels=True)
plt.show()

path_stage3 = "../Tests/pytextrank_dat/o3.json"

kernel = pytextrank.rank_kernel(path_stage2)

with open(path_stage3, 'w') as f:
     for s in pytextrank.top_sentences(kernel, path_stage1):
         f.write(pytextrank.pretty_print(s._asdict()))
         f.write("\n")
         # to view output in this notebook
         print(pytextrank.pretty_print(s._asdict()))


# Stage 4
phrases = ", ".join(set([p for p in pytextrank.limit_keyphrases(path_stage2, phrase_limit=12)]))
sent_iter = sorted(pytextrank.limit_sentences(path_stage3, word_limit=150), key=lambda x: x[1])
s = []

for sent_text, idx in sent_iter:
    s.append(pytextrank.make_sentence(sent_text))

graf_text = " ".join(s)
print("**excerpts:** %s\n\n**keywords:** %s" % (graf_text, phrases,))
