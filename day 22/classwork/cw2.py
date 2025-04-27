cold_drinks = ["კოკა-კოლა", "ფანტა", "სპრაიტი", "აისი ჩაი", "ენერგეტიკული სასმელი"]
favorite_drink = cold_drinks[1]  

new_drink = input("რომელი ცივი სასმელი გსურთ დაამატოთ მაცივარში? ")
cold_drinks.append(new_drink)  

print("აირჩიეთ სასმელი ამ სიიდან:", cold_drinks)
choice = int(input("რომელი სასმელი გსურთ? შეიყვანეთ ინდექსი (0-დან იწყება): "))
print("თქვენ აირჩიეთ:", cold_drinks[choice]) 

my_name = "ავთო"
print("თქვენი სახელის პირველი 3 სიმბოლოა:", my_name[0:3])