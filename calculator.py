operator = input('enter a operator9+,-,*,/):')
num1 = float(input('enter the 1st number:'))
num2 = float(input('enter the 2nd number:'))

if operator =='+':
    result = num1 + num2
    print(round(result, 1))
elif operator =='-':
    result = num1 - num2
    print(round(result, 1))
elif operator =="*":
    result = num1 * num2
    print(round(result, 1))
elif operator =='/':
    result = num1 / num2
    print(round(result, 1))
else:
    print(f'{operator}is not a valid operator')

