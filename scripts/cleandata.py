import json
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Veri dosyasını oku
with open("../data/reduced-the-data-set/vehicle-failure-reduced-data-set.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# İçerik ve yorumları birleştir
all_texts = []
for entry in data:
    if entry.get('content'):
        all_texts.append(entry['content'])
    if entry.get('comments'):
        all_texts.extend(entry['comments'])

print(f"Toplam {len(all_texts)} adet açıklama+yorum işlendi.")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]
    return tokens

tokenized_corpus_lemmatized = []
tokenized_corpus_stemmed = []

for text in all_texts:
    tokens = preprocess_text(text)
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    stemmed = [stemmer.stem(token) for token in tokens]

    tokenized_corpus_lemmatized.append(lemmatized)
    tokenized_corpus_stemmed.append(stemmed)

print(f"Lemmatized corpus boyutu: {len(tokenized_corpus_lemmatized)}")
print(f"Stemmed corpus boyutu: {len(tokenized_corpus_stemmed)}")

lemmatized_df = pd.DataFrame({
    "processed_text": [" ".join(doc) for doc in tokenized_corpus_lemmatized]
})
lemmatized_df.to_csv("corpus_lemmatized.csv", index=False, encoding="utf-8")

stemmed_df = pd.DataFrame({
    "processed_text": [" ".join(doc) for doc in tokenized_corpus_stemmed]
})
stemmed_df.to_csv("corpus_stemmed.csv", index=False, encoding="utf-8")

print("\n📁 Temizlenmiş korpuslar CSV formatında başarıyla kaydedildi.")
