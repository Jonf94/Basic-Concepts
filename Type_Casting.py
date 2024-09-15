#You can't divide a strong by a float; so we are going to use the float function. 
#height_cm = input('Height converter: enter your height in cm: ')
#below is correct
#height_cm = input('Height converter: enter your height in cm: ')
#float_height_cm = float(height_cm)
#print('Your height in feet is', float_height_cm / 30.48)

#below is correct
height_cm = float(input('Height converter: enter your height in cm: '))
print('Your height in feet is', height_cm / 30.48)

# now we're going to use the int function : int() ; within our code that we used previously. 
year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')