def calculate_average(numbers):
    if not numbers:
        return 0 
    return sum(numbers) / len(numbers)

nums = [10, 20, 30, 40]
avg = calculate_average(nums)
print("საშუალო არის:", avg)