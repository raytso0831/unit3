#Ray Tso
#2/18/18
#unitConverterUPDATED.py

print('choice_1= Kilometers to Miles')
print('choice_2=  Kilograms to Pounds')
print('choice_3=  Liters to Gallons')
print('choice_4= Celsius to Fahrenheit')

while True:
    choice = (input('Choose a number from 1-4 or type quit: '))
    if choice == '1':
        kilom = float(input('Enter number of Kilometers: '))
        print(kilom, 'kilometers is',kilom*.621371,'miles')
    elif choice == '2':
        kilo = float(input('Enter a number of Kilograms: '))
        print(kilo, 'kilograms is',kilo*2.204,'pounds')
    elif choice == '3':
        liter = float(input('Enter a number of Liters: '))
        print(liter, 'liters is',liter*.264,'gallons')
    elif choice==4:
        celsius = float(input('Enter degrees in Celcius: '))
        print(celsius, 'degrees Celsius is',)
    elif choice == 'quit':
        break
    else:
        print('ERROR!!!')
        break

    
