# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://docs.google.com/spreadsheets/d/1VP9BE_eI2yl6uUHSm4mGiiwjRdoqCqnkcIjsv5Q2ex4/export?format=csv"
data = pd.read_csv(url)

# Plot the distribution of employees across each team
plt.figure(figsize=(10, 6))
data['Team'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Employees Across Each Team')
plt.xlabel('Team')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
###################################################################################
# Plot the segregation of employees based on positions
plt.figure(figsize=(10, 6))
data['Position'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon'])
plt.title('Segregation of Employees Based on Positions')
plt.ylabel('')
plt.show()
###################################################################################
# Define age bins
age_bins = [20, 30, 40, 50, 60, 70]  # You can adjust the age ranges as needed

# Create age groups
data['age_group'] = pd.cut(data['Age'], bins=age_bins)

# Plot the predominant age group among employees
plt.figure(figsize=(10, 6))
data['age_group'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
plt.title('Predominant Age Group Among Employees')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
###################################################################################
# Plot the team with the highest salary expenditure
plt.figure(figsize=(10, 6))
data.groupby('Team')['Salary'].sum().plot(kind='bar', color='lightblue')
plt.title('Team with the Highest Salary Expenditure')
plt.xlabel('Team')
plt.ylabel('Total Salary Expenditure')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
###################################################################################
# Plot the position with the highest salary expenditure
plt.figure(figsize=(10, 6))
data.groupby('Position')['Salary'].sum().plot(kind='bar', color='lightcoral')
plt.title('Position with the Highest Salary Expenditure')
plt.xlabel('Position')
plt.ylabel('Total Salary Expenditure')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
###################################################################################
# Plot the correlation between age and salary
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', data=data)
plt.title('Correlation between Age and Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()