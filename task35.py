# Foydalanuvchi so‘zlardan iborat ro‘yxat kiritadi. So‘zlarni uzunligiga qarab 3 guruhga ajrating:

# <= 3 harfli
# 4-6 harfli
# > 6 harfli Har bir guruh alohida ro'yxatda bo'lsin.

words = []
LenShort_3 = []
LenMiddle4_6 = []
LenLong_6 = []

for i in range(3):

    word = input(f"{i+1}-so'zni kiriting: ")
    words.append(word.strip())

for word in words:
    if len(word) <= 3:
        LenShort_3.append(word)
    elif len(word) >= 4 and len(word) <= 6:
        LenMiddle4_6.append(word)
    else:
        LenLong_6.append(word)

print(f"""
<= 3 harfli: {LenShort_3}
4-6 harfli: {LenMiddle4_6}
> 6 harfli: {LenLong_6}
""")