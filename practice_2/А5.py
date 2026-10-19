x=0
while x== 0:
   try: 
      fnum = int(input('Введите число А:'))
      snum = int(input('Введите число В:'))
      while snum==0:
        print ('На ноль делить нельзя(')
        fnum = int(input('Введите число А:'))
        snum = int(input('Введите число В:'))
      x=x+1
   except:
        print('Нужно ввести ЧИСЛО')
if fnum % snum ==0:
    print ('YES')
else:
    print ('NO')
