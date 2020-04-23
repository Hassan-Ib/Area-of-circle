# Area of a circle

print("Welcome, This to calculate the area of circle ")
print()

while True:
    radius = input('input your radius :')
    print()
    if radius == 'exit':
        break

    elif float(radius) == 0:
        print('You cant enter {0} for radius'.format(radius))
        print()
        print('you can enter exit if you are done !')
        print()
        continue

    elif float(radius) < 0:
        print('Sorry!, This is imaginary')
        print()
        print('you can enter exit if you are done !')
        print()
        continue

    elif float(radius) > 0:
        value_of_pi = 3.14159
        Area_of_circle = value_of_pi * (float(radius)**2)
        print('Area of circle = {0}'.format(round(Area_of_circle)))
        print()
        print('you can enter exit if you are done !')
        print()
        continue