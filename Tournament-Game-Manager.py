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