import matplotlib.pyplot as plt

def fibonacci(n):
    list = []
    if n == 0:
        return
    elif n == 1:
        list = [0]
    elif n == 2:
        list = [0, 1]
    else:
        list = [0, 1]
        count = 2;
        for i in range(len(list)):
            while(count != n):
                list.append(list[len(list) - 1]+ list[len(list) - 2])
                count = count + 1
    return list

n = int(input('Enter the range for fibonacci numbers you want to plot : '))
print("Enter 1 for line map \nEnter 2 for red dot map \nEnter 3 for red dash map \nEnter 4 for green triangle map \nEnter 5 for blue square map")
option = int(input("Enter Your Option : "))
if option == 1:
    plt.plot(fibonacci(n))
elif option == 2:
    plt.plot(fibonacci(n), 'ro')
elif option == 3:
    plt.plot(fibonacci(n), 'r--')
elif option == 4:
    plt.plot(fibonacci(n), 'g^')
elif option == 5:
    plt.plot(fibonacci(n), 'bs')
