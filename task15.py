# Foydalanuvchidan start va end indekslarini olib, o‘sha oralig‘dagi bo‘limni chiqaring.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)

print("Qaysi oraliqni olmoqchisiz?")

start = int(input("Nechidan boshlab: "))

stop = int(input("Nechigacha: "))

print(numbers[start:stop+1])