def check_divisibility(num):
  # // Expected output is "TRUE" or "FALSE"

num = int(input("Enter a number: "))
print(check_divisibility(num))
if(num % 5 == 0):
  print("True")
else:
    print("False")
