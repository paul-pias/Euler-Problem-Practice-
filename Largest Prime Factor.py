import math

def primenumber(num): # Function that generate prime numbers that are in range on given input
    y=[]
    for x in range(0,num):
        if x >1:
            for i in range(2,x):
                if x%i==0: #Checking if the numbers in range of given input number are divisible by itself and another number
                    break #if condition is true then break
            else :
                y.insert(0,x)  # Inserting the prime numbers into a list

    print("Prime Numbers are {}".format(y[::-1]))

def prime_factors(num): # Function that find the factors of prime numbers that are in range on given input
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors



print("Enter Your Number : ")
number=int(input())
primenumber(number)
print("Largest prime_factors of {} is {} ".format(number,prime_factors(number)))



