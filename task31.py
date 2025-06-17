# Ro‘yxatda eng ko‘p takrorlangan elementni toping (bir nechta bo‘lsa, birinchisini chiqaring). 
# Misol: input: [3, 5, 3, 2, 5, 5, 1] → output: 5

numbers = []
filter_numbers = []

for i in range(1, 8):

    number = int(input(f"{i} - sonni kiriting: "))
    numbers.append(number)

min = 0

for number in numbers:
    max = numbers.count(number)
    if max > min:
        min = max
        filter_numbers.clear()
        filter_numbers.append(number)

print(filter_numbers)