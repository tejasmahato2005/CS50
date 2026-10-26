height = 0

while height < 1 or height > 8:
    try:
        height = int(input("Height: "))
        if height < 1 or height > 8:
            print("Enter a  valid height")
    except ValueError:
        print("Enter a  valid height")

for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i+1))
