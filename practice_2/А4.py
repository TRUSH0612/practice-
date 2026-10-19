x = 0
while x == 0:
    try:
        fnum = int(input("введиде число A от 1 до 1000: "))
        snum = int(input("введиде число B от 1 до 1000: "))
        while fnum not in range(1, 1001) or snum not in range(1, 1001):
            print('данные не подходят')
            fnum = int(input("введиде число A от 1 до 1000: "))
            snum = int(input("введиде число B от 1 до 1000: "))
        x = x = 1
    except:
        print('это ж не число')
result = fnum if fnum > snum else snum
print("наибольшее число: ", result)
