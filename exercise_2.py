def print_rectangle(n, m) :
     
    for x in range(1, n+1) :
        for y in range(1, m+1) :
            if (x == 1 or x == n or
                y == 1 or y == m) :
                print("*", end="")           
            else :
                print(" ", end="")           
         
        print()
rows = 6
columns = 20
print_rectangle(rows, columns)
