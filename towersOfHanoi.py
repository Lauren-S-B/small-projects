def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Recursion Level =", n)
        print("Move disk 1 from source", source, "to destination", destination)
        print("n=", n, ",", "src =", source, "dest=", destination, "\n")
        return
    # try adding tab
    tab = '   '*n
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print(tab, "Recursion Level =", n)
    print(tab, "Move disk", n, "from source", source, "to destination", destination)
    print(tab, "n=",n,",", "src =", source, "dest=", destination, "\n")
    TowerOfHanoi(n - 1, auxiliary, destination, source)

#n = 4
n = int(input("Please enter the number of disks: "))
TowerOfHanoi(n, '1', '2', '3')

