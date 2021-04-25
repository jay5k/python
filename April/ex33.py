i = 0 
numbers = []

while i <6:
	print("")
	print(f"At the top i is {i}:")
	numbers.append(i)
	
	i = i + 1
	
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")
	
print("\nThe numbers:\n ")

for num in numbers:
	print(num)
	