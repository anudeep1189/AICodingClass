# 8. Given a list of words, use list comprehension to create a list of words that are palindromes and have length greater than 3.

words = ["madam", "level", "hello", "world", "racecar", "noon", "python", "rotor"]

palindromesLong = [
    word for word in words 
    if len(word) > 3 and word == word[::-1]
]

print(f"Palindromes with length greater than 3: {palindromesLong}")