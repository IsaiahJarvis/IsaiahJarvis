def primesTo(num):
    list1 = []
    
    for i in range(2, num):
        if isPrime(i) == True:
            list1.append(i)
    return list1

        
def isPrime(num):
    if num == 4:
        return False
    for i in range(2, int(num/2)):
        if (num % i == 0):
            return False
    return True
