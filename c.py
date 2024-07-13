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
