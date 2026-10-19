x = 0
while x ==0:
    try:
        sek = int(input("введите кол-во секунд: "))
        x = x + 1
    except:
        print ('проверьте введённые данные(')
while sek>86399: # Больше суток
    sek=sek-84000
h=sek // 3600
k=h*3600
sek=sek-k
m=sek // 60
l=m*60
s=sek-l
print ('{:02}:{:02}:{:02}'.format( h, m, s))