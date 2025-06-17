# 2 ta ro‘yxat berilgan. Ularda umumiy bo‘lgan elementlarni alohida ro‘yxatga ajrating (takrorlarsiz). 
# Misol: list1 = [1, 2, 3, 4, 5] list2 = [4, 5, 6, 7] → output: [4, 5]

group_A = [1, 2, 3, 4, 5]
group_B = [4, 5, 6, 7]
members_AB = []

for member in group_A :
    if group_B.count(member):
        members_AB.append(member)

print(members_AB)