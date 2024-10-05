'''Function that inputs the number of bottles to be shipped by the company. It should print the break-up of the number
of cartons used in descending order of capacity.'''

def NoOfCartonsUsed(BottleNo):
    # Calculate the number of XL cartons
    xl = BottleNo // 48
    xlrem = BottleNo % 48
    
    # Calculate the number of Large cartons
    large = xlrem // 24
    largerem = xlrem % 24
    
    # Calculate the number of Medium cartons
    medium = largerem // 12
    mediumrem = largerem % 12
    
    # Calculate the number of Small cartons
    small = mediumrem // 6
    
    # If there are any remaining bottles (less than 6), they need an additional small carton
    if mediumrem % 6 > 0:
        small += 1
    
    # Print only cartons that are used
    if xl > 0:
        print(f"{xl} XL")
    if large > 0:
        print(f"{large} Large")
    if medium > 0:
        print(f"{medium} Medium")
    if small > 0:
        print(f"{small} Small")

# Input from the user
BottleNo = int(input("Enter the number of bottles to be packed: "))
NoOfCartonsUsed(BottleNo)


