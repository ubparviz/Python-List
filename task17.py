# Foydalanuvchi istalgancha ism kiritadi (append bilan), oxirida uzunligini len() bilan chiqaring.

names = []

while True:
    name = input("Ism kiriting ('Ok' deb yozsangiz to'xtaydi): ").strip().capitalize()
    if name.lower() == 'ok':
        break
    names.append(name)

print(f"Jami {len(names)} ta ism kiritildi.")
