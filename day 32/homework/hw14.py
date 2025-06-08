def count_vowels(text):
    vowels = "aeiouAEIOU" 
    count = 0

    for char in text:
        if char in vowels:
            count += 1
        else:
            pass  

    return count

sample_text = "გამარჯობა, როგორ ხარ?"
print("ხმოვნების რაოდენობა:", count_vowels(sample_text))