# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = x / y

# print(f"{z:.2f}")

def main():
    x = int(input("whats x? "))
    print("x squared is", square(x))

def square(num):
    # return num * num
    return pow(num, 2)

main()