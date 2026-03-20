def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["abra",'cadabra','capybara','abracadabra']

print(rem(l,"abra"))
