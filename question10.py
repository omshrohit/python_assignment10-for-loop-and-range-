# write a python script to print all prime number within a range,# range start=15,end=45.
start=15
end=45
print("-------PRIME NUMBERS--------")
for i in  range(start,end+1):
    for  e in range(2,i):
        if i%e==0:
            break
    else:
        print(i)
