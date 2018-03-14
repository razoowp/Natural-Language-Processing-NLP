import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "My name is Mr. Raju Thapa. I have done bachelor of computer application. I don't have any " \
               "word to say. He is excellent in writing articles."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))