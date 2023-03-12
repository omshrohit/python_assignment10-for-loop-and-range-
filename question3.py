# write a python script to print first M  multiple of N.
m=int(input("enter the value of m"))
n=int(input("enter  the value of n"))

for i in range(n,m*n+1,n):
    print(i)