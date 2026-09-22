temperature = input('enter a temperature of water')
temperature = int(temperature)

if temperature > 100:
    print('it is a gaseous state')
    
elif temperature < 0:
    print('its a solid state')
    
else:
    print('it is liquid')