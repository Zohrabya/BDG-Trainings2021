def is_prime(n):
   if n <=  1:
      return False
  
   for x in range (2, n):
      if n % x ==  0:
         return   False
   return    True

def   main():
   value = int (input ("Enter an integer:"))
   if  is_prime(value):
      print (value, "is prime.")
   else :
      print (value, "is not prime.")
if  __name__   == "__main__":
   main()