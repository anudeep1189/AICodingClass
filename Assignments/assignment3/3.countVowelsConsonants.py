# 3. Create a program that reads a string and counts vowels and consonants separately. Ignore spaces and punctuation.

inputString = input("Enter a string : ")

vowels = "aeiou"
vowelCount = 0
consonantCount = 0

for char in inputString:
    charLower = char.lower()
    if 'a' <= charLower <= 'z':  
        if charLower in vowels:
            vowelCount += 1
        else:
            consonantCount += 1

print(f"Number of vowels: {vowelCount}")
print(f"Number of consonants: {consonantCount}")
