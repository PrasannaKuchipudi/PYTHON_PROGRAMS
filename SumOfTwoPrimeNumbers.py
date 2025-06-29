def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def check_sum_of_primes(number):
    for i in range(2,number):
        if is_prime(i) and is_prime(number-i):
            print(f"{number}={i}+{number-i}")
            return True
    print(f"{number} cannot be expressed as the sum of two prime numbers.")
    return False
n=int(input("Enter a number:"))
check_sum_of_primes(n)