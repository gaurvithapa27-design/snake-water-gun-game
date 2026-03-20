def f():
    n=int(input("Enter number: " ))
    for i in range(1, 11):
        print(i*n)
    return f()
f()