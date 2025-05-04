import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1️⃣ Temizlenmiş veriyi oku (lemmatized olan)
with open("corpus_lemmatized.json", "r", encoding="utf-8") as f:
    corpus = json.load(f)

# 2️⃣ Token listelerini tekrar metin haline getir
lemmatized_texts = [' '.join(tokens) for tokens in corpus]

# 3️⃣ Metinleri CSV olarak kaydet (her satır bir metin)
df_texts = pd.DataFrame(lemmatized_texts, columns=["text"])
df_texts.to_csv("lemmatized_texts.csv", index=False, encoding="utf-8")
print("📄 Token'lar metinleştirilip kaydedildi → lemmatized_texts.csv")

# 4️⃣ TF-IDF işlemi
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(lemmatized_texts)

# 5️⃣ Özellik isimlerini al ve TF-IDF skorlarını DataFrame'e çevir
feature_names = vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# 6️⃣ TF-IDF skorlarını CSV olarak kaydet
tfidf_df.to_csv("tfidf_scores.csv", index=False, encoding="utf-8")
print("📊 TF-IDF skorları kaydedildi → tfidf_scores.csv")

# 7️⃣ İlk cümledeki en yüksek TF-IDF skorlu 5 kelime
first_sentence_vector = tfidf_df.iloc[0]
top_5_words = first_sentence_vector.sort_values(ascending=False).head(5)

print("\n🔎 İlk açıklamadaki en önemli 5 kelime (TF-IDF):")
print(top_5_words)

# 8️⃣ "engine" kelimesine en benzer kelimeleri bul
target_word = "engine"
try:
    index = feature_names.tolist().index(target_word)
    word_vector = tfidf_matrix[:, index].toarray()
    all_vectors = tfidf_matrix.toarray()
    similarities = cosine_similarity(word_vector.T, all_vectors.T).flatten()
    top_indices = similarities.argsort()[-6:][::-1]

    print(f"\n🔗 '{target_word}' kelimesine en benzeyen kelimeler:")
    for idx in top_indices:
        print(f"{feature_names[idx]}: {similarities[idx]:.4f}")
except ValueError:
    print(f"\n⚠️ Kelime bulunamadı: {target_word}")
