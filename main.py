# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = "https://docs.google.com/spreadsheets/d/1VP9BE_eI2yl6uUHSm4mGiiwjRdoqCqnkcIjsv5Q2ex4/export?format=csv"
df = pd.read_csv(url)

# Check the initial data
print("Initial data:")
print(df.head())

# Correct the data in the "height" column
df['height'] = np.random.randint(150, 181, size=len(df))

# Check the corrected data
print("\nCorrected data:")
print(df.head())

# Retrieve the 'height' column after correction
height_column = df['height']
print(height_column)

# 1. Calculate the distribution of employees across each team
team_distribution = df['Team'].value_counts()

# Calculate the percentage split relative to the total number of employees
total_employees = len(df)
percentage_split = (team_distribution / total_employees) * 100

# Display the results
print("Distribution of Employees Across Each Team:")
print(team_distribution)
print("\nPercentage Split Relative to Total Number of Employees:")
print(percentage_split)

# 2. Segregate employees based on their positions
employees_by_position = df.groupby('Position')

# Display the number of employees in each position
for position, employees in employees_by_position:
    print(f"Position: {position}, Number of Employees: {len(employees)}")

# 3. Define age bins
age_bins = [20, 30, 40, 50, 60, 70]  # You can adjust the age ranges as needed

# Create age groups
age_groups = pd.cut(df['Age'], bins=age_bins)

# Count the number of employees in each age group
age_group_counts = age_groups.value_counts()

# Identify the predominant age group
predominant_age_group = age_group_counts.idxmax()

# Display the results
print("Number of Employees in Each Age Group:")
print(age_group_counts)
print("\nPredominant Age Group:", predominant_age_group)

# Group the data by team and calculate the total salary expenditure for each team
team_salary_expenditure = df.groupby('Team')['Salary'].sum()

# 4. Group the data by position and calculate the total salary expenditure for each position
position_salary_expenditure = df.groupby('Position')['Salary'].sum()

# Discover which team and position have the highest salary expenditure
team_highest_salary = team_salary_expenditure.idxmax()
position_highest_salary = position_salary_expenditure.idxmax()

# Display the results
print("Team with the Highest Salary Expenditure:", team_highest_salary)
print("Position with the Highest Salary Expenditure:", position_highest_salary)

# 5. Plot the correlation between age and salary
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title('Correlation between Age and Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()