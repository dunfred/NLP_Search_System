import re
import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

qoute = re.compile(r"[`|('')]")
brw = sent_tokenize(" ".join([qoute.sub('',i) for i in brown.words()[:500]]))
brw


search = input("Your search: ")

new_tokens = nltk.pos_tag(word_tokenize(search))

filtered_string = []
for word in new_tokens:
    if word[1] in ["NNP","NN","NP","NNS","VBN","VBG"]:
        filtered_string.append(word[0])

print("Your search reults for",[print(i, end=" ") for i in filtered_string])

search_query = []

for sentence in brw:
    for word in filtered_string:
        if word.lower() in sentence.lower():
            search_query.append(sentence)

search_query = set(search_query)
[print(i,"\n\n") for i in search_query]