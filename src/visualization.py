from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the text file
with open('../data/bible.txt', 'r') as file:
    text = file.read()

# Generate a word cloud
wordcloud = WordCloud().generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
