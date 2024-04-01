"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

"""

# def my_function():
#   print("Hello from a function")

# my_function()

#passing args

# def sum(a,b):
#     return a+b
# print(sum(2,3))

# #arbitrary args

# def my_function2(*kids):
#     print("The youngs child is "+kids[2])
# my_function2("Emil", "Tobias", "Linus")

#python recursion

"""
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

"""

"""def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)"""

#fibonacci series 

def fib(n):
    if n<=1:
        return n
    else:
         return(fib(n-1) + fib(n-2))
        
for i in range(5):
    print(fib(i))
    


def fact(n):
    if n==1:
        return n
    else:
        return (n*fact(n-1))
num = 5
print("The factorial of",num,"is",fact(num))