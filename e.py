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
