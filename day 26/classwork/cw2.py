full_name = "avto bolkvadze"  
result = ""

for i, char in enumerate(full_name):
    if char.isupper():
        for j in range(i+1, min(i+4, len(full_name))):
            other_char = full_name[j]
            if other_char.isupper():
                result += other_char.lower()

print("Result:", result)