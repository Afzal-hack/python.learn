"""
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z
(atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
"""
lugat = { # lug`at yaratish
    'integer':"Butun son",# 'nomi' : 'manosi'
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"
   }

key = input("Kalit so'z kiriting:").lower() # kalit soz so`raladi va kichik simbolga almashtiriladi
print(lugat.get(key,"Bunday so'z mavjud emas"))# lug`at get yordamida tekshiraldi(key) kalit sozi yordamida lug`at ichi dan qidirish