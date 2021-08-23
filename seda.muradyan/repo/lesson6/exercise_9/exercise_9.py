def c2f():
   celsius = float(input("What is the Celsius temperature? "))
   fahrenheit = 9/5 * celsius + 32

   print("The temperature {1} is {0:,.2f} degrees Fahrenheit.".format(fahrenheit, celsius))
c2f()