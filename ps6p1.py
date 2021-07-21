print("enter quantity")
q = int(input())
print("enter price")
p = int(input())
ep = q * p
if ep > 100:
    dr = 0.5
    print("your order is more then $100 so I added a discount of 50%")
else:
    dr = 0.2
    print("your order is less then 100 so you get a 20& discount")
d = dr * ep
total = ep - d
print("your total after the discount is " + str(d) + " and without the discount is " + str(ep))
