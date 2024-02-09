def count_characters(string):
    result = {}

    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


def count_character_two(string):
    result = {}

    for char in string:
        result[char] = string.count(char)
    return result


print(count_characters('google.com'))
print(count_character_two('google.com'))
