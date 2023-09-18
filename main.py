#1.1 Implement a recursive function to calculate the factorial of the given number
"""
1! = 1×1
2! = 2×1
3! = 3×2×1
"""
def fact_rec(h);
  if n==0 or n==1;
  return 1
  else :
    return n*fact_rec(n-1) 
number=￼2
  res=￼ fact_rec(number)
print("The factorial of {} is {}.".format(number,res)) 

    
  