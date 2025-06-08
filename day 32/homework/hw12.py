def longest_word(words):
    if not words:
        return "" 
    
    longest = words[0] 
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

words_list = ["გამარჯობა", "დაჯექი", "კომპიუტერი", "პროგრამირება"]
print("ყველაზე გრძელი სიტყვაა:", longest_word(words_list))