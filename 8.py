# factorial calculation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_calculation():
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))

factorial_calculation()


host = "https://api.vezubr.com"
print(repr(host))

s = "https://api.vezubr.com "
print(repr(s))