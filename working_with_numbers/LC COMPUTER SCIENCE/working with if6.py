bill = input('enter the bill')
bill = float(bill)

if bill >= 2000:
    print('discount will be a 15%')
    
elif bill >= 1500:
    print('discount will be a 10%')
    
elif bill >= 1000:
    print('discount will be a 5%')
    
else:
    print('there is no discount')