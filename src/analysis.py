import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize

with open('../data/bible.txt', 'r') as file:
    text = file.read()

# Tokenize the text into words
tokens = word_tokenize(text)

# Create a frequency distribution of words
freqDist = FreqDist(tokens)

# Get the most common 10 words
mostCommonWords = freqDist.most_common(10)

# Print the most common words and frequencies
for word, freq in mostCommonWords:
    print(word, freq)
    
    