def palindromable(characters):
    char_length = len(characters)
    unique_chars = list(set(characters))
    
    if characters == characters[::-1]:
        return True
    if char_length == 4 and len(unique_chars) == 2:
        return True
    if char_length > 4 and char_length % 2 == 0:
        return False
    if char_length > 4 and char_length % 2 != 0:
        char_count = []
        for i in unique_chars:
            char_count.append(characters.count(i))
        
        if char_count.count(1) > 1:
            return False
        
        for i in char_count:
            if i > 2:
                return False
        return True

if __name__ == "__main__":
    print palindromable('lleve')
    print palindromable('mdaam')
    print palindromable('mother')
    print palindromable('')
    print palindromable('1')