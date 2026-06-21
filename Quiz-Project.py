import pandas as pd

df = pd.DataFrame({
            "Question": [
                "Pakistan ka capital kya hai?",
                "2 + 2 kitna hota hai?",
                "Python kis type ki language hai?",
                "Earth par kitne continents hain?",
                "AI ka full form kya hai?"
            ],
            "Answer": [
                "Islamabad",
                "4",
                "Programming",
                "7",
                "Artificial Intelligence"
            ]
        })

for i in range(len(df)):

    question = df.iloc[i]["Question"]
    answer = df.iloc[i]["Answer"]

    print(question)

    user_answer = input("Answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct ✅")
    else:
        print("Wrong ❌")
