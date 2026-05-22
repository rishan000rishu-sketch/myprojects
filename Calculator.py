import math

def sub(num1,num2):
    return num1-num2

def add(num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def sqrt(num):
    return math.sqrt(num)

while True:
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Sqrt')
    print('6. Exit')

    option=input('Select your option: ')

    if option in('1','2','3','4'):
        num1=float(input('Enter first number: '))
        num2=float(input('Enter second number: '))

        if option=='1':   
            print('result is: ',add(num1,num2))

        elif option=='2':
            print('result is: ',sub(num1,num2))

        elif option=='3':
            print('result is: ',mul(num1,num2))

        elif option=='4':
            print('result is: ',div(num1,num2))

    elif option=='5':
        num=float(input('Enter a number: '))
        print(f'The sqrt of {num}: ',sqrt(num))

    elif option=='6':
        print('Exiting program....')
        break

    else:
        print('invalid option')
