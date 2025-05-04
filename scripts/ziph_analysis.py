import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

base_dir = os.path.dirname(os.path.abspath(__file__))
processed_dir = os.path.join(base_dir, "..", "data", "cleaned-reduced-data-set")
plots_dir = os.path.join(base_dir, "..", "plots")
os.makedirs(plots_dir, exist_ok=True)

lemmatized_df = pd.read_csv(os.path.join(processed_dir, "corpus_lemmatized.csv"))
stemmed_df = pd.read_csv(os.path.join(processed_dir, "corpus_stemmed.csv"))

def flatten_tokens(df):
    all_text = " ".join(df['processed_text'].dropna().astype(str).tolist())
    return all_text.split()

lemmatized_tokens = flatten_tokens(lemmatized_df)
stemmed_tokens = flatten_tokens(stemmed_df)

def plot_zipf(tokens, title, filename):
    word_counts = Counter(tokens)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    ranks = np.arange(1, len(sorted_word_counts) + 1)
    frequencies = [count for _, count in sorted_word_counts]

    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, marker='.', linestyle='none', label='Gerçek')

    k = frequencies[0]
    theoretical_zipf = [k / r for r in ranks]
    plt.loglog(ranks, theoretical_zipf, 'r-', alpha=0.7, label='Teorik Zipf (1/rank)')

    plt.title(title)
    plt.xlabel('Rank (log scale)')
    plt.ylabel('Frequency (log scale)')
    plt.legend()
    plt.grid(True, alpha=0.3)

    output_path = os.path.join(plots_dir, filename)
    plt.savefig(output_path)
    plt.close()
    print(f"Zipf grafiği kaydedildi: {output_path}")
    return output_path

plot_zipf(lemmatized_tokens, "Zipf Analizi - Lemmatized Veri", "zipf_lemmatized.png")
plot_zipf(stemmed_tokens, "Zipf Analizi - Stemmed Veri", "zipf_stemmed.png")
