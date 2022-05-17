def menu():
    print('1: Set the temperature.')
    print('2: Set the moisture level.')
    print('3: Set the light intensity.')
    print('4: Turn off.')
    
    option = int(input('Enter your option: '))
    
    if option == 1:
        settings()
    elif option == 2:
        settings()
    elif option == 3:
        settings()
    else:
        quit()
        
def settings():
    temp = float(input('Enter your green house temperature value: '))
    moisture = float(input('Enter your green house moisture value: '))
    light = float(input('Enter your green house light intensity value: '))
    set_values = {
        'temp': temp,
        'moisture': moisture,
        'light': light
    }
    return set_values

def display():
    welcome()
    menu()
    
def welcome():
    print('Welcome to Green House Solutions.')
    
display()