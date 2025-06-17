# input() yordamida foydalanuvchidan 3 ta ism olib ro‘yxat yarating.

names = []

for name in range(3):
    while True:
        name = input("Ismingizni kiriting: ").strip().capitalize()
        if name.isalpha():
            names.append(name)
            break
        else:
            print("Ismni to'g'ri kiriting!")
    
print(names)