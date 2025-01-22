def cubesquare():
    start = int(input("Enter the start number: \n"))
    end = int(input("Enter the end number: \n"))
    squares = []
    cubes = []
    for i in range(start, end+1):
        if i%2==0:
            squares.append(i**2)
        elif i%2!=0:
            cubes.append(i**3)
    print("Squares of even numbers: \n", squares)
    print("Cubes of odd numbers: \n", cubes)
cubesquare()

def swap():
    n1 = int(input("Enter the first number: \n"))
    n2 = int(input("Enter the second number: \n"))
    temp = n1
    n1 = n2
    n2 = temp
    print("Swapped numbers: \n", n1,n2)