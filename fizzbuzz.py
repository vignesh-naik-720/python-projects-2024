def FizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i%5 == 0:
            print(str(i) + " = FizzBuzz")
        elif i % 3 == 0:
            print(str(i) + " = Fizz")
        elif i % 5 == 0:
            print(str(i) + " = Buzz")
        else:
            print(str(i))

n = int(input("Enter the range of numbers : "))
FizzBuzz(n)
