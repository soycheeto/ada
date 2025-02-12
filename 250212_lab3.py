"""
normal program: take a number from the user & check primality
activity program: user input range and find primes
"""
import math
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n==1:
            return "1 is neither prime nor composite. \n"
        if n%i==0:
            return f"{n} is composite.\n"

    return f"{n} is prime.\n"

print(prime(3301))

def primeRange():
    sn = int(input("Enter the lower limit: \n"))
    en = int(input("Enter the upper limit: \n"))
    for i in range(sn, en+1):
        print(prime(i))

primeRange()
