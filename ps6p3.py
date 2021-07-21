print("enter salespersons last name")
sp = str(input())
print("how many sales have gone through")
s = int(input())
if s >= 100000 :
  c = float(.1)
else:
  if s <= 100000:
    c = float(.05)
  else:
    c = float(0)
ny = float(s * .05)
print("Hello " + str(sp) + " your commission is " + str(c) + " and your next year's target is " + str(ny))
