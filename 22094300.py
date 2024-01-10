#Student ID: 22094300


import matplotlib.pyplot as plt
import pandas as pd

# Read data from the CSV file into a DataFrame
df = pd.read_csv('film-data.csv')  # Replace 'your_filename.csv' with the actual name of your CSV file

# Extract relevant columns for plotting
films = df['Film']
weekend_gross = df['Weekend Gross']
weeks_on_release = df['Weeks on Release']

# Plotting the Weekend Gross vs Weeks on Release as a bar plot
plt.figure(figsize=(10, 6))
plt.bar(films, weekend_gross, color='gray')
plt.title('Weekend Gross for Each Film')
plt.xlabel('Films')
plt.ylabel('Weekend Gross (£)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("22094300.png", dpi=300)




#2nd plot




#2 Read data from the CSV file into a DataFrame
df2 = pd.read_csv('film_data.csv')

# Extract relevant columns for plotting
films_2 = df2['Film']

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(films, weekend_gross, color='blue')
plt.xlabel('Films')
plt.ylabel('Weekend Gross')
plt.title('Weekend Gross for Each Film')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.savefig("22094300.png", dpi=300)


#3 plot

df3 = pd.read_csv('data.csv')  # Replace 'your_filename.csv' with the actual name of your CSV file

# Plotting a Pie Chart based on Total Gross to date
plt.figure(figsize=(8, 8))
plt.pie(df['Total Gross to date'], labels=df['Film'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Total Gross to date')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("22094300.png", dpi=300)



#plot4

# Read data from the CSV file into a DataFrame
df4 = pd.read_csv('data-file.csv')  # Replace 'your_filename.csv' with the actual name of your CSV file

# Plotting a Scatter Plot based on Weeks on Release and Weekend Gross
plt.figure(figsize=(10, 6))
plt.scatter(df['Weeks on Release'], df['Weekend Gross'], color='skyblue', marker='o')
plt.title('Scatter Plot: Weekend Gross vs Weeks on Release')
plt.xlabel('Weeks on Release')
plt.ylabel('Weekend Gross (£)')
plt.grid(True)
plt.savefig("22094300.png", dpi=300)
