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
