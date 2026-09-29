cost_price = input('enter a cost price')
cost_price = int(cost_price)
if cost_price >10000:
    print('tax 15%')
    
elif cost_price >5000 and cost_price <=10000:
    print('tax 10%')
    
elif cost_price <= 5000:
    print('tax 5%')