print("""You enter a dark room with two doors.
Do you go through door #1 or door #2""")

door = input(">   ")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake and run.")
	print("2. Kindly ask the bear his name.")
	
	bear = input(">   ")
	
	if bear == "1":
		print("The bear chases you and eats your face off. Game over!")
	elif bear == "2":
		print("The bears turns and waves then goes back to eating his cake.")
	else:
		print(f"Well doing {bear} is probably not a terrible idea.")
		print("Bear closes the door.")
		
if door == "2":
	print("You enter a room where on a table sits 3 pills and a glass of water.")
	print("What do you do?")
	print("1. Take the red pill?")
	print("2. Take the blue pill?")
	print("3. Take the yellow pill?")
	
	
	pill = input(">  ")
	
	if pill == "1":
		print("You are dropped into a pool of blood filled with pirahnas. Game Over!")
	elif pill == "2":
		print("You enter a crystal clear lake in Colorado.")
	else:
		print("You exit this game of life or death with your life.")
		