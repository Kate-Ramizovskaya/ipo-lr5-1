spis=input("Введите строку для определения (На руском!)")## ввод данных
glas=0 
sogl=0
length=0
vse_glas="яыуаеиоюэЯЫУАИЕОЮЭ"
vse_sogl="йфцчвскмпнртгьшлбщдзжхЙФЦЧУВСКМПНРТГЬШЛБЩДЗЖХ"
for char in spis:
    length+=1
    if char in vse_glas:
        glas+=1
    elif char in vse_sogl:
        sogl+=1

print("Кол-во гласных: ")
print("Кол-во согласных: ")
print("Кол-во букв: ")