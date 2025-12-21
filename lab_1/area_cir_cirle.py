# to calculate the area and circumference of circle

# take radius

rad = eval(input('Enter radius: '))


# area
PIE = round(22/7, 2)
a = PIE*(rad)**2
# circumference
c = 2*PIE*rad

#display

print('Area : ', a)
print('circumference : ',c)
