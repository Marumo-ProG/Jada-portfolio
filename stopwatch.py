'''
    This exercise was meant to demonstrate the use of the time module in python where we created
    a stopwatch that can be used to calculate the time taken to perform a certain task
'''

from time import *
start_point = int(input("Enter 1 to start:"))
start = 0
if start_point == 1:
    start = time()

end_point = int(input("Enter 0 to stop:"))
end = 0
if end_point == 0:
    end = time()

difference_calc =round(end- start, 2)
print(difference_calc)