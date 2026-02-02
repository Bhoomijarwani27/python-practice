# Function should handle both string & number
def add(a, b):
    return a + b

x = input("Enter first value: ")
y = input("Enter second value: ")

# try converting to number
if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)

print("Result:", add(x, y))


