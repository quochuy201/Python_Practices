#### print n fist fibonaci number and cube it

cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
   
    if n == 0:
        fibonacci_numbers =[]
    elif n == 1:
        fibonacci_numbers=[0]
    else:
        fibonacci_numbers = [0, 1]
        for i in range(2, n):
            fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return(fibonacci_numbers )


n =15

print(list(map(cube, fibonacci(n))))
