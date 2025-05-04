# Doğal Dil İşleme ile Araç Arıza Analizi

## Proje Genel Bakış

Bu proje, Reddit'ten toplanan araç arızaları ile ilgili tartışmaları analiz etmek için Doğal Dil İşleme (NLP) tekniklerini uygulamaktadır. Uygulama, metin ön işleme, Zipf yasası analizi, TF-IDF vektörleştirme ve araç arıza açıklamaları üzerinde farklı parametrelerle eğitilen çoklu Word2Vec modellerini içermektedir.

## Proje Amaçları

Reddit'ten toplanan araç arıza veri seti şunlar için kullanılabilir:

- Araç arıza tartışmalarındaki yaygın kalıpları ve trendleri analiz etme
- Otomotiv problem açıklamalarının dilbilimsel özelliklerini anlama
- Otomotiv forumları için anlamsal arama yetenekleri geliştirme
- Arıza açıklamalarına dayalı öneri sistemleri oluşturma
- Metinsel açıklamalara dayalı benzer araç problemlerini tanımlama
- Araç arıza raporlarından önemli özellikleri ve belirtileri çıkarma

## Depo Yapısı

```
.
├── data/
│   ├── cleaned-reduced-data-set/         # Temizlenmiş ve ön işlenmiş veri
│   │   ├── corpus_lemmatized.csv
│   │   └── corpus_stemmed.csv
│   ├── processed/                        # İşlenmiş veri dosyaları
│   ├── raw-data-set/                     # Reddit'ten alınan ham JSON verisi
│   ├── reduced-the-data-set/             # Filtrelenmiş/azaltılmış veri seti
│   ├── similar_words/                    # Kelime benzerliği çıktıları
│   └── tf-idf-score/                     # TF-IDF vektörleştirme sonuçları
├── models/                               # Eğitilmiş Word2Vec modelleri
├── plots/                                # Oluşturulmuş görselleştirmeler 
└── scripts/                              # Veri işleme için Python Kodları
```

## Kurulum ve Ayarlar

### Ön Koşullar

- Python 3.8 veya daha üst sürümü

### Ortam Kurulumu

1. Sanal ortam oluşturun:
   ```bash
   python -m venv venv
   ```

2. Sanal ortamı etkinleştirin:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Veri İşleme Adımları

### 1. Veri Toplama

Proje, Reddit'ten araç arıza tartışmalarının toplanmasıyla başlar:

```bash
python scripts/recieve-data-in-reddit.py
```

### 2. Veri Azaltma

Veri setini ilgili araç arıza içeriğine odaklanacak şekilde filtreleme ve azaltma:

```bash
python scripts/reduce-data-set.py
```

### 3. Veri Ön İşleme

Metin verilerini temizleme ve ön işleme:

```bash
python scripts/cleandata.py
```

Bu adım şunları içerir:
- Metin temizleme
- Tokenizasyon
- Durak kelimeleri (stop words) kaldırma
- Lemmatizasyon ve kök bulma (stemming) (iki ayrı veri seti oluşturma)

### 4. Zipf Analizi

Korpustaki kelime frekans dağılımlarını analiz etme:

```bash
python scripts/ziph_analysis.py
```

### 5. TF-IDF Vektörleştirme

Metnin TF-IDF temsillerini oluşturma:

```bash
python scripts/tfidf_vectorizater.py
```

### 6. Word2Vec Model Eğitimi

Farklı parametrelerle çoklu Word2Vec modellerini eğitme:

```bash
python scripts/create_model.py
```

Eğitim süreci şunları içerir:
- CBOW ve Skip-gram mimarileri
- Farklı pencere boyutları (2 ve 5)
- Çeşitli vektör boyutları (100 ve 300)
- Hem lemmatize edilmiş hem de kökleri bulunan (stemmed) versiyonlar

### 7. Model Değerlendirme

Eğitilen modelleri değerlendirme:

```bash
python scripts/modeltest.py
```

## Word2Vec Modelleri

Proje, farklı parametrelerle eğitilmiş 16 farklı Word2Vec modelini içermektedir:

| Model Tipi | Pencere Boyutu | Vektör Boyutu | Mimari    | Metin İşleme  |
|------------|----------------|---------------|-----------|---------------|
| Word2Vec   | 2              | 100           | CBOW      | Lemmatized    |
| Word2Vec   | 2              | 100           | Skip-gram | Lemmatized    |
| Word2Vec   | 2              | 300           | CBOW      | Lemmatized    |
| Word2Vec   | 2              | 300           | Skip-gram | Lemmatized    |
| Word2Vec   | 5              | 100           | CBOW      | Lemmatized    |
| Word2Vec   | 5              | 100           | Skip-gram | Lemmatized    |
| Word2Vec   | 5              | 300           | CBOW      | Lemmatized    |
| Word2Vec   | 5              | 300           | Skip-gram | Lemmatized    |
| Word2Vec   | 2              | 100           | CBOW      | Stemmed       |
| Word2Vec   | 2              | 100           | Skip-gram | Stemmed       |
| Word2Vec   | 2              | 300           | CBOW      | Stemmed       |
| Word2Vec   | 2              | 300           | Skip-gram | Stemmed       |
| Word2Vec   | 5              | 100           | CBOW      | Stemmed       |
| Word2Vec   | 5              | 100           | Skip-gram | Stemmed       |
| Word2Vec   | 5              | 300           | CBOW      | Stemmed       |
| Word2Vec   | 5              | 300           | Skip-gram | Stemmed       |

## Görselleştirmeler

Proje birkaç görselleştirme içerir:

- Kelime frekans dağılımları (Zipf yasası)
- Word2Vec vektör gösterimleri
- Kelime dağarcığı boyutu karşılaştırmaları
- Model performans metrikleri

Bu görselleştirmeleri `plots/` dizininde görüntüleyebilirsiniz.

## Notlar

- Büyük dosyalar (>100MB) depodan hariç tutulmuştur.
- Tüm modeller, araç arızalarına odaklanan temizlenmiş ve ön işlenmiş bir Reddit veri alt kümesi üzerinde eğitilmiştir.
- Köklenmiş (stemmed) ve lemmatize edilmiş veri setleri, aynı metinsel içerik üzerinde farklı perspektifler sunar.


