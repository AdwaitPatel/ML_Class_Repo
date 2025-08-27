import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")  # Replace with your CSV file name or path

# Display the contents
print(df)
print(df.head())


iris = pd.read_csv('https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/refs/heads/master/Iris.csv')
print(iris)