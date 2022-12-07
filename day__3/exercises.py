import math

age = 21
heigth = 52
cpx = (4 + 2j)

print('age: ', age)
print('heigth: ', heigth)
print('cpx: ', cpx)

base = float(input('Enter base: '))
heigth = float(input('Enter heigth: '))
area_triangle = 0.5*heigth*base
print('The area of triangle is', area_triangle)

side_a = float(input('Enter side_a: '))
side_b = float(input('Enter side_b: '))
side_c = float(input('Enter side_c: '))
triangle_perimeter=side_a+side_b+side_c

print('The perimeter of the triangle is', triangle_perimeter)

length = float(input('Enter length: '))
width = float(input('Enter width: '))
print('The area of retangle is: ', length*width)
print('The perimeter of retangle is: ', 2*length+2*width)

radious = float(input('Enter radious: '))
print('The area of circle is ', 3.14*radious**2)
print('The perimeter of circle is ', 2*radious*3.14)

(2,2) (6,10)

mrise =   2 - 6
mrun = 2 - 10
slope = mrise/mrun
print('slope: ', slope)
euclidean_distance = math.sqrt((math.pow(10-2, 2)+math.pow(6-2, 2)))
print('euclidean_distance: ', euclidean_distance)

job_hours = float(input('Enter job hours: '))
rate_hours = float(input('Enter rate per hour: '))
print('total earnings after ' + str(job_hours) + ' hours are: ', job_hours*rate_hours)

lived_years = int(input('Enter number of years you lived: '))
maxyears = 60*60*24*365*100
lived_seconds = 60*60*24*365*lived_years
seconds_remaining = maxyears-lived_seconds

print('You have lived for ' + str(lived_seconds) + ' seconds.')
print('Lets assume that you will lived for 100 (hundred) years')
print('You can live on total for ' + str(maxyears) + ' seconds')
print('You have only ' + str(seconds_remaining) + ' seconds remaining.')

a = 1
b = 1

print(str(a) + ' ' +  str(b) + ' ' + str(a)  + ' ' + str(a*a) + ' ' + str(a*a*a) )
a+=1
print(str(a) + ' ' +  str(b) + ' ' + str(a)  + ' ' + str(a*a) + ' ' + str(a*a*a) )
a+=1
print(str(a) + ' ' +  str(b) + ' ' + str(a)  + ' ' + str(a*a) + ' ' + str(a*a*a) )
a+=1
print(str(a) + ' ' +  str(b) + ' ' + str(a)  + ' ' + str(a*a) + ' ' + str(a*a*a) )
a+=1
print(str(a) + ' ' +  str(b) + ' ' + str(a)  + ' ' + str(a*a) + ' ' + str(a*a*a) )