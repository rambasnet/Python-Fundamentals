# Fibonacci numbers module

def fib(n):    
    """
    prints Fibonacci series up to nth term
    """
    a, b = 0, 1
    print(a, b, end=' ')
    i = 2
    while i < n:
        a, b = b, a+b
        print(b, end=' ')
        i += 1
    print()

def fib2(n):   
    """
    returns list of Fibonacci series up to nth term
    """
    result = [0, 1]
    i = 2
    while i < n:
        result.append(result[i-1] + result[i-2])
        i += 1
    return result


def main():
    import sys
    fib(5)
    print(fib2(5))
    fib(int(sys.argv[1]))
    print(fib2(int(sys.argv[1])))

if __name__ == "__main__":
    main()
