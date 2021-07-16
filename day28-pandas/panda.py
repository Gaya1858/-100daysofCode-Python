'''
- pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
    built on top of the Python programming language.
- pandas is designed for working with tabular and heterogeneous data.
---The two main data structures in pandas are Series, and DataFrame.
#Todo Series check out #### series.jpg###
- A one-dimensional array-like object containing an array of data values and
    associated array of labels called its index.
- Series values can be of any Numpy data types.
- Just like arrays, a single series can only hold one data type at a time.
-- can create series using dictionary

#Todo DataFrame check out ## dataframe.jpg### for coding###dataframe.code.jpg###
- A tabular spreadsheet-like data structure which contains columns, each of which can be a different data type.
- You can think of a dataframe as multiple series sharing the same index values.
- The dataframe has two axes: the index axis and the column axis.

How to create a DataFrame?
There are multiple ways to create the above dataframe. They all include using pd.DataFrame() constructor.
'''

import pandas as pd


thisdict = {
    "brand": ["Ford","Audi","Merc","Honda"],
    "electric": [False,True,False,True],
    "year": [1964,2018,2009,2020],
    "colors": ["red", "white", "blue","black"]
}

new_sheet = pd.DataFrame(thisdict)
print(new_sheet)
'''
   brand  electric  year colors
0   Ford     False  1964    red
1   Audi      True  2018  white
2   Merc     False  2009   blue
3  Honda      True  2020  black
'''
new_series =pd.Series(new_sheet["brand"]) ### or new_series =pd.Series(new_sheet.brand) both same
print(new_series)
'''
0     Ford
1     Audi
2     Merc
3    Honda
Name: brand, dtype: object
'''
print(new_sheet[new_sheet.brand=="Ford"]) ### this will give row where the brand name is ford
#0  Ford     False  1964    red


