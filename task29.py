# Foydalanuvchi 10 ta son kiritadi.
# Shu sonlardan takrorlanmaydigan (faqat bir marta uchragan) sonlardan iborat yangi ro‘yxat yarating. 
# Misol: input: [1, 2, 2, 3, 4, 1, 5, 6, 3, 7] → output: [4, 5, 6, 7]

numbers = []
filter_numbers = []

for i in range(1, 11):

    number = int(input(f"{i} - sonni kiriting: "))
    numbers.append(number)
    
for number in numbers:
    if numbers.count(number) == 1:
        filter_numbers.append(number)


print(filter_numbers)


# yoki qo'shimcha list yaratmasdan, shu listni o'zida filterlasa ham bo'ladi

# numbers = []

# for i in range(1, 11):

#     number = int(input(f"{i} - sonni kiriting: "))
#     numbers.append(number)
    
#     if numbers.count(number) != 1:
#         while number in numbers:
#             numbers.remove(number)


# print(numbers)