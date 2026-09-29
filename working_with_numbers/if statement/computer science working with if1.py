a = 20

if a>15:
    print(f'{a} is greater than 15')
    print('this is part of if block')
print('this is not in the if statement')

sales = input('enter their sales for the month')
sales = float(sales)
total = sales*0.15

if sales>40000:
    print(f'{sales} greater than 400000')
print('bonus earned is',total)