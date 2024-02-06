"""
izoxli lugatdagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
"""
key = input("Kalit so'z kiriting:").lower()
tarans = lugat.get(key)
if tarans == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{key.title()} so'zi {tarans} deb tarjima qilinadi")
