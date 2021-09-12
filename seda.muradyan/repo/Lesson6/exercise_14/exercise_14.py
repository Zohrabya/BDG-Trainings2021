from   random    import    randrange
minnumber  = 1
maxnumber  = 49
numnumbers   = 6

# Use a list to store the numbers on the ticket
ticket_nums = []

for   i  in  range (numnumbers):
   rand = randrange(minnumber, maxnumber +  1)
   while    rand   in  ticket_nums:
      rand = randrange(minnumber, maxnumber   +  1)

   # Add the number to the ticket
   ticket_nums.append(rand)

ticket_nums.sort()
print ("Your      numbers    are:   ",  end="")
for   n  in  ticket_nums:
   print (n,    end="    ")
print ()