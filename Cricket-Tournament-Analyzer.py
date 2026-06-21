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