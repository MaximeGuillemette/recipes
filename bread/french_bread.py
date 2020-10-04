import sys

rflour = 1
rwater = 0.7
ryeast = 0.01
rsalt = 0.02

if sys.argv[1] == '-f':
	flour = float(sys.argv[2])
	print(f"flour = {flour * rflour} kg")
	print(f"water = {flour * rwater} kg")
	print(f"yeast = {flour * ryeast} kg")
	print(f"salt = {flour * rsalt} kg")
	print(f"total = {flour * (rflour + rwater + ryeast + rsalt)}")
