# python103,medium, exercise 4

#Print a box based on user inputs

#defining asterics
aster = '*'

#defining counter
count = 0

#defining width
width = int(input('Enter a number for width: '))

#defining height
height = int(input('Enter a number for height: '))

#checking/printing height and width + printing first line
if height > 0 and width > 0:
    print(f'Width: {width}')
    print(f'Height: {height}')
    print(aster * width)

#prints middle of box
while count < (height - 2):
    print(aster + (' ' * (width - 2)) + aster)
    count += 1

#prints base of box    
print(aster * width)