#!/usr/bin/env python3

password = input("Enter a password: ")

def good_password(p):
    p_list = list(p)
    if len(p) >= 8:
        for s in p_list:
            if s.isalpha():
                for s in p_list:
                    if s.isupper():
                        for s in p_list:
                            if s.isnumeric():    
                                return True    
                            
    return False                
        

print(good_password(password))
