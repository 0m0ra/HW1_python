n = int(input()) #значение 
if n >= 11 and n <= 14:
        print(n, 'korov')
else:
        temp = n % 10
        if temp == 0 or (temp >= 5 and temp <= 9): # промежуток от 5 до 9
                print(n, 'korov')
        if temp == 1: # кратно 1
                print(n, 'korova')
        if temp >=2 and temp <=4: # промежуток от 2 до 4
                print(n, 'korovy')