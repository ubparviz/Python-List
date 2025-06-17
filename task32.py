# Foydalanuvchi so‘zlar ro‘yxatini kiritadi. 
# Shu ro‘yxatdan faqat uzunligi 5 dan katta bo‘lgan so‘zlarni yangi ro‘yxatga yozing. 
# Misol: ["kitob", "dastur", "AI", "hello", "python"] → ["dastur", "python"]

words = []
big_words = []

for i in range(1, 6):
    word = input(f"{i} - so'zni kiriting: ")
    words.append(word.strip())

for word in words:
    if len(word) > 5:
        big_words.append(word)

print(big_words)