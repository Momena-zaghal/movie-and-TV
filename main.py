import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Windows 10 Pro\Desktop\archive\imdb_top_1000.csv')

print(df.columns)

df = df.drop([3, 5], axis=0)

if 'Genre' in df.columns:
    genre_counts = df['Genre'].value_counts()
    genre_df = pd.DataFrame({'Genre': genre_counts.index, 'Count': genre_counts.values})

    plt.figure(figsize=(10, 6))
    plt.bar(genre_df['Genre'], genre_df['Count'])
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.title('Most Popular Genre of Movies/TV Shows')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Genre column not found in the DataFrame.")

if 'Director' in df.columns:
    director_counts = df['Director'].value_counts()
    director_df = pd.DataFrame({'Director': director_counts.index, 'Count': director_counts.values})

    plt.figure(figsize=(10, 6))
    plt.bar(director_df['Director'][:10], director_df['Count'][:10])
    plt.xlabel('Director')
    plt.ylabel('Count')
    plt.title('Director with the Most Top-Rated Movies/TV Shows')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Director column not found in the DataFrame.")
