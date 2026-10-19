x=0
while x == 0:
  try:
     x1, y1 = map(int, input('Введите координаты первой клетки (x1/y1): '). split ('/'))
     x2, y2 = map(int, input('Введите координаты втрой клетки  (x2/y2): '). split ('/'))
     while x1 not in range(1,9) or\
     x2 not in range(1,9) or\
     y1 not in range(1,9) or\
     y2 not in range(1,9) :
      print ('Значения выходят за пределы дозволенного...')
      x1, y1 = map(int, input('Введите координаты первой клетки (x1/y1): '). split ('/'))
      x2, y2 = map(int, input('Введите координаты втрой клетки  (x2/y2): '). split ('/'))
     x=x+1
  except:
      print ('вверите по образцу ЧЕРЕЗ /')
if (x1+y1) % 2 ==0:
    cell1 = 'White'
else:
   cell1 = 'Black'
if (x2+y2) % 2 ==0:
    cell2 = 'White'
else:
    cell2 = 'Black'
if cell1 == cell2:
    print ('Yesssssss!!!!!!!!!! Oni odnogo cveta')
    print ('color vashei kletki - ', cell1 or cell2)
else: 
    print ('No(')


 

  


