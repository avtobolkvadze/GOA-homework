even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number (negative number to stop): "))
    
    if number < 0:
        break  
    elif number % 2 == 0:
        even_count += 1  
    else:
        odd_count += 1  

print("Even numbers entered:", even_count)
print("Odd numbers entered:", odd_count)