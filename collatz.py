def collatz(number):
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            else: 
                number = 3 * number + 1
                print(number)
print("Enter a number.\n")
try:
    value = int(input())
    collatz(value)
except ValueError:
    print("Error: Please enter a number")

