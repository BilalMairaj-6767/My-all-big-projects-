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