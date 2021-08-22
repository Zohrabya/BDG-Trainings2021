#!usr\bin\env python 3

def triangle(side_1, side_2, side_3):  

    #applying the logic
    if (side_1 > side_2 + side_3) or (side_2 > side_1 + side_3) or (side_3 > side_1 + side_2): 
        #if the above condition is true
        print ("Not a valid triangle")  

    #if the above condition is false
    else:  
        print ("A valid triangle") 

triangle (12, 40, 50)  #calling the function