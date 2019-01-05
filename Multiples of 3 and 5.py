def multiple(num): #Checking if The given number is divisible by 3 or 5

    if num%3==0 or num%5==0:
        print("Number is Divisible")
    else :
        print("Number is not Divisible")
print("Enter Your Number :")

num=int(input()) # Enter a random number
multiple(num)

count=0
#Summing the numbers that are divisble by either 3 or 5 in range of given input
for i in range(num):

    if i%3==0 or i%5==0:
        count=count+i
print(count)