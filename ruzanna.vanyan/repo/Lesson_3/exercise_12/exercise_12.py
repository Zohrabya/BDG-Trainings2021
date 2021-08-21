cont = int(input("Enter the size of container: "))
if(cont > 1):
    result = round(cont*0.10,2)
    print("The refund amount is: ",result,"$" )
elif(cont<= 1):
    result = round(cont*0.25,2)
    print("The refund amount is:",result,"$" ) 
