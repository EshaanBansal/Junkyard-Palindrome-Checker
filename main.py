def junkyard_palindrome(items):
    reversed_items = [item[::-1] for item in items]
    char_count = {}
    
    for item in reversed_items:
        for char in item:
            char_count[char] = char_count.get(char, 0) + 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return "No"
    
    return "Yes"
