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
