# Foydalanuvchi 6 ta son kiritadi. 
# Shu sonlar orasidan yig‘indisi 10 ga teng bo‘lgan barcha juftliklarni (pair) chiqaring. 
# Misol: input: [1, 2, 3, 7, 8, 9] → output: [(1, 9), (2, 8), (3, 7)]

numbers = []
filter_numbers = []

for i in range(1, 7):

    number = int(input(f"{i} - sonni kiriting: "))
    numbers.append(number)

for i in range(len(numbers)):
    for x in range(i+1, len(numbers)):
        if numbers[i] + numbers[x] == 10:
            filter_numbers.append((numbers[i], numbers[x]))

print(filter_numbers)