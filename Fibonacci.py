#Memoization 
n = int(input("Enter the nth term: "))
def fibonacci(n):
     
     if n ==1:

        return 1
     elif n == 2:
        
        return 1
     elif n > 2:
        
        value= fibonacci(n-1)+fibonacci(n-2)
        return value

for n in range(1, n):
    print(n, ':',fibonacci(n))

