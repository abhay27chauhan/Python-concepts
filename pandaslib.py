# Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

# this file will show error if you have a file named string.py present in the same directory as this file

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], 
columns=["Column1", "Column2", "Column3", "Column4"])

print(df)
print(df.head())


## Accessing the elements
print(df.loc['Row1']) # used to retrieve rows from a data frame

print(df.iloc[[0, 1]])  # also used to retrieve rows -> will retrieve 2 rows -> 0 and 1
print(df.iloc[:, :])  # complete table is printed
print(df.iloc[:, 1:]) # can control the no. of rows and cols to print

print(type(df.loc['Row1'])) # series -> single row -> cannot be represented as 2d
print(type(df.iloc[[0, 1]])) # data frame -> it contains 2 rows -> can be represented as 2d
print(type(df.iloc[:, 1:])) # data frame

#convert Dataframes into array
arr = df.iloc[:, 1:].values
print(arr)

count = df['Column1'].value_counts()
print(count)
