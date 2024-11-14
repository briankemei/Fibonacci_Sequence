'''uses for loop '''
'''
def iterative_Fibonacci(n):
    first = 1
    second = 1
    # List to store the sequence, initialized with the first two terms
    numbers = [first, second]

    for _ in range(2, n):
        term = first + second
        numbers.append(term)
        first = second
        second = term
        
    return numbers

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
print(iterative_Fibonacci(n))
'''
# writing a iterative Fibonacci function using a while loop

def fibonacci_while(n):
    first, second = 0, 1
    numbers = []
    count = 0
    while count < n:
        numbers.append(first)
        first, second = second, first + second
        count += 1
    return numbers

n = int(input("Enter the number of terms: "))
print(fibonacci_while(n))



