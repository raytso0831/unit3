#Ray Tso
#2/18/18
#unitConverterUPDATED.py

print('choice_1= Kilometers to Miles')
print('choice_2=  Kilograms to Pounds')
print('choice_3=  Liters to Gallons')
print('choice_4= Celsius to Fahrenheit')

while True:
    choice = (input('Choose a number or type quit: '))
    if choice == '1':
        kilom = float(input('Enter number of Kilometers: '))
        print(kilom, 'kilometers is',kilom*.621,'miles')
    elif choice == '2':
        kilog = float(input('Enter a number of Kilograms: '))
        print(kilog, 'kilograms is',kilog*2.204,'pounds')
    elif choice == '3':
        liter = float(input('Enter a number of Liters: '))
        print(liter, 'liters is',l*.264,'gallons')
    elif choice == 'quit':
        break
    else:
        celsius = float(input('Enter degrees in Celsius: '))
        print(celsius, 'degrees Celsius is',celsius*1.8+32,'degrees Fahrenheit')
    
    
