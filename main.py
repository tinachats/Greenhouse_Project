def menu():
    print('1: Set the temperature.')
    print('2: Set the moisture level.')
    print('3: Set the light intensity.')
    print('4: Turn off.')
    
    option = int(input('Enter your option: '))
    
    if option == 1:
        temp_settings()
    elif option == 2:
        moisture_settings()
    elif option == 3:
        light_settings()
    else:
        quit()
        
def temp_settings():
    temp = float(input('Enter your green house temperature value: '))
    print(f'Temp: {temp}° successfully set.')

def moisture_settings():
    moisture = float(input('Enter your green house moisture value: '))
    print(f'Moisture: {moisture}% successfully set.')
    
def light_settings():
    light = float(input('Enter your green house light intensity value: '))
    print(f'Light Intensity: {light}% successfully set.')
    
def display():
    welcome()
    menu()
    
def welcome():
    print('Welcome to Green House Solutions.')
    
display()