import time
import math

start_time = time.perf_counter()


def isPrime(n):
    if (math.factorial(n-1)+1) % n != 0:
        return False

    return True


def input_P(p=1):
    while isPrime(p) == False or p < 2:
        p = int(input("Please enter a prime number 'P': "))
    return p


def input_Q(q=1):
    while isPrime(q) == False or q < 2:
        q = int(input("Please enter a prime number 'Q': "))
    return q


# ------------------------------------------------------------


p = input_P()
q = input_Q()
n = p*q
func_Euler = (p-1)*(q-1)

list_of_prime_numbers = []
for num in range(2, func_Euler + 1):
    if isPrime(num) and (func_Euler % num != 0):
        list_of_prime_numbers.append(num)

e = min(list_of_prime_numbers)
print("Your public key is: {", e, " ; ", n, "}", sep="")

m = int(input("Enter the text you want to encrypt ('m'): "))

c = m**e % n
print("Your encrypted text: ", c, sep="")

print("Program runtime: ", time.perf_counter() - start_time)
