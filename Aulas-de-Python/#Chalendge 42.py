#Chalendge 42
l1 = float(input("Enter the line length: "))
l2 = float(input("Enter the other line length: "))
l3 = float(input("Enter one more: "))
if l2 < l1 + l3 and l1 < l2 + l3 and l3 < l2 + l1:
    if l1 == l2 == l3:
        print("\nThese lines form a equilateral triangle.\nBecause all the lines have the same length.\n")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("\nThese lines form a isosceles triangle.\nBecause two lines have the same length.\n")
    else:
        print("\nThese lines form a scalene triangle.\nBecause all the lines have different length.\n")
else:
    print("\nThese lines cannot form a triangle\n")