while True:
    num = int(input('Enter Number:'))
    sum = 0 
    for i in range(1,num):
        if num%i==0:
            sum += i
    if sum == num:
        print(f'{num} kamel')
    else :
        print(f'{num} nakamel')
    
    con = input('Exit ? [y/n] ')
    if con[0]=='y' or con[0]=='Y' :
        break