import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "..", "data", "tf-idf-score")
os.makedirs(data_dir, exist_ok=True)

lemmatized_path = os.path.join(data_dir, "corpus_lemmatized.csv")
stemmed_path = os.path.join(data_dir, "corpus_stemmed.csv")

lemmatized_df = pd.read_csv(lemmatized_path)
stemmed_df = pd.read_csv(stemmed_path)

lemmatized_df['processed_text'] = lemmatized_df['processed_text'].fillna('')
stemmed_df['processed_text'] = stemmed_df['processed_text'].fillna('')

lemmatized_texts = lemmatized_df['processed_text'].tolist()
stemmed_texts = stemmed_df['processed_text'].tolist()

def create_tfidf_matrix(texts, max_features=None):
    """
    Metinler için TF-IDF vektörleştirme yapar ve DataFrame olarak döndürür
    """
    vectorizer = TfidfVectorizer(max_features=max_features)
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
    return tfidf_df, tfidf_matrix, feature_names

print("Lemmatized veri için TF-IDF hesaplanıyor...")
lemmatized_tfidf_df, lemmatized_tfidf_matrix, lemmatized_features = create_tfidf_matrix(lemmatized_texts)
lemmatized_csv_path = os.path.join(data_dir, "tfidf_lemmatized.csv")
lemmatized_tfidf_df.to_csv(lemmatized_csv_path, index=False, encoding="utf-8")
print(f"✅ Lemmatized TF-IDF kaydedildi → {lemmatized_csv_path}")

print("Stemmed veri için TF-IDF hesaplanıyor...")
stemmed_tfidf_df, stemmed_tfidf_matrix, stemmed_features = create_tfidf_matrix(stemmed_texts)
stemmed_csv_path = os.path.join(data_dir, "tfidf_stemmed.csv")
stemmed_tfidf_df.to_csv(stemmed_csv_path, index=False, encoding="utf-8")
print(f"✅ Stemmed TF-IDF kaydedildi → {stemmed_csv_path}")

if not lemmatized_tfidf_df.empty:
    print("\n🔎 Lemmatized - İlk açıklamadaki en önemli 5 kelime (TF-IDF):")
    top5 = lemmatized_tfidf_df.iloc[0].sort_values(ascending=False).head(5)
    print(top5)

def analyze_word_similarity(tfidf_matrix, feature_names, target_word, top_n=5):
    """
    Belirli bir kelimeye en benzer kelimeleri bulur
    """
    if target_word not in feature_names:
        print(f"⚠️ '{target_word}' kelimesi bulunamadı.")
        return

    index = feature_names.tolist().index(target_word)
    word_vector = tfidf_matrix[:, index].toarray()
    all_vectors = tfidf_matrix.toarray()
    similarities = cosine_similarity(word_vector.T, all_vectors.T).flatten()
    top_indices = similarities.argsort()[-(top_n + 1):][::-1]

    print(f"\n🔗 '{target_word}' kelimesine en benzer {top_n} kelime:")
    for idx in top_indices:
        if feature_names[idx] == target_word:
            continue
        print(f"{feature_names[idx]}: {similarities[idx]:.4f}")

sample_word = "engine"
analyze_word_similarity(lemmatized_tfidf_matrix, lemmatized_features, sample_word)

analyze_word_similarity(stemmed_tfidf_matrix, stemmed_features, sample_word)
