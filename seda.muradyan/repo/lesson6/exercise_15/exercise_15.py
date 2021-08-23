from   random    import    randrange
minnumber  = 1
maxnumber = 49
numnumbers = 6

# Use a list to store the numbers on the ticket
ticketnums = []

# Generate NUM NUMS random but distinct numbers
for   i  in  range (numnumbers):

   rand = randrange(minnumber, maxnumber  +  1)
   while    rand   in  ticketnums:
      rand = randrange(minnumber, maxnumber +  1)

# Add the number to the ticket
   ticketnums.append(rand)

ticketnums.sort()
print ("Your  numbers are: ",  end="")
for   n  in  ticketnums:
   print (n,    end="    ")
print ()