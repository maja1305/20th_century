# Reusable plotting functions
import matplotlib.pyplot as plt
import seaborn as sns

def top_n_barplot(data, x, y, title, figsize=(8,4), palette="mako"):

    plt.figure(figsize=figsize)
    sns.barplot(x=x, y=y, data=data, palette=palette)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()