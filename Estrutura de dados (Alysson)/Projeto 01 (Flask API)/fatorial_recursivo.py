def fatorial(n):
    #caso base
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)
    
r = fatorial(10)
print (f'O fatorial do número 10 é {r} !')