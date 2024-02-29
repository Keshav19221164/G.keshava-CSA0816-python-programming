x=int(input("enter the number:"))
y=[]
print("the factors of",x,"are:")
for i in range(1,x+1):
    if x%i==0:
        y.append(i)
print(y)
print("number of factors:",len(y))
n=int(input("enter n value:"))
print(n,"the factors is:",y[n-1])
