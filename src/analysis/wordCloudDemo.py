import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open("../../data/bible_corpus.txt", "r") as file:
   big_string = file.read()
    
wordcloud = WordCloud(width=1600, height=800,max_font_size=200).generate(big_string)
plt.figure(figsize=(12,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

output_image_file = "../../data/wordcloudDemo.png"
plt.savefig(output_image_file, bbox_inches='tight')

# Display a message to confirm successful saving
print(f"Word cloud image saved to {output_image_file}")
