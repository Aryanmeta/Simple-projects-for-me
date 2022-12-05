# for & range

def factorial(n):
    result = 1 
    if n < 0 :
        print(False)
    elif n == 0:
        result = 0
    for i in range(1,n+1):
        result *= i
    print(result)

factorial(int(input('Tyoe your number: ')))
