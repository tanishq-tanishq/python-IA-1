#Design a module math_utils.py with functions: factorial(n),is_prime(n),gcd(a,b).Include exception handling for invalid or negative inputs. Import and test these functions from another script.

# math_utils.py

def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed.")
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
n=int(input("Enter the number: "))
print("The factorial of the number is ",factorial(n))


def is_prime(x):
    count=0
    if x < 2:
        return False
    for i in range(1,x+1):
        if x % i == 0:
            count+=1
    if count<2:
        print("Prime number")
x=int(input("Enter the number: "))
is_prime(x)

    



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(gcd(a,b))

