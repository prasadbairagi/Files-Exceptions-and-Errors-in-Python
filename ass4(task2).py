

dt = input("Enter text to write to the file : ")

try:
    with open('output.txt', 'w') as output:
        output.write(dt + '\n')
        print("data successfully written to output.txt")
except Exception as e:
    print("There is a Problem", str(e))


with open("output.txt", 'a') as out2:
    dt2 = input("Please enter additional text to append information : ")
    out2.write(dt2)
    print("data successfully appended")

print("final content of  output.txt")
f = open("output.txt", "r")
print("Line 1 :", f.readline())
print("Line 2 :", f.readline())

