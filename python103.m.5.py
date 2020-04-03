#Python103, medium, exercise 5
#print a triangle consisting of rows of 1, 3, 5, & 7 * characters

count = 0

ast = '*'

space = ' '

#for count in range(4):
 #   print((' ' * (count - 1) + ast))

while count == 0:
    print((space * 3) + ast)
    count += 1
    while count == 1:
        print((space * 2) + (ast * 3))
        count += 1
        while count == 2:
            print(space + (ast * 5))
            count += 1
            while count == 3:
                print(ast * 7)
                count += 1