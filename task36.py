# Foydalanuvchi kiritgan so‘zlar ro‘yxatidan eng uzun so‘zni toping. 
# Shart: Agar bir nechta bo‘lsa, birinchi uchraganini qaytaring.

words = []
longest_word = []

for i in range(5):

    word = input(f"{i+1}-so'zni kiriting: ")
    words.append(word.strip())

max = 0

for word in words:

    if len(word) > max:

        max = len(word)
        longest_word.clear()
        longest_word.append(word)

print(longest_word)