def pypart(n):
    if n==0:
        return
    else:
        pypart(n-1)
        print("1"*n)
n=5
pypart(n)
