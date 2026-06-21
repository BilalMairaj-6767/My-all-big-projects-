import pandas as pd
import matplotlib.pyplot as plt
import random

names = [
    "Ali", "Bilal", "Ahmed", "Hamza", "Usman",
    "Ayesha", "Fatima", "Zara", "Hira", "Sana"
]

cities = [
    "Karachi", "Lahore", "Islamabad",
    "Multan", "Peshawar", "Quetta"
]

data = []

for i in range(5000):
    data.append([
        i + 1,
        random.choice(names),
        random.randint(12, 22),
        random.choice(cities),
        random.randint(300, 500)
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Student_ID",
        "Name",
        "Age",
        "City",
        "Marks"
    ]
)
print(df)

total_students = len(df)
average_marks = df['Marks'].mean()
highest_marks = df['Marks'].max()
lowest_marks = df['Marks'].min()
top_5 = df.nlargest(5, 'Marks')

print("\nTotal Students:", total_students)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("\nTop 5 Students:")
print(top_5[['Student_ID', 'Name', 'Marks']])

plt.figure(figsize=(10, 6))
plt.hist(df['Marks'], bins=20, color='lightblue', edgecolor='black')
plt.title('Marks Histogram')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.grid(True)
plt.show()