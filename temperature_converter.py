print("---temperatur converter---")
C_to_F = "1.Цельсээс Фаренгейтрүү"
print(C_to_F)
F_to_C = "2.Фаренгейтээс Цельсрүү"
print(F_to_C)
C_to_K = "3.Цельсээс Кельвинрүү"
print(C_to_K)
K_to_C = "4.Кельвинээс Цельсрүү"
print(K_to_C)
F_to_K = "5.Фаренгейтээс Кельвинрүү"
print(F_to_K)
K_to_F = ("6.Кельвинээс Фаренгейтрүү")
print(K_to_F)

hurvuuleh_utga = input("Хөрвүүлэх хэмжүүр (тоог бичнэ үү)")
print("Хөрвүүлэх хүсэлт:" + hurvuuleh_utga)
temp_num = int(input("Температурын утга: "))

# CF = (float(temp_num) * 9/5) + 32
# FC = (float(temp_num) - 32) * 5/9
# CK = float(temp_num) + 273.15
# KC = float(temp_num) - 273.15
# FK = (float(temp_num) + 459.67) * 5/9
# KF = float(temp_num) * 9/5 - 459.67
hariu = 0
if hurvuuleh_utga == "1":
    hariu = "Цельсээс Фаренгейтрүү " + str((float(temp_num) * 9/5) + 32) + " болж хөрвөнө."
elif hurvuuleh_utga == "2":
    hariu = "Фаренгейтээс Цельсрүү " + ((float(temp_num) - 32) * 5/9) + " болж хөрвөнө."
elif hurvuuleh_utga == "3":
    hariu = "Цельсээс Кельвинрүү " + str(float(temp_num) + 273.15) + " болж хөрвөнө."
elif hurvuuleh_utga == "4":
    hariu = "Кельвинээс Цельсрүү " + str(float(temp_num) - 273.15) + " болж хөрвөнө."
elif hurvuuleh_utga == "5":
    hariu = "Фаренгейтээс Кельвинрүү " + str((float(temp_num) + 459.67) * 5/9) + " болж хөрвөнө."
elif hurvuuleh_utga == "6":
    hariu = "Кельвинээс Фаренгейтрүү " + str(float(temp_num) * 9/5 - 459.67) + " болж хөрвөнө."

print(f"Температурын утга: {hariu}")
    



