import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Read the text file

with open('../data/bible.txt', 'r') as file:
    text = file.read()

# Tokenize the text into words
tokens = word_tokenize(text)

# Print the first 10 tokens
print(tokens[:10])
