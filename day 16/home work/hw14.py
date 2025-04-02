correct_pin = "1234"  
attempts = 0  

while True:
    pin = input("Please enter your 4-digit PIN code: ")
    attempts += 1
    
    if pin == correct_pin:
        print(f"Authorization successful! You tried {attempts} times.")
        break  
    else:
        print("Incorrect PIN. Please try again.")