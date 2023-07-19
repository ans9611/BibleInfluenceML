import nltk
nltk.download('stopwords')
import glob
from nltk.corpus import stopwords

# ... (rest of your code)


data = [] 
ifiles = glob.glob("books/*.txt")
for ifile in ifiles: 
    book = open(ifile, "r").read().strip() 
    data.append(book)

stop_words = stopwords.words('english')
stop_words.extend(["thy","thou","thee", "hath", "upon", "me", "him", "them", "shall","ye", "one", "unto", "us"])


def remove_stopwords(text, stop_words):
    outtext = ' '.join([word for word in text.split() if word not in stop_words])
    return outtext


for i, book in enumerate(data, 0):
    # remove NUMBER:NUMBER. pattern at the beginning
    data[i] = re.sub(r"\d{1,}\:\d{1,}\.", "",data[i])
    # remove NAME Chapter NUMBER 
    data[i] = re.sub(r"\w{1,} Chapter \d{1,}","",data[i] )
    #lower case 
    data[i] = data[i].lower() 
    # remove punctuation 
    data[i] = data[i].translate(str.maketrans('', '', string.punctuation))
    # remove new lines 
    data[i] = re.sub('\s+', " ", data[i]) 
    # remove new line
    data[i] = re.sub(r"\\n", " ", data[i])
    # remove stopwords 
    data[i] = ' '.join([word for word in data[i].split() if word not in stop_words]) #remove_stopwords(data[i], stop_words)
