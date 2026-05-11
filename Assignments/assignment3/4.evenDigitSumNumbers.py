# 4. Given a list of numbers, use a loop to build a new list containing only numbers whose digits sum to an even value.

numbers = [12, 23, 34, 45, 56, 67, 78, 89, 10, 111, 202, 314]

even_digit_sum_numbers = []

for num in numbers:
    digit_sum = 0
    temp = num

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if digit_sum % 2 == 0:
        even_digit_sum_numbers.append(num)

print(f"Original list : {numbers}")
print(f"Even digit sum list: {even_digit_sum_numbers}")
