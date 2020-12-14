from nltk.tokenize import WhitespaceTokenizer
import nltk
import collections
import random

#with open("insert text file here!! The more lines the more accurate the sentences!!", "r", encoding="utf-8") as f:
with open("corpus.txt", "r", encoding="utf-8") as f:
    tokens = WhitespaceTokenizer().tokenize(f.read())
    trigram = nltk.trigrams(tokens)
    trigram = [x for x in map(' '.join, trigram)]

    x = 0
    while x < 10:
        complete = False
        sentence = []
        word = random.choice(trigram).split(" ")[:2]
        if word[0][0].isupper() and not any([word[y].endswith(x) for x in [".", "?", "!"] for y in range(2)]):
            word = " ".join(word)
            while complete is False:
                dct = collections.defaultdict(int)
                for i in trigram:
                    if word == " ".join(i.split(" ")[:2]):
                        dct[" ".join(i.split(" ")[1:3])] += 1
                dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
                dct_word = [x for x in dct.keys()][0]
                sentence.append(word.split(" ")[0])
                if any([sentence[-1].endswith(x) for x in [".", "?", "!"]]):
                    if len(sentence) >= 5:
                        print(" ".join(sentence))
                        complete = True
                        continue
                word = dct_word
            x += 1
