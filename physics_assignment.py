print ('Mathematic & Physics  Operation')
#introduction
first_Name = input('First Name:   ')
last_Name = input('Last Name:    ')

start_viewing_formulars = input('Start Viewing Formulars: ')
#area of a sqaure
def area_of_sqaure():
    length1 = int(input('Enter  a number: '))
    length2 = int(input('Enter  a number: '))
    area = length1*length2
    print(area)
#area of triangle
def area_of_triangle():
    b = float(input('Enter the breadth of the triangle: '))
    h = float(input('Enter the height of the triangle: '))
    area_2 = '1/2' * b * h
    print(area_2)
#area of rectangle
def area_of_rectangle():
    breadth = float(input('Enter the breadth of the rectangle: '))
    height = float(input('Enter the height of the rectangle: '))
    area_3 = breadth * height
    print(area_3)
#formular for force
def force_formular():
    mass = float(input('Enter the mass : '))
    acceleration = float(input('Enter the acceleration : '))
    force = mass * acceleration
    print(force)
#formular of velocity
def velocity_formular():
    displacement = int(input('Enter the displacement : '))
    acceleration = int(input('Enter the acceleration : '))
    velocity = displacement / acceleration
    print(velocity)

options = input('Enter the options:(a,b,c,d,e)       ')

if options == 'a':
    area_of_sqaure()
elif options == 'b':
    area_of_triangle()
elif options == 'c':
    force_formular()
elif options == 'd':
    velocity_formular()
elif options == 'e':
    force_formular()
else:
    print('Invalid option')

print('thank you' + (first_Name)  +    (last_Name) +  'for viewing')




