# math.factorial(x)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def perm(n, r):
    result = fact(n) / fact(n-r)
    return result
    
    
def comb(n, r):
    result = perm(n, r) / fact(r)
    return result
    

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

print("Permutasyon: ", perm(num1, num2))
print("Combinasyon: ", comb(num1, num2))