n=int(input("Enter the number of rows: "))    
def pattern(n):
    if (n==1):
        return
    print("-" * n)
    pattern(n-1)


pattern(n)