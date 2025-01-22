def calc(n1,n2,op):
    if op == "1":
        return n1 + n2
    elif op == "2":
        return n1-n2
    elif op == "3":
        return n1*n2
    elif op == "4":
        return n1/n2

valid = ["1", "2", "3", "4", "5"]
while True:
    op = input("Enter 1 for addition, 2 for subtration, 3 for multiplication, 4 for division, and 5 to exit:\n")
    if op == "5":
        print("Exiting the program.")
        break
    if op not in valid:
        print("Invalid input.")
        continue
    n1 = int(input("Enter the first number: \n"))
    n2 = int(input("Enter the second number: \n"))
    calc(n1,n2,op)
    

