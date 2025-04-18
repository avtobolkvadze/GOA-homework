total = 0


while True:
    number = int(input("Enter a number (negative number to stop): "))
    
    if number < 0:
        break  
    elif number > 0:
        total += number 


print("Sum of all positive numbers is:", total)