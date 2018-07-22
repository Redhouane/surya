#!/Users/redhouaneabdellaoui/anaconda/envs/DrEA/bin/python python
# -*- coding: utf-8 -*-


from pyteaser import Summarize


text = """
(Reuters) - Twitter Inc said it has implemented a security technology that makes it harder to spy on its users and called on other Internet firms to do the same, as Web providers look to thwart spying by government intelligence agencies.

The online messaging service, which began scrambling communications in 2011 using traditional HTTPS encryption, said on Friday it has added an advanced layer of protection for HTTPS known as “forward secrecy.”

“A year and a half ago, Twitter was first served completely over HTTPS,” the company said in a blog posting. “Since then, it has become clearer and clearer how important that step was to protecting our users’ privacy.”

Twitter’s move is the latest response from U.S. Internet firms following disclosures by former spy agency contractor Edward Snowden about widespread, classified U.S. government surveillance programs.

Facebook Inc, Google Inc, Microsoft Corp and Yahoo Inc have publicly complained that the government does not let them disclose data collection efforts. Some have adopted new privacy technologies to better secure user data.

Forward secrecy prevents attackers from exploiting one potential weakness in HTTPS, which is that large quantities of data can be unscrambled if spies are able to steal a single private “key” that is then used to encrypt all the data, said Dan Kaminsky, a well-known Internet security expert.

The more advanced technique repeatedly creates individual keys as new communications sessions are opened, making it impossible to use a master key to decrypt them, Kaminsky said.

“It is a good thing to do,” he said. “I’m glad this is the direction the industry is taking.”

(Reporting by Jim Finkle; editing by Andrew Hay)
"""

# url = 'http://www.huffingtonpost.com/2013/11/22/twitter-forward-secrecy_n_4326599.html'

titre = "Twitter’s ‘Forward Secrecy’ Takes Step To Make It Harder To Spy On Its Users"
key_phrases = Summarize(titre, text)

summary = '\n'.join(key_phrases)

print('\n')
print(summary)
