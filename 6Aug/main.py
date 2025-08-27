import numpy as np
import pandas as pd

matrix1 = np.array(
    [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]
)

matrix2 = np.array(
    [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
)
# print("Sum of the elements in an Matrix => ", np.sum(matrix1))
# print("Addition of two Matrices\n", np.add(matrix1, matrix2))
# print("Matrix Subtraction => \n", np.subtract(matrix1, matrix2))
# print("Matrix Multiplication => \n", np.multiply(matrix1, matrix2))
# print("Dot Product => \n", np.dot(matrix1, matrix2))
# print("Dot Product => \n", matrix1 @ matrix2)
# print("Matrix Division => \n", np.divide(matrix1, matrix2))


data = [10, 20, 30, 40, 50]

# Question 1 : Print the data through series
print(pd.Series(data=data))
print("=" * 50)

# Question 2 : Print the series data with the index
print(pd.Series(data, index = ["a", "b", "c", "d", "e"]))
print("=" * 50)

# Question 3 : Create two columns calories and duration and insert the values
df = pd.DataFrame(
    {
        "Calories": [200, 400, 80],
        "Duration": [22, 35, 58]
    },
    index=["day 1", "day 2", "day 3"]
)
print(df)
print("=" * 50)

# Question 4 : Create three columns name, age and city and insert the values with the index name of person
df2 = pd.DataFrame(
    {
        "Name": ["Adwait", "Shshank", "Dhruv"],
        "Age": [20, 19, 20],
        "City": ["Mathura", "Agra", "Jhansi"]
    }, index=[1, 2, 3]
)
print(df2)
print("=" * 50)
