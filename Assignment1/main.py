n = 25
k = 10

def iteration(n, k):
    return iterationFactorical(n) / (iterationFactorical(k) * iterationFactorical(n - k))

def recursive(n, k):
    return recursiveFactorical(n) / (recursiveFactorical(k) * recursiveFactorical(n - k))

def iterationFactorical(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

def recursiveFactorical(n):
    if n == 1:
        return 1
    return recursiveFactorical(n - 1) * n

def seperate(n, k):
    if(n == k):
        return 1
    if(k == 1):
        return n
    return seperate(n - 1,  k - 1) + seperate(n - 1, k)

def main():
    pass

def testIteration():
    print(iteration(n, k))

def testRecursive():
    print(recursive(n, k))

def testSeprate():
    print(seperate(n, k))

if __name__ == "__main__":
    main()
