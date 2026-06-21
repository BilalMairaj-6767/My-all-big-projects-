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