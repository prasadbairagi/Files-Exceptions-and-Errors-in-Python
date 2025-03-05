

try:
    with open("sample.txt", "r") as f:
        print("Line 2 :", f.readline())
        print("Line 2 :", f.readline())

except FileNotFoundError:
    print("The file 'sample.txt' was not found")
