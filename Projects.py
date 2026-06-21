#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


# In[17]:


import pandas as pd

class StudentManagementSystem:
    def __init__(self):
        self.df = pd.DataFrame({
            'Roll_No': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
            'Name': ['Ali Raza', 'Sana Khan', 'Ahmed Malik', 'Fatima Ahmed', 'Bilal Hassan', 'Zara Sheikh', 'Hamza Ali', 'Ayesha Siddiqui', 'Usman Chaudhry', 'Hira Tariq'],
            'Age': [20, 21, 19, 22, 20, 21, 19, 22, 20, 21],
            'Father_Name': ['Raza Ahmed', 'Imran Khan', 'Malik Ashraf', 'Ahmed Raza', 'Hassan Ali', 'Sheikh Javed', 'Ali Akbar', 'Siddiqui Raza', 'Chaudhry Latif', 'Tariq Mehmood'],
            'Class': ['12th', '12th', '11th', '12th', '11th', '12th', '11th', '12th', '11th', '12th'],
            'City': ['Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan', 'Peshawar', 'Quetta', 'Sialkot', 'Gujranwala'],
            'Total_Marks_Obtained': [450, 380, 470, 420, 430, 410, 445, 400, 490, 370],
            'Percentage': [90, 76, 94, 84, 86, 82, 89, 80, 98, 74],
            'Grade': ['A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A+', 'C'],
            'Result': ['Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail']
        })
        self.admin_code = "admin123"
        self.load_data()
    
    def convert_age(self, age_input):
        word_to_number = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
            'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
            'twenty one': 21, 'twenty two': 22, 'twenty three': 23, 'twenty four': 24, 'twenty five': 25
        }
        
        age_input = age_input.lower().strip()
        
        if age_input.isdigit():
            return int(age_input)
        elif age_input in word_to_number:
            return word_to_number[age_input]
        else:
            return None
    
    def load_data(self):
        try:
            temp_df = pd.read_csv("students.csv")
            print("Data loaded successfully from students.csv")
            print("Columns in CSV:", temp_df.columns.tolist())
            
            if 'Roll_No' not in temp_df.columns:
                if 'Roll No' in temp_df.columns:
                    temp_df.rename(columns={'Roll No': 'Roll_No'}, inplace=True)
                elif 'Roll_Number' in temp_df.columns:
                    temp_df.rename(columns={'Roll_Number': 'Roll_No'}, inplace=True)
                elif 'roll_no' in temp_df.columns:
                    temp_df.rename(columns={'roll_no': 'Roll_No'}, inplace=True)
                else:
                    print("No roll number column found. Creating new dataframe.")
                    self.save_data()
                    return
            
            self.df = temp_df
            
        except FileNotFoundError:
            print("No existing file found. Starting with default data.")
            self.save_data()
        except Exception as e:
            print(f"Error loading data: {e}")
            self.save_data()
    
    def save_data(self):
        self.df.to_csv("students.csv", index=False)
        print("Data saved to students.csv")
    
    def search_student(self):
        print("\nSearch by:")
        print("1. Roll Number")
        print("2. Name")
        search_choice = input("Enter your choice (1/2): ")
        
        if search_choice == '1':
            try:
                roll_no = int(input("Enter roll number: "))
                student_data = self.df[self.df['Roll_No'] == roll_no]
            except:
                print("Invalid roll number!")
                return
        elif search_choice == '2':
            student_name = input("Enter student name: ")
            student_data = self.df[self.df['Name'].str.lower() == student_name.lower()]
        else:
            print("Invalid choice!")
            return
        
        if not student_data.empty:
            row = student_data.iloc[0]
            print(f"\nInformation for {row['Name']}:")
            print(f"Roll Number : {row['Roll_No']}")
            print(f"Name : {row['Name']}")
            print(f"Age : {row['Age']}")
            print(f"Father Name : {row['Father_Name']}")
            print(f"Class : {row['Class']}")
            print(f"City : {row['City']}")
            print(f"Total Marks Obtained : {row['Total_Marks_Obtained']}")
            print(f"Percentage : {row['Percentage']}")
            print(f"Grade : {row['Grade']}")
            print(f"Result : {row['Result']}")
        else:
            print("No student found!")
    
    def add_student(self):
        admin_code = input("Enter admin code: ")
        
        if admin_code == self.admin_code:
            print("\n--- Add New Student ---")
            new_roll = int(input("Enter roll number: "))
            
            if new_roll in self.df['Roll_No'].values:
                print("Roll number already exists!")
                return
            
            new_name = input("Enter student name: ")
            
            age_input = input("Enter age (you can write in numbers or words like 'twenty'): ")
            new_age = self.convert_age(age_input)
            while new_age is None:
                age_input = input("Invalid age! Please enter age again (numbers or words like 'twenty'): ")
                new_age = self.convert_age(age_input)
            
            new_father = input("Enter father name: ")
            new_class = input("Enter class (11th/12th): ")
            new_city = input("Enter city: ")
            new_marks = int(input("Enter total marks obtained: "))
            new_percentage = float(input("Enter percentage: "))
            new_grade = input("Enter grade (A+, A, B, C): ")
            new_result = input("Enter result (Pass/Fail): ")
            
            new_student = pd.DataFrame({
                'Roll_No': [new_roll],
                'Name': [new_name],
                'Age': [new_age],
                'Father_Name': [new_father],
                'Class': [new_class],
                'City': [new_city],
                'Total_Marks_Obtained': [new_marks],
                'Percentage': [new_percentage],
                'Grade': [new_grade],
                'Result': [new_result]
            })
            
            self.df = pd.concat([self.df, new_student], ignore_index=True)
            self.save_data()
            print(f"\n{new_name} (Roll No: {new_roll}) has been added successfully!")
            self.view_all_students()
        else:
            print("Invalid admin code! Access denied.")
    
    def delete_student(self):
        admin_code = input("Enter admin code: ")
        
        if admin_code == self.admin_code:
            print("\nDelete by:")
            print("1. Roll Number")
            print("2. Name")
            delete_choice = input("Enter your choice (1/2): ")
            
            if delete_choice == '1':
                try:
                    roll_no = int(input("Enter roll number to delete: "))
                    student_data = self.df[self.df['Roll_No'] == roll_no]
                    if not student_data.empty:
                        self.df = self.df[self.df['Roll_No'] != roll_no]
                        self.save_data()
                        print(f"\nStudent with Roll No {roll_no} has been deleted successfully!")
                    else:
                        print(f"No student found with roll number: {roll_no}")
                        return
                except valueerror:
                    print("Invalid roll number!")
                    return
                    
            elif delete_choice == '2':
                student_name = input("Enter student name to delete: ")
                student_data = self.df[self.df['Name'].str.lower() == student_name.lower()]
                if not student_data.empty:
                    self.df = self.df[self.df['Name'].str.lower() != student_name.lower()]
                    self.save_data()
                    print(f"\n{student_name.title()} has been deleted successfully!")
                else:
                    print(f"No student found with name: {student_name}")
                    return
            else:
                print("Invalid choice!")
                return
            
            self.view_all_students()
        else:
            print("Invalid admin code! Access denied.")
    
    def view_all_students(self):
        if self.df.empty:
            print("\nNo students found in the database!")
        else:
            print("\n" + "="*80)
            print("ALL STUDENTS RECORD")
            print("="*80)
            columns_to_show = ['Roll_No', 'Name', 'Class', 'City', 'Percentage', 'Grade', 'Result']
            existing_columns = [col for col in columns_to_show if col in self.df.columns]
            print(self.df[existing_columns].to_string(index=False))
    
    def display_menu(self):
        while True:
            print("\n" + "="*40)
            print("STUDENT MANAGEMENT SYSTEM")
            print("="*40)
            print("1. Search Student")
            print("2. Add Student (Admin Only)")
            print("3. Delete Student (Admin Only)")
            print("4. View All Students")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1/2/3/4/5): ")
            
            if choice == '1':
                self.search_student()
            elif choice == '2':
                self.add_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.view_all_students()
            elif choice == '5':
                print("Exiting... Thank you!")
                self.save_data()
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.display_menu()


# In[188]:


import pandas as pd

class Tournament_Game_Manager:
    def __init__(self): 
        self.df = pd.DataFrame({
            'Player': ['shayan', 'Ali', 'Ahmed', 'Hamza', 'Usman','Ayesha', 'Fatima', 'Zara', 'Hassan', 'Sana','Hira', 'Talha', 'Anaya', 'Saad', 'Muneeb'],
            'Player_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            'Game': ['Free Fire', 'PUBG', 'Free Fire', 'PUBG', 'Valorant','Free Fire', 'Valorant', 'PUBG', 'Free Fire', 'Valorant','Free Fire', 'PUBG', 'Valorant', 'Free Fire', 'PUBG'],
            'Wins': [15, 10, 12, 8, 20, 14, 18, 11, 9, 16, 13, 7, 19, 6, 17],
            'Losses': [3, 5, 4, 7, 2, 6, 3, 4, 8, 5, 5, 8, 2, 10, 4]
        })
        self.admin_code = "admin123"
        self.load_data()
    
    def load_data(self):
        try:
            temp_df = pd.read_csv("Tournament_Game_Managment.csv")
            self.df = temp_df
            print("Data loaded successfully from Tournament_Game_Managment.csv")
            print("Columns in CSV:", temp_df.columns.tolist())
        except FileNotFoundError:
            print("No existing file found. Starting with default data.")
            self.save_data()
        except Exception as e:
            print(f"Error loading data: {e}")
            self.save_data()
    
    def save_data(self):
        self.df.to_csv("Tournament_Game_Managment.csv", index=False)
        print("Data saved to Tournament_Game_Managment.csv")
    
    def search_player(self):
        print("\nSearch by:")
        print("1. Player Number")
        print("2. Player Name")
        search_choice = input("Enter your choice (1/2): ")
        
        if search_choice == '1':
            try:
                rank_no = int(input("Enter player number: "))
                Player_data = self.df[self.df['Player_No'] == rank_no]
            except:
                print("Invalid Player Number!")
                return
        elif search_choice == '2':
            Player_name = input("Enter Player name: ")
            Player_data = self.df[self.df['Player'].str.lower() == Player_name.lower()]
        else:
            print("Invalid choice!")
            return
        
        if not Player_data.empty:
            row = Player_data.iloc[0]
            print(f"\nInformation for {row['Player']}:")
            print(f"Player: {row['Player']}")
            print(f"Player_No : {row['Player_No']}")
            print(f"Game: {row['Game']}")
            print(f"Wins: {row['Wins']}")
            print(f"Losses : {row['Losses']}")
        else:
            print("No Player found!")
    
    def show_top_player(self):
        if self.df.empty:
            print("\nNo Player found in the database!")
            return
        
        print("\n" + "="*80)
        print("TOP PLAYER RANKINGS")
        print("="*80)
        
        # Find top player by most wins
        top_player_by_wins = self.df.loc[self.df['Wins'].idxmax()]
        
        # Find top player by best win/loss ratio
        self.df['Win_Ratio'] = self.df['Wins'] / (self.df['Wins'] + self.df['Losses'])
        top_player_by_ratio = self.df.loc[self.df['Win_Ratio'].idxmax()]
        
        # Top 5 players by wins
        top_5_players = self.df.nlargest(5, 'Wins')[['Player', 'Player_No', 'Game', 'Wins', 'Losses']]
        
        print("\n🏆 TOP PLAYER OF THE TOURNAMENT (Most Wins): 🏆")
        print("-" * 80)
        print(f"Player Name: {top_player_by_wins['Player']}")
        print(f"Player Number: {top_player_by_wins['Player_No']}")
        print(f"Game: {top_player_by_wins['Game']}")
        print(f"Wins: {top_player_by_wins['Wins']}")
        print(f"Losses: {top_player_by_wins['Losses']}")
        
        print("\n📊 BEST WIN/LOSS RATIO: 📊")
        print("-" * 80)
        print(f"Player Name: {top_player_by_ratio['Player']}")
        print(f"Player Number: {top_player_by_ratio['Player_No']}")
        print(f"Game: {top_player_by_ratio['Game']}")
        print(f"Wins: {top_player_by_ratio['Wins']}")
        print(f"Losses: {top_player_by_ratio['Losses']}")
        print(f"Win Ratio: {top_player_by_ratio['Win_Ratio']:.2%}")
        
        print("\n🏅 TOP 5 PLAYERS BY WINS: 🏅")
        print("-" * 80)
        print(top_5_players.to_string(index=False))

        self.df = self.df.drop('Win_Ratio', axis=1)
    
    def add_player(self):
        admin_code = input("Enter admin code: ")
        
        if admin_code == self.admin_code:
            print("\n===== Add New Player =====")
            new_roll = int(input("Enter Player Number: "))
            
            if new_roll in self.df['Player_No'].values:
                print("Player number already exists!")
                return

            New_PlayerName = str(input("Enter player name: "))
            New_Match = str(input("Enter Game: "))
            New_Wins = int(input("Enter Wins: "))
            New_Losses = int(input("Enter Losses: "))
            New_Strike_Rate = int(input("Enter Strike_Rate: "))
            New_Runs = int(input("Enter Runs: "))

            New_Player_df = pd.DataFrame({
                'Name': [New_Player],
                'Player_ID': [new_roll],
                'Game': [New_Game],
                'Wins': [New_Wins],
                'Losses': [New_Losses]
            })
                
            self.df = pd.concat([self.df, New_Player_df], ignore_index=True)
            self.save_data()
            print(f"\n{New_Player} (Player No: {new_roll}) has been added successfully!")
            self.view_all_player()
        else:
            print("Invalid admin code! Access denied.")
    
    def delete_player(self):
        admin_code = input("Enter admin code: ")
        
        if admin_code == self.admin_code:
            print("\nDelete by:")
            print("1. Player Number")
            print("2. Name")
            delete_choice = input("Enter your choice (1/2): ")
            
            if delete_choice == '1':
                try:
                    Player_no = int(input("Enter Player number to delete: "))
                    Player_data = self.df[self.df['Player_No'] == Player_no]
                    if not Player_data.empty:
                        self.df = self.df[self.df['Player_No'] != Player_no]
                        self.save_data()
                        print(f"\nPlayer with Player No {Player_no} has been deleted successfully!")
                    else:
                        print(f"No Player found with Player number: {Player_no}")
                        return
                except ValueError:
                    print("Invalid Player number!")
                    return
                    
            elif delete_choice == '2':
                Player_name = input("Enter Player name to delete: ")
                Player_data = self.df[self.df['Player'].str.lower() == Player_name.lower()]
                if not Player_data.empty:
                    self.df = self.df[self.df['Player'].str.lower() != Player_name.lower()]
                    self.save_data()
                    print(f"\n{Player_name.title()} has been deleted successfully!")
                else:
                    print(f"No Player found with name: {Player_name}")
                    return
            else:
                print("Invalid choice!")
                return
            
            self.view_all_player()
        else:
            print("Invalid admin code! Access denied.")
    
    def view_all_player(self):
        if self.df.empty:
            print("\nNo Player found in the database!")
        else:
            print("\n" + "="*80)
            print("ALL PLAYER RECORD")
            print("="*80)
            columns_to_show = ['Player_ID', 'Name', 'Matches', 'Wins', 'Losses', 'Strike_Rate', 'Runs']
            existing_columns = [col for col in columns_to_show if col in self.df.columns]
            print(self.df[existing_columns].to_string(index=False))
    
    def display_menu(self):
        while True:
            print("\n" + "="*40)
            print("Tournament_Game_Manager")
            print("="*40)
            print("1. Search Player")
            print("2. Add Player (Admin Only)")
            print("3. Delete Player (Admin Only)")
            print("4. View All Player win and lossing rate")
            print("5. Show Top Player")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1/2/3/4/5/6): ")
            
            if choice == '1':
                self.search_player()
            elif choice == '2':
                self.add_player()
            elif choice == '3':
                self.delete_player()
            elif choice == '4':
                self.view_all_player()
            elif choice == '5':
                self.show_top_player()
            elif choice == '6':
                print("Exiting... Bye Bye")
                self.save_data()
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    system = Tournament_Game_Manager()
    system.display_menu()


# In[118]:


password = input("enter password(should be 8 letters) :")



has_capital = False
has_number = False

for char in password:

    if char.isupper():
        has_capital = True

    if char.isdigit():
        has_number = True

if len(password) >= 8 and has_capital and has_number:
    print("ur Password is Strong")

elif len(password) >= 8 and has_number:
    print("ur Password is Medium")

else:
    print("ur Password is Weak")

print("\nDoes it have numbers (True/False) : ", has_number)
print("Does it starts With capital (True/False) : ", has_capital)
print(len(password))


# In[195]:


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


# In[157]:


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


# In[ ]:





# In[170]:


try:
    print(int(input("enter your age : ")))
except ValueError:
    print("invalid age")


# In[178]:


try:
    a = int(input("first number : "))
    b = int(input("second number :"))
    print("Sum = ",a + b)
except ValueError:
    print("invalid number")


# In[204]:


import pandas as pd
import matplotlib.pyplot as plt

class CricketTournament:
    def __init__(self):
        self.admin_password = "admin123"
        self.load_data()
        self.df = pd.DataFrame({
            "Player_ID": [101,102,103,104,105,106,107,108,109,110,
                          111,112,113,114,115,116,117,118,119,120],
            "Name": [
                "Babar Azam","Mohammad Rizwan","Shaheen Afridi","Shadab Khan",
                "Fakhar Zaman","Imad Wasim","Naseem Shah","Abdullah Shafique",
                "Haris Rauf","Iftikhar Ahmed","Saim Ayub","Salman Ali Agha",
                "Usama Mir","Azam Khan","Tayyab Tahir","Mohammad Amir",
                "Khushdil Shah","Aamer Jamal","Saud Shakeel","Abrar Ahmed"
            ],
            "Team": [
                "Karachi Kings","Lahore Lions","Karachi Kings","Islamabad Eagles",
                "Lahore Lions","Karachi Kings","Peshawar Panthers","Islamabad Eagles",
                "Lahore Lions","Peshawar Panthers","Karachi Kings","Islamabad Eagles",
                "Peshawar Panthers","Lahore Lions","Islamabad Eagles","Karachi Kings",
                "Peshawar Panthers","Lahore Lions","Islamabad Eagles","Peshawar Panthers"
            ],
            "Matches": [
                20,18,19,21,17,20,16,18,20,19,
                17,18,16,15,17,19,18,16,20,17
            ],
            "Runs": [
                850,790,120,450,680,320,90,610,75,410,
                590,520,110,480,430,60,370,210,640,50
            ],
            "Wickets": [
                0,0,28,22,0,18,25,0,30,10,
                0,12,21,0,3,26,8,19,0,24
            ],
            "Wins": [
                14,12,11,15,10,13,8,12,9,10,
                11,13,7,9,10,12,8,9,14,6
            ],
            "Losses": [
                6,6,8,6,7,7,8,6,11,9,
                6,5,9,6,7,7,10,7,6,11
            ],
            "Strike_Rate": [
                135,140,95,145,150,130,88,138,80,142,
                148,136,92,155,139,75,144,125,132,70
            ]
        })
    
    def load_data(self):
        pass
    
    def save_data(self):
        try:
            self.df.to_csv("cricketplayers.csv", index=False)
            print("✅ Data saved successfully")
        except Exception as e:
            print(f"❌ Error saving data: {e}")
    
    def verify_admin(self):
        password = input("Enter Admin Password: ")
        if password == self.admin_password:
            return True
        else:
            print("❌ Incorrect password! Access denied.")
            return False
    
    def view_all_players(self):
        if self.df.empty:
            print("❌ No players found")
            return
        print("\n" + "="*100)
        print("🏏 ALL PLAYERS")
        print("="*100)
        print(self.df[["Name", "Team", "Matches", "Runs", "Wickets", "Wins", "Losses", "Strike_Rate"]].to_string(index=False))
        print("="*100)
    
    def search_player(self):
        if self.df.empty:
            print("❌ No players found")
            return
        
        print("\n🔍 SEARCH PLAYER")
        print("1. Search by Player ID")
        print("2. Search by Name")
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            try:
                player_id = int(input("Enter Player ID: "))
                result = self.df[self.df["Player_ID"] == player_id]
                if result.empty:
                    print(f"❌ No player found with ID: {player_id}")
                else:
                    print("\n✅ Player Found:")
                    print(result.to_string(index=False))
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
        
        elif choice == "2":
            name = input("Enter Player Name: ").strip()
            result = self.df[self.df["Name"].str.lower() == name.lower()]
            if result.empty:
                print(f"❌ No player found with name: {name}")
            else:
                print("\n✅ Player Found:")
                print(result.to_string(index=False))
        else:
            print("❌ Invalid choice")
    
    def add_player(self):
        if not self.verify_admin():
            return
        
        print("\n➕ ADD NEW PLAYER ➕")
        
        try:
            player_id = int(input("Enter Player ID: "))
            if player_id in self.df["Player_ID"].values:
                print(f"❌ Player ID {player_id} already exists!")
                return
            
            name = input("Enter Player Name: ").strip()
            team = input("Enter Team Name: ").strip()
            
            matches = int(input("Enter Matches Played: "))
            if matches < 0:
                print("❌ Matches cannot be negative")
                return
            
            runs = int(input("Enter Total Runs: "))
            if runs < 0:
                print("❌ Runs cannot be negative")
                return
            
            wickets = int(input("Enter Total Wickets: "))
            if wickets < 0:
                print("❌ Wickets cannot be negative")
                return
            
            wins = int(input("Enter Wins: "))
            if wins < 0:
                print("❌ Wins cannot be negative")
                return
            
            losses = int(input("Enter Losses: "))
            if losses < 0:
                print("❌ Losses cannot be negative")
                return
            
            if wins + losses > matches:
                print("❌ Wins + Losses cannot exceed Matches")
                return
            
            strike_rate = float(input("Enter Strike Rate: "))
            if strike_rate < 0:
                print("❌ Strike Rate cannot be negative")
                return
            
            new_player = pd.DataFrame([{
                "Player_ID": player_id,
                "Name": name,
                "Team": team,
                "Matches": matches,
                "Runs": runs,
                "Wickets": wickets,
                "Wins": wins,
                "Losses": losses,
                "Strike_Rate": strike_rate
            }])
            
            self.df = pd.concat([self.df, new_player], ignore_index=True)
            self.save_data()
            print(f"✅ Player {name} added successfully!")
            
        except ValueError:
            print("❌ Invalid input. Please enter correct data types.")
    
    def delete_player(self):
        if not self.verify_admin():
            return
        
        if self.df.empty:
            print("❌ No players found❌")
            return
        
        print("\n🗑️ DELETE PLAYER 🗑️")
        print("1. Delete by Player ID")
        print("2. Delete by Name")
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            try:
                player_id = int(input("Enter Player ID to delete: "))
                if player_id not in self.df["Player_ID"].values:
                    print(f"No player found with ID: {player_id}")
                    return
                
                player_name = self.df[self.df["Player_ID"] == player_id]["Name"].values[0]
                confirm = input(f"Are you sure you want to delete {player_name}? (y/n): ")
                
                if confirm.lower() == 'y':
                    self.df = self.df[self.df["Player_ID"] != player_id]
                    self.save_data()
                    print(f"✅ Player {player_name} deleted successfully!")
                else:
                    print("❌ Deletion cancelled❌")
                    
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
        
        elif choice == "2":
            name = input("Enter Player Name to delete: ").strip()
            result = self.df[self.df["Name"].str.lower() == name.lower()]
            
            if result.empty:
                print(f"❌ No player found with name: {name}")
                return
            
            print(f"\nFound {len(result)} player(s) with name '{name}':")
            print(result.to_string(index=False))
            
            confirm = input(f"Are you sure you want to delete all these players? (y/n): ")
            if confirm.lower() == 'y':
                self.df = self.df[self.df["Name"].str.lower() != name.lower()]
                self.save_data()
                print(f"✅ All players named '{name}' deleted successfully!")
            else:
                print("❌ Deletion cancelled")
        else:
            print("❌ Invalid choice")
    
    def analysis_menu(self):
        if self.df.empty:
            print("❌ No players found")
            return
        
        while True:
            print("\n" + "="*60)
            print("📊 ANALYSIS MENU")
            print("="*60)
            print("1. Highest Run Scorer")
            print("2. Highest Wicket Taker")
            print("3. Average Runs")
            print("4. Average Strike Rate")
            print("5. Players Per Team")
            print("6. Team-wise Average Runs")
            print("7. Best Win-Loss Ratio")
            print("8. Most Wins")
            print("9. Most Losses")
            print("10. Back to Main Menu")
            print("="*60)
            
            choice = input("Enter your choice (1-10): ")
            
            if choice == "1":
                max_runs = self.df["Runs"].max()
                top_scorer = self.df[self.df["Runs"] == max_runs]
                print(f"\n🏆 Highest Run Scorer: {max_runs} runs")
                print(top_scorer[["Name", "Team", "Runs"]].to_string(index=False))
            
            elif choice == "2":
                max_wickets = self.df["Wickets"].max()
                top_bowler = self.df[self.df["Wickets"] == max_wickets]
                print(f"\n🎯 Highest Wicket Taker: {max_wickets} wickets")
                print(top_bowler[["Name", "Team", "Wickets"]].to_string(index=False))
            
            elif choice == "3":
                avg_runs = self.df["Runs"].mean()
                print(f"\n📈 Average Runs: {avg_runs:.2f}")
            
            elif choice == "4":
                avg_sr = self.df["Strike_Rate"].mean()
                print(f"\n📈 Average Strike Rate: {avg_sr:.2f}")
            
            elif choice == "5":
                team_counts = self.df["Team"].value_counts()
                print("\n🏏 Players Per Team:")
                for team, count in team_counts.items():
                    print(f"   {team}: {count} players")
            
            elif choice == "6":
                team_avg_runs = self.df.groupby("Team")["Runs"].mean()
                print("\n🏏 Team-wise Average Runs:")
                for team, avg in team_avg_runs.items():
                    print(f"   {team}: {avg:.2f}")
            
            elif choice == "7":
                self.df["Win_Ratio"] = self.df["Wins"] / self.df["Matches"]
                best_ratio = self.df["Win_Ratio"].max()
                best_players = self.df[self.df["Win_Ratio"] == best_ratio]
                print(f"\n🏆 Best Win-Loss Ratio: {best_ratio:.2%}")
                print(best_players[["Name", "Team", "Wins", "Losses", "Matches"]].to_string(index=False))
                self.df = self.df.drop(columns=["Win_Ratio"])
            
            elif choice == "8":
                max_wins = self.df["Wins"].max()
                most_wins = self.df[self.df["Wins"] == max_wins]
                print(f"\n🏆 Most Wins: {max_wins} wins")
                print(most_wins[["Name", "Team", "Wins", "Losses"]].to_string(index=False))
            
            elif choice == "9":
                max_losses = self.df["Losses"].max()
                most_losses = self.df[self.df["Losses"] == max_losses]
                print(f"\n😞 Most Losses: {max_losses} losses")
                print(most_losses[["Name", "Team", "Wins", "Losses"]].to_string(index=False))
            
            elif choice == "10":
                break
            
            else:
                print("❌ Invalid choice. Please try again.❌")
    
    def show_charts(self):
        if self.df.empty:
            print("❌ No players found❌")
            return
        
        while True:
            print("\n" + "="*50)
            print("📊 CHART MENU📊")
            print("="*50)
            print("1. Runs Distribution (Histogram)")
            print("2. Players Per Team (Bar Chart)")
            print("3. Matches vs Runs (Scatter Plot)")
            print("4. Wins by Player (Bar Chart)")
            print("5. Back to Main Menu")
            print("="*50)
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                plt.figure(figsize=(10, 6))
                plt.hist(self.df["Runs"], bins=10, color='skyblue', edgecolor='black')
                plt.title("Runs Distribution of Players")
                plt.xlabel("Runs")
                plt.ylabel("Number of Players")
                plt.grid(True)
                plt.show()
            
            elif choice == "2":
                team_count = self.df["Team"].value_counts()
                plt.figure(figsize=(10, 6))
                plt.bar(team_count.index, team_count.values, color='lightgreen', edgecolor='black')
                plt.title("Players Per Team")
                plt.xlabel("Team")
                plt.ylabel("Number of Players")
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            
            elif choice == "3":
                plt.figure(figsize=(10, 6))
                plt.scatter(self.df["Matches"], self.df["Runs"], color='coral', s=100)
                plt.title("Matches vs Runs")
                plt.xlabel("Matches Played")
                plt.ylabel("Runs Scored")
                plt.grid(True)
                plt.show()
            
            elif choice == "4":
                plt.figure(figsize=(12, 6))
                plt.bar(self.df["Name"], self.df["Wins"], color='gold', edgecolor='black')
                plt.title("Wins by Player")
                plt.xlabel("Player Name")
                plt.ylabel("Wins")
                plt.xticks(rotation=45, ha='right')
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            
            elif choice == "5":
                break
            
            else:
                print("❌ Invalid choice. Please try again.❌")
    
    def advanced_analysis(self):
        if self.df.empty:
            print("❌ No players found❌")
            return
        
        while True:
            print("\n" + "="*60)
            print("🔬 ADVANCED ANALYSIS")
            print("="*60)
            print("11. Top 5 Run Scorers")
            print("12. Top 5 Wicket Takers")
            print("13. Players with 20+ Wickets")
            print("14. Players with 500+ Runs")
            print("15. Team with Most Wins")
            print("16. Player Statistics Summary")
            print("17. Back to Main Menu")
            print("="*60)
            
            choice = input("Enter your choice (11-17): ")
            
            if choice == "11":
                top_5_runs = self.df.nlargest(5, "Runs")[["Name", "Team", "Runs"]]
                print("\n🏏 Top 5 Run Scorers:")
                print(top_5_runs.to_string(index=False))
            
            elif choice == "12":
                top_5_wickets = self.df.nlargest(5, "Wickets")[["Name", "Team", "Wickets"]]
                print("\n🎯 Top 5 Wicket Takers:")
                print(top_5_wickets.to_string(index=False))
            
            elif choice =="13":
                players_20_wickets = self.df[self.df["Wickets"] >= 20][["Name", "Team", "Wickets"]]
                if players_20_wickets.empty:
                    print("\n❌ No players with 20+ wickets")
                else:
                    print("\n🏏 Players with 20+ Wickets:")
                    print(players_20_wickets.to_string(index=False))
            
            elif choice == "14":
                players_500_runs = self.df[self.df["Runs"] >= 500][["Name", "Team", "Runs"]]
                if players_500_runs.empty:
                    print("\n❌ No players with 500+ runs")
                else:
                    print("\n🏏 Players with 500+ Runs:")
                    print(players_500_runs.to_string(index=False))
            
            elif choice == "15":
                team_wins = self.df.groupby("Team")["Wins"].sum()
                best_team = team_wins.idxmax()
                most_wins = team_wins.max()
                print(f"\n🏆 Team with Most Wins: {best_team} with {most_wins} wins")
                print("\nAll Teams:")
                for team, wins in team_wins.items():
                    print(f"   {team}: {wins} wins")
            
            elif choice == "16":
                print("\n📊 PLAYER STATISTICS SUMMARY")
                print("="*50)
                print(f"Total Players: {len(self.df)}")
                print(f"Total Runs: {self.df['Runs'].sum()}")
                print(f"Total Wickets: {self.df['Wickets'].sum()}")
                print(f"Average Runs per Player: {self.df['Runs'].mean():.2f}")
                print(f"Average Wickets per Player: {self.df['Wickets'].mean():.2f}")
                print(f"Average Strike Rate: {self.df['Strike_Rate'].mean():.2f}")
                print(f"Total Wins: {self.df['Wins'].sum()}")
                print(f"Total Losses: {self.df['Losses'].sum()}")
                print("="*50)
            
            elif choice == "17":
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    def main_menu(self):
        while True:
            print("\n" + "="*60)
            print("🏏 CRICKET TOURNAMENT ANALYZER")
            print("="*60)
            print("1. View All Players")
            print("2. Search Player")
            print("3. Add Player (Admin Only)")
            print("4. Delete Player (Admin Only)")
            print("5. Analysis Menu")
            print("6. Charts")
            print("7. Advanced Analysis")
            print("8. Save And Exit")
            print("="*60)
            
            choice = input("Enter your choice (1-8): ")
            
            if choice == "1":
                self.view_all_players()
            elif choice == "2":
                self.search_player()
            elif choice == "3":
                self.add_player()
            elif choice == "4":
                self.delete_player()
            elif choice == "5":
                self.analysis_menu()
            elif choice == "6":
                self.show_charts()
            elif choice == "7":
                self.advanced_analysis()
            elif choice == "8":
                
                self.save_data()
                print("🙋🏽‍♂️👋Thank you for using Cricket Tournament Analyzer!🙋🏽‍♂️👋")
                break
            else:
                print("❌Invalid choice. Please try again.❌")

if __name__ == "__main__":
    tournament = CricketTournament()
    tournament.main_menu()


# In[2]:


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


# In[18]:


class HospitalAnalyzer:
    def __init__(self):
        random.seed(42)
        np.random.seed(42)
        
        self.df = pd.DataFrame({
            "Patient_ID": [101,102,103,104,105,106,107,108,109,110,
                           111,112,113,114,115,116,117,118,119,120],
            "Name": [
                "Ali Khan","Ahmed Raza","Sara Ahmed","Ayesha Malik","Hassan Ali",
                "Fatima Noor","Usman Tariq","Zainab Shah","Bilal Ahmed","Mariam Khan",
                "Hamza Siddiqui","Noor Fatima","Talha Sheikh","Iqra Hassan","Daniyal Khan",
                "Laiba Ali","Saad Malik","Hira Ahmed","Abdullah Khan","Anaya Noor"
            ],
            "Age": [
                45,32,28,51,39,24,60,35,42,30,
                55,26,48,37,65,22,58,33,40,29
            ],
            "Gender": [
                "Male","Male","Female","Female","Male",
                "Female","Male","Female","Male","Female",
                "Male","Female","Male","Female","Male",
                "Female","Male","Female","Male","Female"
            ],
            "Disease": [
                "Diabetes","Flu","Asthma","Heart Disease","Hypertension",
                "Migraine","Diabetes","Flu","Asthma","Typhoid",
                "Heart Disease","Migraine","Hypertension","Flu","Diabetes",
                "Typhoid","Heart Disease","Asthma","Hypertension","Migraine"
            ],
            "Treatment_Cost": [
                25000,5000,12000,50000,18000,
                8000,27000,4500,15000,9000,
                55000,7000,20000,6000,30000,
                8500,52000,14000,19000,7500
            ],
            "Days_Admitted": [
                7,2,4,10,5,
                3,8,2,4,3,
                9,2,6,2,8,
                3,10,5,6,2
            ],
            "Doctor": [
                "Dr. Ahmed","Dr. Khan","Dr. Ali","Dr. Hassan","Dr. Ahmed",
                "Dr. Khan","Dr. Ali","Dr. Hassan","Dr. Ahmed","Dr. Khan",
                "Dr. Ali","Dr. Hassan","Dr. Ahmed","Dr. Khan","Dr. Ali",
                "Dr. Hassan","Dr. Ahmed","Dr. Khan","Dr. Ali","Dr. Hassan"
            ]
        })
        self.results = {}
    
    def run_analysis(self):
        self.basic_statistics()
        self.age_analysis()
        self.disease_analysis()
        self.gender_analysis()
        self.cost_analysis()
        self.doctor_analysis()
        self.correlation_analysis()
        self.visualize_all()
        self.print_summary()
    
    def basic_statistics(self):
        print("\n" + "="*60)
        print("MAMJI HOSPITAL MANAGEMENT ANALYSIS REPORT")
        print("="*60)
        print("\n BASIC STATISTICS")
        print("-"*40)
        
        stats = {
            'total_patients': len(self.df),
            'unique_diseases': self.df['Disease'].nunique(),
            'avg_age': self.df['Age'].mean(),
            'avg_cost': self.df['Treatment_Cost'].mean(),
            'total_cost': self.df['Treatment_Cost'].sum(),
            'avg_days': self.df['Days_Admitted'].mean()
        }
        
        self.results['basic_stats'] = stats
        
        for key, value in stats.items():
            if 'cost' in key and 'total' not in key:
                print(f"  {key.replace('_', ' ').title()}: ${value:,.2f}")
            elif 'total_cost' in key:
                print(f"  {key.replace('_', ' ').title()}: ${value:,.2f}")
            elif 'days' in key:
                print(f"  {key.replace('_', ' ').title()}: {value:.1f} days")
            else:
                print(f"  {key.replace('_', ' ').title()}: {value:,}")
    
    def age_analysis(self):
        print("\n AGE ANALYSIS")
        print("-"*40)
        
        oldest = self.df.loc[self.df['Age'].idxmax()]
        youngest = self.df.loc[self.df['Age'].idxmin()]
        
        age_groups = pd.cut(self.df['Age'], 
                           bins=[0, 18, 35, 50, 100], 
                           labels=['Children', 'Young Adults', 'Middle-aged', 'Seniors'])
        
        self.results['age_stats'] = {
            'oldest': oldest,
            'youngest': youngest,
            'mean': self.df['Age'].mean(),
            'median': self.df['Age'].median(),
            'std': self.df['Age'].std(),
            'groups': age_groups.value_counts()
        }
        
        print(f"  Oldest Patient: {oldest['Name']} (Age: {oldest['Age']}, Disease: {oldest['Disease']})")
        print(f"  Youngest Patient: {youngest['Name']} (Age: {youngest['Age']}, Disease: {youngest['Disease']})")
        print(f"  Mean Age: {self.df['Age'].mean():.1f} years")
        print(f"  Median Age: {self.df['Age'].median():.1f} years")
        print("  Age Group Distribution:")
        for group, count in age_groups.value_counts().items():
            print(f"    - {group}: {count} patients ({count/len(self.df)*100:.1f}%)")
    
    def disease_analysis(self):
        print("\n DISEASE ANALYSIS")
        print("-"*40)
        
        disease_counts = self.df['Disease'].value_counts()
        disease_costs = self.df.groupby('Disease')['Treatment_Cost'].agg(['mean', 'sum', 'count'])
        disease_costs.columns = ['avg_cost', 'total_cost', 'count']
        disease_days = self.df.groupby('Disease')['Days_Admitted'].mean()
        
        most_common = disease_counts.index[0]
        most_expensive = disease_costs['avg_cost'].idxmax()
        costliest_treatment = self.df.loc[self.df['Treatment_Cost'].idxmax()]
        
        self.results['disease_stats'] = {
            'counts': disease_counts,
            'costs': disease_costs,
            'days': disease_days,
            'most_common': most_common,
            'most_expensive_disease': most_expensive,
            'costliest_treatment': costliest_treatment
        }
        
        print(f"  Most Common Disease: {most_common} ({disease_counts.iloc[0]} patients)")
        print(f"  Most Expensive Disease (avg): {most_expensive} (${disease_costs.loc[most_expensive, 'avg_cost']:,.2f})")
        print(f"\n  Costliest Individual Treatment:")
        print(f"    Patient: {costliest_treatment['Name']}")
        print(f"    Disease: {costliest_treatment['Disease']}")
        print(f"    Cost: ${costliest_treatment['Treatment_Cost']:,.2f}")
        print(f"    Days Admitted: {costliest_treatment['Days_Admitted']} days")
        
        print("\n  Disease Distribution:")
        for disease, count in disease_counts.items():
            pct = count/len(self.df)*100
            avg_cost = disease_costs.loc[disease, 'avg_cost']
            avg_days = disease_days.loc[disease]
            print(f"    - {disease}: {count} patients ({pct:.1f}%), Avg Cost: ${avg_cost:,.2f}, Avg Days: {avg_days:.1f}")
    
    def gender_analysis(self):
        print("\n GENDER ANALYSIS")
        print("-"*40)
        
        gender_stats = self.df.groupby('Gender').agg({
            'Patient_ID': 'count',
            'Age': 'mean',
            'Treatment_Cost': 'mean',
            'Days_Admitted': 'mean'
        })
        gender_stats.columns = ['count', 'avg_age', 'avg_cost', 'avg_days']
        
        self.results['gender_stats'] = gender_stats
        
        for gender in gender_stats.index:
            row = gender_stats.loc[gender]
            print(f"\n  {gender}:")
            print(f"    Patients: {row['count']}")
            print(f"    Avg Age: {row['avg_age']:.1f} years")
            print(f"    Avg Treatment Cost: ${row['avg_cost']:,.2f}")
            print(f"    Avg Days Admitted: {row['avg_days']:.1f}")
    
    def cost_analysis(self):
        print("\n COST ANALYSIS")
        print("-"*40)
        
        cost_stats = {
            'total': self.df['Treatment_Cost'].sum(),
            'mean': self.df['Treatment_Cost'].mean(),
            'median': self.df['Treatment_Cost'].median(),
            'std': self.df['Treatment_Cost'].std(),
            'min': self.df['Treatment_Cost'].min(),
            'max': self.df['Treatment_Cost'].max(),
            'percentiles': self.df['Treatment_Cost'].quantile([0.25, 0.5, 0.75])
        }
        
        self.results['cost_stats'] = cost_stats
        
        print(f"  Total Treatment Cost: ${cost_stats['total']:,.2f}")
        print(f"  Mean Cost: ${cost_stats['mean']:,.2f}")
        print(f"  Median Cost: ${cost_stats['median']:,.2f}")
        print(f"  Cost Range: ${cost_stats['min']:,.2f} - ${cost_stats['max']:,.2f}")
        print(f"  Standard Deviation: ${cost_stats['std']:,.2f}")
        print("  Percentiles:")
        for p, val in cost_stats['percentiles'].items():
            print(f"    {int(p*100)}th percentile: ${val:,.2f}")
    
    def doctor_analysis(self):
        print("\n DOCTOR ANALYSIS")
        print("-"*40)
        
        doctor_stats = self.df.groupby('Doctor').agg({
            'Patient_ID': 'count',
            'Treatment_Cost': 'mean',
            'Days_Admitted': 'mean'
        })
        doctor_stats.columns = ['patient_count', 'avg_cost', 'avg_days']
        
        self.results['doctor_stats'] = doctor_stats
        
        print("  Doctor Performance Summary:")
        for doctor in doctor_stats.index:
            row = doctor_stats.loc[doctor]
            print(f"    - {doctor}:")
            print(f"      Patients: {row['patient_count']}")
            print(f"      Avg Treatment Cost: ${row['avg_cost']:,.2f}")
            print(f"      Avg Days Admitted: {row['avg_days']:.1f}")
        
        busiest_doctor = doctor_stats['patient_count'].idxmax()
        print(f"\n  Busiest Doctor: {busiest_doctor} ({doctor_stats.loc[busiest_doctor, 'patient_count']} patients)")
    
    def correlation_analysis(self):
        print("\n CORRELATION ANALYSIS")
        print("-"*40)
        
        numeric_cols = self.df[['Age', 'Treatment_Cost', 'Days_Admitted']]
        corr_matrix = numeric_cols.corr()
        
        self.results['correlations'] = corr_matrix
        
        print("  Correlation Matrix:")
        print(corr_matrix.round(3))
        
        corr_pairs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j], 
                                  corr_matrix.iloc[i, j]))
        
        corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
        
        print("\n  Strongest Correlations:")
        for col1, col2, corr in corr_pairs:
            if abs(corr) > 0.1:
                direction = "positive" if corr > 0 else "negative"
                print(f"    - {col1} ↔ {col2}: {corr:.3f} ({direction})")
    
    def visualize_all(self):
        print("\n" + "="*60)
        print("GENERATING VISUALIZATIONS")
        print("="*60)
        
        self.plot_age_distribution()
        self.plot_disease_distribution()
        self.plot_gender_analysis()
        self.plot_cost_distribution()
        self.plot_age_vs_cost()
        self.plot_disease_cost_boxplot()
        self.plot_doctor_performance()
        self.plot_correlation_heatmap()
        self.plot_treatment_cost_by_disease()
        
        print("\n All visualizations displayed")
    
    def plot_age_distribution(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df['Age'].hist(bins=10, edgecolor='black', alpha=0.7, color='skyblue', ax=ax)
        ax.set_xlabel('Age (years)')
        ax.set_ylabel('Number of Patients')
        ax.set_title('Age Distribution of Patients')
        ax.axvline(self.df['Age'].mean(), color='red', linestyle='--', 
                  label=f'Mean Age: {self.df["Age"].mean():.1f}')
        ax.axvline(self.df['Age'].median(), color='green', linestyle='--',
                  label=f'Median Age: {self.df["Age"].median():.1f}')
        ax.legend()
        plt.tight_layout()
        plt.show()
    
    def plot_disease_distribution(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        disease_counts = self.df['Disease'].value_counts()
        colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffa07a', '#dda0dd', '#f0e68c', '#87ceeb']
        disease_counts.plot(kind='bar', ax=ax, edgecolor='black', color=colors[:len(disease_counts)])
        ax.set_xlabel('Disease')
        ax.set_ylabel('Number of Patients')
        ax.set_title('Distribution of Diseases')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        for i, v in enumerate(disease_counts):
            ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def plot_gender_analysis(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        gender_counts = self.df['Gender'].value_counts()
        ax1.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',
                startangle=90, explode=[0.05, 0.05], colors=['#3498db', '#e74c3c'])
        ax1.set_title('Gender Distribution')
        
        gender_disease = pd.crosstab(self.df['Gender'], self.df['Disease'])
        gender_disease.plot(kind='bar', ax=ax2, edgecolor='black')
        ax2.set_xlabel('Gender')
        ax2.set_ylabel('Number of Patients')
        ax2.set_title('Gender Distribution by Disease')
        ax2.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)
        plt.tight_layout()
        plt.show()
    
    def plot_cost_distribution(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df['Treatment_Cost'].hist(bins=15, edgecolor='black', color='lightcoral', ax=ax)
        ax.set_xlabel('Treatment Cost ($)')
        ax.set_ylabel('Number of Patients')
        ax.set_title('Distribution of Treatment Costs')
        ax.axvline(self.df['Treatment_Cost'].mean(), color='red', linestyle='--',
                  label=f'Mean: ${self.df["Treatment_Cost"].mean():,.2f}')
        ax.axvline(self.df['Treatment_Cost'].median(), color='green', linestyle='--',
                  label=f'Median: ${self.df["Treatment_Cost"].median():,.2f}')
        ax.legend()
        plt.tight_layout()
        plt.show()
    
    def plot_age_vs_cost(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = ['blue' if x == 0 else 'red' for x in np.random.randint(0, 2, len(self.df))]
        ax.scatter(self.df['Age'], self.df['Treatment_Cost'], 
                  c=colors, s=100)
        ax.set_xlabel('Age (years)')
        ax.set_ylabel('Treatment Cost ($)')
        ax.set_title('Age vs Treatment Cost')
        z = np.polyfit(self.df['Age'], self.df['Treatment_Cost'], 1)
        p = np.poly1d(z)
        ax.plot(self.df['Age'].sort_values(), p(self.df['Age'].sort_values()),
                "g-", label='Trend Line')
        ax.legend()
        plt.tight_layout()
        plt.show()
    
    def plot_disease_cost_boxplot(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        diseases = self.df['Disease'].unique()
        data_to_plot = [self.df[self.df['Disease'] == d]['Treatment_Cost'].values for d in diseases]
        bp = ax.boxplot(data_to_plot, labels=diseases, patch_artist=True)
        for patch in bp['boxes']:
            patch.set_facecolor('lightblue')
        ax.set_xlabel('Disease')
        ax.set_ylabel('Treatment Cost ($)')
        ax.set_title('Treatment Cost Distribution by Disease')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    
    def plot_doctor_performance(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        doctor_counts = self.df['Doctor'].value_counts()
        doctor_counts.plot(kind='bar', ax=ax1, edgecolor='black', color='lightgreen')
        ax1.set_xlabel('Doctor')
        ax1.set_ylabel('Number of Patients')
        ax1.set_title('Patients per Doctor')
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
        
        doctor_avg_cost = self.df.groupby('Doctor')['Treatment_Cost'].mean()
        doctor_avg_cost.plot(kind='bar', ax=ax2, edgecolor='black', color='gold')
        ax2.set_xlabel('Doctor')
        ax2.set_ylabel('Average Treatment Cost ($)')
        ax2.set_title('Average Cost per Doctor')
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
        
        plt.tight_layout()
        plt.show()
    
    def plot_correlation_heatmap(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        numeric_cols = self.df[['Age', 'Treatment_Cost', 'Days_Admitted']]
        corr_matrix = numeric_cols.corr()
        
        im = ax.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
        ax.set_xticks(range(len(corr_matrix.columns)))
        ax.set_yticks(range(len(corr_matrix.columns)))
        ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
        ax.set_yticklabels(corr_matrix.columns)
        
        for i in range(len(corr_matrix.columns)):
            for j in range(len(corr_matrix.columns)):
                text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                             ha='center', va='center', color='black' if abs(corr_matrix.iloc[i, j]) < 0.5 else 'white')
        
        plt.colorbar(im, ax=ax)
        ax.set_title('Correlation Heatmap')
        plt.tight_layout()
        plt.show()
    
    def plot_treatment_cost_by_disease(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        disease_cost = self.df.groupby('Disease')['Treatment_Cost'].mean().sort_values(ascending=True)
        colors = plt.cm.viridis(np.linspace(0, 1, len(disease_cost)))
        disease_cost.plot(kind='barh', ax=ax, color=colors, edgecolor='black')
        ax.set_xlabel('Average Treatment Cost ($)')
        ax.set_ylabel('Disease')
        ax.set_title('Average Treatment Cost by Disease')
        for i, v in enumerate(disease_cost):
            ax.text(v + 500, i, f'${v:,.2f}', va='center')
        plt.tight_layout()
        plt.show()
    
    def print_summary(self):
        print("\n" + "="*60)
        print("SUMMARY DASHBOARD")
        print("="*60)
        
        summary = pd.DataFrame({
            'Metric': ['Total Patients', 'Average Age', 'Average Cost', 'Total Cost', 
                      'Average Days Admitted', 'Most Common Disease', 'Most Expensive Disease'],
            'Value': [
                len(self.df),
                f"{self.df['Age'].mean():.1f} years",
                f"${self.df['Treatment_Cost'].mean():,.2f}",
                f"${self.df['Treatment_Cost'].sum():,.2f}",
                f"{self.df['Days_Admitted'].mean():.1f} days",
                self.df['Disease'].value_counts().index[0],
                self.df.groupby('Disease')['Treatment_Cost'].mean().idxmax()
            ]
        })
        print(summary.to_string(index=False))
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETE!")
        print("="*60)

if __name__ == "__main__":
    analyzer = HospitalAnalyzer()
    analyzer.run_analysis()


# In[ ]:




