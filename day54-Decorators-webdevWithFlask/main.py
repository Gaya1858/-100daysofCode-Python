'''
time.time() will return the current time in seconds since January 1, 1970, 00:00:00
Try running the starting code to see the current time printed.
If you run the code after a while, you'll see a new time printed.
e.g. first run:
1627415818.6527739
second run:
1627415906.237608
The time difference = second run - first run
64.62096405029297
(approx 1 minute)
Given the above information, complete the code exercise by printing out the speed it takes to run the fast_function()
vs the slow_function(). You will need to complete the speed_calc_decorator() function.
Expected Output
https://cdn.fs.teachablecdn.com/RlMWIliS5uAHLA2bB2fh
HINT: You can use function.__name__ to get the name of the function,
SOLUTION: https://repl.it/@appbrewery/day-54-1-solution
'''
import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        current_time1 = time.time()
        current_time2 =current_time1-current_time
        return current_time2
    return wrapper_function
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i*i
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i*i

f =fast_function()
s =slow_function()

print(f"Fast function took {f} seconds to complete")
print(f"Slow function took {s} seconds to complete")

if(f>s):
    diff=f-s
    print(f"Fast funcrion took {diff} seconds extra ")
else:
    diff=s-f
    print(f"Slow funcrion took {diff} seconds extra ")

'''
Fast function took 0.460216760635376 seconds to complete
Slow function took 4.1484739780426025 seconds to complete
Slow funcrion took 3.6882572174072266 seconds extra 
'''