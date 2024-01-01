def magicsquare(n):
    magicSquare = [[0 for i in range(n)] for j in range(n)]
    i = n // 2
    j = n - 1
    
    num = n * n
    count = 1
    
    while(count <= num):
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
                
        if (magicSquare[i][j] != 0):
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[i][j] = count
            count += 1
            
        i = i - 1
        j = j + 1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end = " ")
        print()
    
    print("The sum of each row/column/diagonal is ", str(n*(n**2 + 1)/2))
        
n = int(input("Enter the size of magic square : "))
print("The Solution for a ", n, " x ", n, " magic square is : ")
magicsquare(n)
