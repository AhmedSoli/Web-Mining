import os
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

nltk.download('stopwords')

st = LancasterStemmer()
stop_words = set(stopwords.words('english'))

for fileName in os.listdir('solution_one'):
    file = open('solution_one/' + fileName,encoding="utf8")
    try :
        line = file.read()
        words = line.split()
        for word in words:
            if not word in stop_words:
                filteredFile = open('solution_two/' + fileName, 'w')
                filteredFile.write(" "+st.stem(word))
                filteredFile.close()
    except UnicodeDecodeError:
        print("unicode error")
    except NameError:
        print("nameerror")
        
docs = []
        
for fileName in os.listdir('solution_two'):
    file = open('solution_two/' + fileName,encoding="utf8")
    try:
        docs.append(file.read())
    except UnicodeDecodeError:
        print("unicode error")
        
vec = CountVectorizer()
X = vec.fit_transform(docs)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
print(df)