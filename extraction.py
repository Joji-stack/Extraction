Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
==== No Subprocess ====

WARNING: Running IDLE without a Subprocess is deprecated
and will be removed in a later version. See Help/IDLE Help
for details.




TSLA: Period '5row' is invalid, must be one of ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
                       Date      Open  ...  Dividends  Stock Splits
0 2010-06-29 00:00:00-04:00  1.266667  ...        0.0           0.0
1 2010-06-30 00:00:00-04:00  1.719333  ...        0.0           0.0
2 2010-07-01 00:00:00-04:00  1.666667  ...        0.0           0.0
3 2010-07-02 00:00:00-04:00  1.533333  ...        0.0           0.0
4 2010-07-06 00:00:00-04:00  1.333333  ...        0.0           0.0

[5 rows x 8 columns]
                       Date      Open  ...  Dividends  Stock Splits
0 2010-06-29 00:00:00-04:00  1.266667  ...        0.0           0.0
1 2010-06-30 00:00:00-04:00  1.719333  ...        0.0           0.0
2 2010-07-01 00:00:00-04:00  1.666667  ...        0.0           0.0
3 2010-07-02 00:00:00-04:00  1.533333  ...        0.0           0.0
4 2010-07-06 00:00:00-04:00  1.333333  ...        0.0           0.0

[5 rows x 8 columns]
Traceback (most recent call last):
  File "C:/Users/Lenovo/AppData/Local/Programs/Python/Python310/yf.py", line 13, in <module>
    tesla_revenue_tail = tesla_revenue.tail()
NameError: name 'tesla_revenue' is not defined
Traceback (most recent call last):
  File "C:/Users/Lenovo/AppData/Local/Programs/Python/Python310/yf.py", line 3, in <module>
    tesla_revenue_tail = tesla_revenue.tail()
NameError: name 'tesla_revenue' is not defined
tesla_revenue_tail = tesla_revenue.tail()

# Output the result
print(tesla_revenue_tail)
SyntaxError: multiple statements found while compiling a single statement
Traceback (most recent call last):
  File "C:/Users/Lenovo/AppData/Local/Programs/Python/Python310/yf.py", line 9, in <module>
    tesla_revenue_tail = tesla_revenue.tail()
NameError: name 'tesla_revenue' is not defined
>>>        index  Total Revenue
2 2023-12-31  25167000000.0
3 2023-09-30  23350000000.0
4 2023-06-30  24927000000.0
5 2023-03-31            NaN
6 2022-12-31            NaN
>>> 
Tesla Revenue - Last 5 Rows:
   level_0      index  Total Revenue
2        2 2023-12-31  25167000000.0
3        3 2023-09-30  23350000000.0
4        4 2023-06-30  24927000000.0
5        5 2023-03-31            NaN
6        6 2022-12-31            NaN

GameStop (GME) Data - First 5 Rows:
                       Date      Open  ...  Dividends  Stock Splits
0 2002-02-13 00:00:00-05:00  1.620128  ...        0.0           0.0
1 2002-02-14 00:00:00-05:00  1.712707  ...        0.0           0.0
2 2002-02-15 00:00:00-05:00  1.683250  ...        0.0           0.0
3 2002-02-19 00:00:00-05:00  1.666418  ...        0.0           0.0
4 2002-02-20 00:00:00-05:00  1.615921  ...        0.0           0.0

[5 rows x 8 columns]
>>> GameStop (GME) Revenue - Last 5 Rows:
       index Total Revenue
1 2024-01-31  1793600000.0
2 2023-10-31  1078300000.0
3 2023-07-31  1163800000.0
4 2023-04-30  1237100000.0
5 2023-01-31           NaN
>>> Traceback (most recent call last):
  File "C:/Users/Lenovo/AppData/Local/Programs/Python/Python310/yf.py", line 2, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 1921, in __call__
    return self.func(*args)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\idlelib\runscript.py", line 166, in run_module_event
    interp.runcode(code)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\idlelib\pyshell.py", line 779, in runcode
    self.restart_subprocess()
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\idlelib\pyshell.py", line 512, in restart_subprocess
    self.rpcclt.close()
AttributeError: 'NoneType' object has no attribute 'close'
