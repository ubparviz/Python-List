# Foydalanuvchi kiritgan 5 ta so‘zdan iborat ro‘yxatdan **palindrom** 
# (masalan: "alla", "kok") so‘zlarni ajratib, yangi ro‘yxatga oling.

words = []
pallindroms = []

for i in range(5):

    word = input(f"{i+1}-so'zni kiriting: ")
    words.append(word)

    if word.strip().lower() == word[::-1].strip().lower():
        pallindroms.append(word)

print("Siz kiritgan so'zlar: ", words)
print("Pallindromlar: ", pallindroms)