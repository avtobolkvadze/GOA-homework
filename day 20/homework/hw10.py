colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

index = int(input("Enter an index (0 to 4): "))

if 0 <= index < len(colors):
    print("Selected color:", colors[index])
else:
    print("Invalid index! Please enter a number between 0 and 4.")