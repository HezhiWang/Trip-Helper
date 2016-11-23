import ex

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
"""
def draw():
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
"""

class A:
    def __init__(self):
        print('haha')

#ex.a() 
