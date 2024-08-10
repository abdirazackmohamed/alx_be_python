size = int(input("Enter the size of the pattern:"))
row = 0
column = 0
for row < size:
    for column in range(size):
        print("*", end="")
    print()
    row += 1
