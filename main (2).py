n=int(input("enter the number:"))
def factorial(n):
  if n == 0:
    return 1
 else:
   return n * factorial (n - 1)
print(factorial(n))
year = 2000

if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")