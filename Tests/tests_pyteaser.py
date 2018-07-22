#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


from pyteaser import SummarizeUrl


url = 'http://www.huffingtonpost.com/2013/11/22/twitter-forward-secrecy_n_4326599.html'
key_phrases = SummarizeUrl(url)
summary = '\n'.join(key_phrases)

print('\n')
print(summary)
