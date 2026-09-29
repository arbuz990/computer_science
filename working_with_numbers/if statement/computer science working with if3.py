number1 = input('enter a number')
number1 = float(number1)
number2 = input('enter a number')
number2 = float(number2)
number3 = input('enter a number')
number3 = float(number3)
abc = number1
if abc < number2:
    abc = number2
if abc < number3:
    abc = number3
print('abc is the largest number')