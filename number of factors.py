x=int(input("Enter the number:"))
y=[]
print("the factors of",x,"are:")
for i in range(1,x):
    if x%i==0:
        y.append(i)
        print(y)
        print("number of factors:",len(y))
        n=int(input("enter N value:"))
        if n>len(y):
            print("invalid:")
        else:
            print("first",n,"factors:")
            for k in range(0,n):
                print(y[k],end='')
                            
