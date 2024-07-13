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
