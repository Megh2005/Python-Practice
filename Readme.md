# **Python Codes**

## (`a.py`) Write a program in Python to print all prime numbers inside a range of numbers provided by the user.

```python
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
lower = int(input("Enter the lower limit of the range: "))
upper = int(input("Enter the upper limit of the range: "))
if lower >= upper:
    print("Invalid range! Lower bound should be less than upper bound.")
else:
    print(f"Prime numbers between {lower} and {upper}:")
    for num in range(lower, upper + 1):
        if is_prime(num):
            print(num)
```

## (`b.py`) Write a Python program to create a Fibonacci sequence till a specific no. of terms and count the number of variables used without any functions.

```python
n = int(input("Enter the number of terms in Fibonacci series: "))
a = 0
b = 1
variable_count = 2
print(f"Fibonacci series up to {n} terms:")
print(a, end=" ")
for _ in range(1, n):
    print(b, end=" ")
    a, b = b, a + b
    variable_count += 1

print(f"\nNumber of variables used in the program: {variable_count}")
```

## (`c.py`) Write a Python program to print the series up to N terms: 1, 3,7, 13, 21, 31… and count the number of mathematical operators used without using any functions.

```python
N = int(input("Enter the number of terms in the series: "))

current_number = 1
step = 2
operator_count = 0
print("Series up to", N, "terms:")
for _ in range(N):
    print(current_number, end=" ")
    if _ < N - 1:
        print(",", end=" ")
    operator_count += 1
    current_number += step
    step += 2
print(f"\nNumber of mathematical operators used: {operator_count}")
```

## (`d.py`) Write a Python program to input a number and check whether it is Krishnamurthy or not, using functions and count the number of iterations used without any functions.

```python
def factorial(num):
    if num == 0 or num == 1:
        return 1
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact
num = int(input("Enter a number : "))
original_num = num
sum_of_factorials = 0
iterations_count = 0
while num > 0:
    digit = num % 10
    sum_of_factorials += factorial(digit)
    num //= 10
    iterations_count += 1
if sum_of_factorials == original_num:
    print(f"{original_num} is a Krishnamurthy number.")
else:
    print(f"{original_num} is not a Krishnamurthy number.")
print(f"Number of iterations used: {iterations_count}")
```

## (`e.py`) Write a Python program to create a list of 20 values and find out Mean, Median and Mode of a list of numbers. Count the number of separators used.

```python
import random
from collections import Counter
import statistics
random.seed(1) 
values = [random.randint(1, 99) for _ in range(20)]
mean = sum(values) / len(values)
median = statistics.median(values)
mode = statistics.mode(values)
separator_count = str(values).count(",")
print(f"List of Values: {values}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Number of separators used: {separator_count}")
```

