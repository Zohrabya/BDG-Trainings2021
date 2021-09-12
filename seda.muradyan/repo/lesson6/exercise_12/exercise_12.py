
negatives   = []
zeros  = []
positives   = []

line = input ("Enter an integer(blank to quit):")
while line   !=  "":
   num = int (line)
   if  num   <  0:
      negatives.append(num)
   elif num   >  0:
      positives.append(num)
   else :
      zeros.append(num)

   # Read the next line of input from the user
   line = input ("Enter an integer(blank to quit):")

for   n  in  negatives:
   print (n)
for   n  in  zeros:
   print (n)
for   n  in  positives:
   print (n)