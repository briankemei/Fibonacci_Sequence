#Function where it call itself automatically 

def fibonacci_Sequence(term):
    if term <=0:
        return 0
    elif term == 1:
        return 1
    else:
        results = fibonacci_Sequence(term-1) + fibonacci_Sequence(term-2)

    return results

term = int(input("Enter the n term of the fibonacci sequence: "))
print(fibonacci_Sequence(term))