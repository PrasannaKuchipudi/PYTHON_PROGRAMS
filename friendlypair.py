def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

def is_friendly_pair(a, b):
    ratio_a = sum_of_divisors(a) / a
    ratio_b = sum_of_divisors(b) / b
    return ratio_a == ratio_b

# Example
num1 = int(input("Enter num1 value:"))
num2 = int(input("Enter num2 value:"))

if is_friendly_pair(num1, num2):
    print(f"{num1} and {num2} are Friendly Pair")
else:
    print(f"{num1} and {num2} are NOT Friendly Pair")
