import json
from gensim.models import Word2Vec

with open("corpus_lemmatized.json", "r", encoding="utf-8") as f:
    tokenized_corpus_lemmatized = json.load(f)

with open("corpus_stemmed.json", "r", encoding="utf-8") as f:
    tokenized_corpus_stemmed = json.load(f)

datasets = [
    ("lemma", tokenized_corpus_lemmatized),
    ("stem", tokenized_corpus_stemmed)
]

windows = [2, 5]
vector_sizes = [100, 300]
sg_values = [0, 1] 

print("\nModel eğitimleri başlıyor...\n")

for corpus_name, corpus_data in datasets:
    for window in windows:
        for vector_size in vector_sizes:
            for sg in sg_values:
                model = Word2Vec(
                    sentences=corpus_data,
                    vector_size=vector_size,
                    window=window,
                    sg=sg,
                    min_count=2,
                    workers=4
                )
                model_name = f"word2vec_{corpus_name}_win{window}_dim{vector_size}_{'sg' if sg else 'cbow'}.model"
                model.save(model_name)
                print(f"✅ Kaydedildi: {model_name}")

print("\nTüm 16 model başarıyla oluşturuldu.")
