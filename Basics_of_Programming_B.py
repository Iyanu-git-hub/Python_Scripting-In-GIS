# Iyanuoluwa Emmanuel Fatunmbi
# January 22, 2024

# ASSIGNMENT 5
print ("ASSIGNMENT 5")
#A list containing words and numbers
v = ('In', '20', 'days', 'Smith', 'will be', '15')
print(v[4])
print(v[-2])

print()
# ASSIGNMENT 6
print ("ASSIGNMENT 6")
# random.random() --> Random float x, 0.0 <= x < 1.0
# random.randrange(100) --> Random integer from 0 to 99
import random
aNumber = random.randrange(100)

#print random number value format as "The value of the number is aNumber"
print("The value of the number is " + str(aNumber))

#Write the code for the conditions below:
#If aNumber is is greater than or equal to 4 and less than or equal to 32 then show the message "The number is in the range."
if aNumber >= 4 and aNumber <= 32:
    print('The number is in this range.')

#Else If aNumber is greater than 57 and less than 73 then show the message "The number is in the range."
elif aNumber > 57 and aNumber < 73:
    print('The number is in this range.')

#Else show "The number does not belong to any of the ranges."
else:
    print('The number does not belong to any of the range.')
print()
# ASSIGNMENT 7
print ("ASSIGNMENT 7")
#Define a variable 1 with the value "gis---data---source.img"
V1 = "gis---data---source.img"

#Replace V1 with a V2 having a value "gis-data-source.img"
V2 = (V1.replace("---","-"))
print (V2)

#Use the endswith method to determine if variable 2 ends with ".jpg"
print(V2.endswith(".jpg"))
print()
# ASSIGNMENT 8
print("ASSIGNMENT 8")
#Assign a variable list ['Cursors', 'can', 'be', 'used', 'to', 'manipulate', 'data']
XYZ = ''
Variable = ['Cursors', 'can', 'be', 'used', 'to', 'manipulate', 'data']
for Variable_New in Variable:
    XYZ = XYZ + Variable_New + ' '
print(XYZ)
