import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import Counter

def analyze_data(data: list) -> dict:
    word_counts = Counter(data)
    return dict(word_counts.most_common(10))

def generate_report(word_counts: dict, output_path: str = "results/figures/word_frequency.png"):
    if not word_counts:
        print("No data to plot.")
        return

    df = pd.DataFrame(word_counts.items(), columns=['Word', 'Count'])
    df['Count'] = pd.to_numeric(df['Count'])
    df.set_index('Word').plot(kind='bar', title='Top 10 Words', ylabel='Frequency')
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f"Report saved to {output_path}")