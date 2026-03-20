def f(l,word):
    for item in l:
        l.remove(word)
    return l


l=["abra",'cadabra','capybara','abracadabra']


print(f(l,"cadabra"))