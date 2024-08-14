#Python program that gives the sum of the first 10 numbers in the Fibonacci seriess
x=int(input("Enter fibonacci number:"))
if x==1:
    fib=[1]
elif x==2:
    fib=[1,1]
else:
    fib=[1,1]
    for i in range(2,x):
        fib.append(fib[i-1]+fib[i-2])
print(fib)