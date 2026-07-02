import pandas as pd

data = {
    "Movie": [
        "Inception", "Avatar", "Titanic", "Interstellar", "Joker",
        "Avengers", "Frozen", "The Batman", "Dune", "Oppenheimer"
    ],
    "Genre": [
        "Sci-Fi", "Action", "Romance", "Sci-Fi", "Drama",
        "Action", "Animation", "Action", "Sci-Fi", "Biography"
    ],
    "Rating": [8.8, 7.9, 7.8, 8.7, 8.4, 8.0, 7.5, 7.9, 8.3, 8.6],
    "Votes": [2200000, 1300000, 1200000, 1800000, 1500000,
              1700000, 700000, 900000, 850000, 1100000],
    "Revenue_Million": [836, 2923, 2264, 701, 1074,
                        2798, 1453, 770, 402, 975],
    "Year": [2010, 2009, 1997, 2014, 2019,
             2012, 2013, 2022, 2021, 2023]
}

df = pd.DataFrame(data)
df

df.head()

df.tail()

df.shape

df.columns

df.info()

df.describe()

highest_Year = df.loc[df["Year"].idxmax()]
Lowest_Year = df.loc[df["Year"].idxmin()]
highest_Rating = df.loc[df["Rating"].idxmax()]
lowest_Rating = df.loc[df["Rating"].idxmin()]
highest_Revenue_Million = df.loc[df["Revenue_Million"].idxmax()]
Lowest_Revenue_Million = df.loc[df["Revenue_Million"].idxmin()]
highest_Votes = df.loc[df["Votes"].idxmax()]
lowest_Vote = df.loc[df["Votes"].idxmin()]

print("Newest year: \n", highest_Year)
print("Oldest year: \n", Lowest_Year)
print("Highest Rating: \n", highest_Rating)
print("Lowest Rating: \n", lowest_Rating)
print("Highest Revenue: \n", highest_Revenue_Million)
print("Lowest Revenue: \n", Lowest_Revenue_Million)
print("Highest Votes: \n", highest_Votes)
print("Lowest Votes: \n", lowest_Vote)

# Total revenue
total_revenue = df["Revenue_Million"].sum()
total_revenue

#Average rating by Genre
average_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(average_rating_by_genre)
#Total revenue by Genre
Total_revenue_by_genre = df.groupby("Genre")["Revenue_Million"].sum()
print(Total_revenue_by_genre)
#Total votes by Genre
Total_votes_by_genre = df.groupby("Genre")["Votes"].sum()
print(Total_votes_by_genre)

# Bar plot
import matplotlib.pyplot as plt
df.groupby("Genre")["Rating"].mean().plot(kind="bar")
plt.xlabel("Genre")
plt.ylabel("Rating")
plt.title("Average Rating by Genre")
plt.show()

# pie chart
df.groupby("Genre")["Revenue_Million"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue by Genre")
plt.show()

# Scatter Plot (Revenue vs Rating)
df.plot(kind="scatter", x="Revenue_Million", y="Rating", title="Revenue vs Rating")
plt.xlabel("Revenue (Million)")
plt.ylabel("Rating")
plt.grid(True)
plt.show()

# Line Chart
df.plot(kind="line", x="Year", y="Rating", title="Rating Over Time")
plt.xlabel("Year")
plt.ylabel("Rating")
plt.grid(True)
plt.show()

# Box Plot
df.boxplot(column="Rating", by="Genre")
plt.xlabel("Genre")
plt.ylabel("Rating")
plt.title("Box Plot of Rating by Genre")
plt.show()

df.to_csv("Movie-Ratings-Analysis.csv", index=False)
