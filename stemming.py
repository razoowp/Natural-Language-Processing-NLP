from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


words = ['python', 'pythoner', 'pythoning', 'pythonly']

ps = PorterStemmer()

for w in words:
    print(ps.stem(w))

mysentence = "Lots of dishes out there, broken. I am very much interested to go for swimming , and eagerly waiting for that. I am not feeling lonly."

tokenize_words = word_tokenize(mysentence)

for w in tokenize_words:
    print(ps.stem(w))