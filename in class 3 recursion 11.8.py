'''
Names in group:
Miguel Salazar, Julio Paveda, Jesus Rodriguez, *RJ Sundseth
Date: 13th March, 2019
Version: 0.0.1
'''

'''
this program uses recursion to fing the greatest number in a list
'''

#julio did this part making the list, defining find_max up to current = x[y-1]
numbers = [765, 180, 240, 110, 930, 400, 222]

def find_max(x, y):                                                       
    if y == 1:                          
        return x[y-1]                                                          
    else:                                                                      
        previous = find_max(x, y-1)                                
        current = x[y-1]     
#RJ did this part he was seeing if previous number in the list is greater than current number in the list 
#up to the print statement where it prints the greatest number.
        if previous > current:                                                 
            return previous                                                    
        else:                                                                  
            return current                                                     

print(find_max(numbers, 7)) #the 7 outside the list says how many elements are in the list and compares them.
