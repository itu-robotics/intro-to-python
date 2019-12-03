sayi = int(input("Sayi giriniz: "))

def isAsal(n):
    for i in range(2, n):
        if n % i != 0:
            pass
        else:
            return False
    return True
    
print(isAsal(sayi))
    
