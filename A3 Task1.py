#Task 1: Calculate Factorial Using a Function 
def Factorial(n):
   if n<2:
      return 1
   else:
      return n*Factorial(n-1)
n=int(input(Enter a number:"))
print("Factorial of ",n,"is",Factorial(n))