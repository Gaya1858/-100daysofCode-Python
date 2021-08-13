'''Problem 1
Given a the contents of a CSV file as csv_contents, return the difference in days between the date of the earliest and the oldest entry.

The CSV file starts with a header row, which contains at least one column called Date.

You are optionally provided with the pandas library if you need it.

EXAMPLES

Input	"Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870"
Output	147
Explanation	There are 147 days between 2014-01-27 and 2014-06-23.
'''
import pandas as pd
import datetime as dt
def diff_days(csv_contents: str) -> int:
    start_date =csv_contents['Date'].min()
    last_date =csv_contents['Date'].max()
    s_year =start_date.split("-")[0]
    s_date = start_date.split("-")[2]
    s_month=start_date.split("-")[1]
    l_year =last_date.split("-")[0]
    l_date = last_date.split("-")[2]
    l_month=last_date.split("-")[1]
    date1 =dt.date(int(s_year),int(s_month),int(s_date))
    date2 =dt.date(int(l_year),int(l_month),int(l_date))
    result = (date2-date1).days
    return result




data =pd.read_csv("ex.csv")
print(data['Date'].max())

print(diff_days(data))
