import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Movie": [
        "Avengers: Endgame", "Frozen II", "Interstellar", "The Dark Knight", 
        "Inception", "Toy Story 4", "Joker", "Spider-Man: No Way Home", 
        "The Lion King", "Avatar", "Titanic", "The Matrix", 
        "Jurassic Park", "Finding Nemo", "The Godfather", 
        "Pulp Fiction", "Forrest Gump", "The Shawshank Redemption", 
        "Gladiator", "The Social Network"
    ],
    "Genre": [
        "Action", "Animation", "Sci-Fi", "Action", 
        "Sci-Fi", "Animation", "Drama", "Action", 
        "Animation", "Sci-Fi", "Drama", "Sci-Fi", 
        "Action", "Animation", "Drama", 
        "Drama", "Drama", "Drama", 
        "Action", "Drama"
    ],
    "Rating": [
        8.4, 7.8, 8.6, 9.0, 
        8.8, 7.7, 8.4, 8.2, 
        8.5, 7.9, 7.9, 8.7, 
        8.1, 8.1, 9.2, 
        8.9, 8.8, 9.3, 
        8.5, 7.8
    ],
    "Views": [
        150000, 90000, 120000, 180000,
        110000, 85000, 95000, 200000,
        100000, 140000, 130000, 105000,
        115000, 88000, 160000,
        125000, 135000, 170000,
        108000, 92000
    ]
}

df = pd.DataFrame(data)

print("NETFLIX MOVIE RATINGS DATASET")
print("="*60)
print(df)
print("\n" + "="*60)

print("\nTotal number of netflix movies:", len(df))

highest = df.loc[df["Rating"].idxmax()]
print(f"Highest rated movie: {highest['Movie']} (Rating: {highest['Rating']})")

lowest = df.loc[df["Rating"].idxmin()]
print(f"Lowest rated movie: {lowest['Movie']} (Rating: {lowest['Rating']})")

avg_rating = df["Rating"].mean()
print(f"Average rating of all movies: {avg_rating:.2f}")

print("\nTop 5 movies by views:")
top5_views = df.nlargest(5, "Views")
for idx, row in top5_views.iterrows():
    print(f"   - {row['Movie']} - {row['Views']:,} views (Rating: {row['Rating']})")

print("\nMovies count by genre:")
genre_counts = df["Genre"].value_counts()
for genre, count in genre_counts.items():
    print(f"   - {genre}: {count} movie(s)")

print("\nAverage rating by genre:")
genre_avg = df.groupby("Genre")["Rating"].mean().round(2)
for genre, avg in genre_avg.items():
    print(f"   - {genre}: {avg}")

print("\n" + "="*60)
print("BONUS INSIGHTS")
print("="*60)

most_popular = genre_counts.idxmax()
print(f"Most popular genre: {most_popular} ({genre_counts[most_popular]} movies)")

best_genre = genre_avg.idxmax()
print(f"Highest rated genre: {best_genre} (Avg: {genre_avg[best_genre]})")

print("\nBest movie in each genre:")
for genre in df["Genre"].unique():
    best = df[df["Genre"] == genre].loc[df[df["Genre"] == genre]["Rating"].idxmax()]
    print(f"   - {genre}: {best['Movie']} (Rating: {best['Rating']})")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

genre_counts.plot(kind="bar", ax=ax1, color='skyblue', edgecolor='black')
ax1.set_title("Number of Movies by Genre", fontsize=14, fontweight='bold')
ax1.set_xlabel("Genre")
ax1.set_ylabel("Number of Movies")
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
ax1.grid(axis='y')

genre_avg.plot(kind="bar", ax=ax2, color='lightcoral', edgecolor='black')
ax2.set_title("Average Rating by Genre", fontsize=14, fontweight='bold')
ax2.set_xlabel("Genre")
ax2.set_ylabel("Average Rating")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
ax2.set_ylim(7.5, 9.5)
ax2.grid(axis='y')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

colors = {'Action': 'red', 'Animation': 'blue', 'Sci-Fi': 'green', 'Drama': 'purple'}
scatter = plt.scatter(df['Views'], df['Rating'], 
                     c=[colors[genre] for genre in df['Genre']], 
                     s=100, edgecolors='black')

for i, row in df.iterrows():
    plt.annotate(row['Movie'], (row['Views'], row['Rating']), 
                fontsize=8, ha='center', va='bottom')

plt.title("Movie Ratings vs Views (Colored by Genre)", fontsize=14, fontweight='bold')
plt.xlabel("Number of Views")
plt.ylabel("Rating")
plt.grid()

handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, 
                      markersize=10, label=genre) for genre, color in colors.items()]
plt.legend(handles=handles)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ANALYSIS SUMMARY")
print("="*60)
print(f"- Total movies analyzed: {len(df)}")
print(f"- Overall average rating: {avg_rating:.2f}")
print(f"- Highest rated: {highest['Movie']} ({highest['Rating']})")
print(f"- Lowest rated: {lowest['Movie']} ({lowest['Rating']})")
print(f"- Most viewed: {top5_views.iloc[0]['Movie']} with {top5_views.iloc[0]['Views']:,} views")
print(f"- Most common genre: {most_popular} ({genre_counts[most_popular]} movies)")
print(f"- Highest rated genre: {best_genre} (Avg: {genre_avg[best_genre]})")
print("="*60)
print("Analysis complete!")