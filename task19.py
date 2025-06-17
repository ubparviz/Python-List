# append() yordamida ro‘yxatga yangi ism qo‘shing.

names = ["Ali", "Vali", "Jalil"]
print(names)

name = input("Ism kiriting: ")
names.append(name.strip().capitalize())

print(names)