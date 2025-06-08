start = int(input("შეიყვანეთ დაწყების რიცხვი: "))
end = int(input("შეიყვანეთ დასრულების რიცხვი: "))

if end < start:
    print("არასწორი შუალედი")
else:
    total_sum = 0
    print("შუალედში არსებული რიცხვები:")
    for number in range(start, end + 1):
        print(number)
        total_sum += number
    print("რიცხვების ჯამი:", total_sum)