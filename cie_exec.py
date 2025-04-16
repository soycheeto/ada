n = int(input("Enter the value count: "))
print("Enter the elements individually: ")
arr = [int(input()) for _ in range(n)]
target = int(input("Enter the search value: "))
for i in range(n):
    if arr[i]==target: 
        print(f"Item found at index {i}")
        found = True
        break
if not found:
    print("Item not found.")