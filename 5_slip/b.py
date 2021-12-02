# B)Write a python script to generate Fibonacci terms using generator function.


def fibgen(itr):
    a = 0 
    b = 1
    for i in range(itr):
        yield a 
        a , b = b , a+b



itr = int(input("Enter the no of fibonachi series that you want"))

print(list(fibgen(itr)))

