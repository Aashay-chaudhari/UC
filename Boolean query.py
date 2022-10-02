import sys

# Import the data
# read lines gives an array which has 1 line as every element of array
f = open('bible.txt', 'r')
docs = f.readlines()
f.close()

word1 = "god"
word2 = "punish"

# The vanilla way of doing retrieval ( takes more time )
# for i in range(len(docs)):
#     if word1 in docs[i] and word2 in docs[i]:
#         print(i, docs[i])

# Create inverted index
invertedIndex = {}

invertedIndex = {}
for i in range(len(docs)):
    for s in docs[i].split():
        if invertedIndex.get(s) is None:
            invertedIndex[s] = {i}
        else:
            invertedIndex.get(s).add(i)

word1 = 'LORD;'
word2 = 'transgressions'
for j in invertedIndex.get(word1) & invertedIndex.get(word2):
    print(j, docs[j])
