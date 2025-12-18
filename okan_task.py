def admin():
    mehsullar=[]

    say=int(input("Mehsul sayini daxil edin: "))
    for _ in range(say):
        adi=input("Mehsulun adi: ")
        qiymeti=float(input("Mehsulun qiymeti: "))
        mehsullar.append((adi,qiymeti))
    return mehsullar

def user(goods):
    istek = input("Axtaris: ")
    c=0
    for i in goods:
        if istek == i[0]:
            print(i[1])
            c+=1
    if c == 0:
        print("Hal-hazirda axtardiginiz mehsul movcud deyil")

print("-----Welcome to Shaghan Shopping Center-----")

goods = admin()

user(goods)
