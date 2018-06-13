from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

myexample = "this is an example showing how a person uses stopwords in his program"

stopwords = set(stopwords.words('english'))

tokenize_words = word_tokenize(myexample)

filtered_words = []

for w in tokenize_words:
    if w not in stopwords:
        filtered_words.append(w)


print(filtered_words)

#OR::

filtered_words = [w for w in tokenize_words if not w in stopwords]
print(filtered_words)