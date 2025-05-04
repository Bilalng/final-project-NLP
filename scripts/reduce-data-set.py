import json
import random

INPUT_FILE = "reddit_ariza_verisi_100000.json"
OUTPUT_FILE = "kucuk_veri.json"

TARGET_RECORD_COUNT = 4000

# Veriyi yükle
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"🔍 Orijinal kayıt sayısı: {len(data)}")

# Verileri karıştır ve hedef kadar seç
random.shuffle(data)
reduced_data = data[:TARGET_RECORD_COUNT]

# Yeni veriyi kaydet
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(reduced_data, f, ensure_ascii=False, indent=2)

print(f"✅ {TARGET_RECORD_COUNT} kayıt kaydedildi → {OUTPUT_FILE}")
