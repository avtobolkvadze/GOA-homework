correct_pin = "1234"

attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == correct_pin:
        print("Access Granted")
        break  
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")

if attempts == 0:
    print("Access Denied")