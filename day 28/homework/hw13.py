text = "I visited Georgia, Armenia and Greece"  # სტრიქონი, რომელშიც ვეძებთ
word = input("შეიყვანეთ საძიებელი სიტყვა: ")

position = text.find(word)

if position != -1:
    print("სიტყვა", word, "მოიძებნა პოზიციაზე:", position)
else:
    print("word not found")