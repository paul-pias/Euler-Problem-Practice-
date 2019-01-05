def fibonnaci(num):
    num1=0
    num2=1
    count=0
    nth =0
    x=[]
    y=[]
    if num==num1 :
        print (num1)
    elif num==num2 :
        print(num1,num2)
    else :
        while count<num:
            x.insert(0,num1) # If given number is greater than 1 then insert the fibbonacci numbers into list of x
            nth=num1+num2 
            num1=num2
            num2=nth
            count +=1

            if (num1%2==0):
                y.insert(0,num1)
        print(x[::-1]) # The numbers are then reversed in list for a better view
        print(y[::-1]) # The numbers are then reversed in list for a better view
print("Enter Your Number :")
number=int(input())
fibonnaci(number)


