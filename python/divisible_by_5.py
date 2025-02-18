def check_divisibility(num):
    # Check if the number is divisible by 5
    if num % 5 == 0:
        return "TRUE"
    else:
        return "FALSE"
num = int(input("Enter a number: "))
print(check_divisibility(num))
