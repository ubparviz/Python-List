# Foydalanuvchi kiritgan indeksga qarab ro‘yxatdagi qiymatni yangilang.

taomlar = ["osh", "shurva", "shashlik", "somsa", "manti"]

print(taomlar)
print("Ro'yaxtda qaysi birini LAG'MON ga almashtiramiz")

index = int(input("O'sha taomni Indexsini kiriting: "))

taomlar[index-1] = "lag'mon"

print(taomlar)