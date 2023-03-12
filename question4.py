#write a python script to print the first 10 multiples of  N in reverse order.
n=int(input("enter the value of n"))
for i in range(10*n,n-1,-n):
    print(i)