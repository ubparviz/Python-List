# Foydalanuvchidan 2 ta teng uzunlikdagi ro‘yxat oling. 
# Har bir ro‘yxatdagi mos indekslardagi qiymatlarni bir-biri bilan almashtiring. 
# Misol: list1 = [1, 2, 3] list2 = [4, 5, 6] → list1 = [4, 5, 6], list2 = [1, 2, 3]

list1 = [1, 2, 3,]
list2 = [4, 5, 6,]
list3 = []

print(f"""
=== ASL ===
List1 = {list1}
List2 = {list2}
""")

list3 = list1
list1 = list2
list2 = list3

print(f"""
=== Almashdi ===
List1 = {list1}
List2 = {list2}
""")



