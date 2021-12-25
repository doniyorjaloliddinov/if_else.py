# Quyidagi mashqlarni bajaring:
# Quyidagi o'zgaruvchilarni yarating: 
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
#viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.


kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print (manzil)

foy_kocha = input("Ko'changizning nomini kiriting: ")
foy_mahalla = input("Mahallangizni nomini kiriting: ")
foy_tuman = input("Tumaningizni nomini kiriting: ")
foy_viloyat = input("Viloyatingizni nomini kiriting: ")
foy_manzil = ("Sizning to'liq manzilingiz"+ " " + foy_kocha.title() + " " + "ko'chasi," + foy_mahalla.title() + " " + "mahallasi," + foy_tuman.title() + " " + "tumani," + foy_viloyat.title() + " " + "viloyati")
print (foy_manzil)