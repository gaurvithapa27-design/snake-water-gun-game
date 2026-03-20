def grtno():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=int(input("enter third number"))
    if(a>(b and c)):
        print(a, "is greatest")
    elif(b>(a and c)):
        print(b, "is greatest")
    else:
        print(c, "is greatest")                                 
grtno() 